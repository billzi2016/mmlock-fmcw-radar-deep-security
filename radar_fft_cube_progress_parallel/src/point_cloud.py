"""Point extraction utilities for range-Doppler-angle FFT cubes."""

from __future__ import annotations

import numpy as np

from .config import RadarConfig

LIGHT_SPEED = 299_792_458.0


def range_axis_m(cfg: RadarConfig) -> np.ndarray:
    beat_freq = np.arange(cfg.range_fft_size) * cfg.sample_rate_hz / cfg.range_fft_size
    return LIGHT_SPEED * beat_freq / (2.0 * cfg.slope_hz_per_s)


def velocity_axis_mps(cfg: RadarConfig) -> np.ndarray:
    wavelength = LIGHT_SPEED / cfg.start_freq_hz
    same_tx_chirp_period = cfg.num_tx * cfg.chirp_period_s
    doppler_freq = np.fft.fftshift(
        np.fft.fftfreq(cfg.doppler_fft_size, d=same_tx_chirp_period)
    )
    return doppler_freq * wavelength / 2.0


def angle_axis_deg(cfg: RadarConfig) -> np.ndarray:
    shifted_bins = np.arange(cfg.angle_fft_size) - cfg.angle_fft_size // 2
    sin_theta = 2.0 * shifted_bins / cfg.angle_fft_size
    sin_theta = np.clip(sin_theta, -1.0, 1.0)
    return np.degrees(np.arcsin(sin_theta))


def detect_points(angle_cube: np.ndarray, cfg: RadarConfig) -> np.ndarray:
    """Extract point candidates from [doppler, angle, range] cube.

    The detector intentionally stays simple and explainable for batch
    preprocessing: median noise floor + dB threshold + top-K pruning. Replace it
    with CA-CFAR/OS-CFAR when reproducing final paper-quality detection.
    """
    power = np.abs(angle_cube) ** 2
    power_db = 10.0 * np.log10(power + 1e-12)

    ranges = range_axis_m(cfg)
    velocities = velocity_axis_mps(cfg)
    angles = angle_axis_deg(cfg)

    valid_range = ranges >= cfg.min_range_m
    if cfg.max_range_m is not None:
        valid_range &= ranges <= cfg.max_range_m

    masked_power_db = power_db.copy()
    masked_power_db[:, :, ~valid_range] = -np.inf

    finite_values = masked_power_db[np.isfinite(masked_power_db)]
    if finite_values.size == 0:
        return _empty_points()

    threshold_db = np.median(finite_values) + cfg.threshold_db_above_median
    coords = np.argwhere(masked_power_db > threshold_db)
    if coords.size == 0:
        return _empty_points()

    scores = masked_power_db[coords[:, 0], coords[:, 1], coords[:, 2]]
    order = np.argsort(scores)[::-1][: cfg.max_points_per_frame]
    coords = coords[order]
    scores = scores[order]

    points = np.zeros(coords.shape[0], dtype=_point_dtype())
    for i, (doppler_bin, angle_bin, range_bin) in enumerate(coords):
        points[i] = (
            ranges[range_bin],
            velocities[doppler_bin],
            angles[angle_bin],
            scores[i],
            doppler_bin,
            angle_bin,
            range_bin,
        )
    return points


def _point_dtype() -> list[tuple[str, str]]:
    return [
        ("range_m", "f4"),
        ("velocity_mps", "f4"),
        ("angle_deg", "f4"),
        ("power_db", "f4"),
        ("doppler_bin", "i4"),
        ("angle_bin", "i4"),
        ("range_bin", "i4"),
    ]


def _empty_points() -> np.ndarray:
    return np.zeros(0, dtype=_point_dtype())
