"""Separated FFT layers for radar cube construction."""

from __future__ import annotations

import numpy as np

from .config import RadarConfig


def range_fft(frame_cube: np.ndarray, cfg: RadarConfig) -> np.ndarray:
    """Run the first FFT over fast-time ADC samples.

    Input shape:
        [loop, tx, rx, sample]

    Output shape:
        [loop, tx, rx, range_bin]
    """
    window = np.hanning(cfg.num_adc_samples).astype(np.float32)
    windowed = frame_cube * window[None, None, None, :]
    return np.fft.fft(windowed, n=cfg.range_fft_size, axis=-1)


def doppler_fft(range_cube: np.ndarray, cfg: RadarConfig) -> np.ndarray:
    """Run the second FFT over slow-time loops.

    Input shape:
        [loop, tx, rx, range_bin]

    Output shape:
        [doppler_bin, tx, rx, range_bin]
    """
    window = np.hanning(cfg.num_loops_per_frame).astype(np.float32)
    windowed = range_cube * window[:, None, None, None]
    cube = np.fft.fft(windowed, n=cfg.doppler_fft_size, axis=0)
    return np.fft.fftshift(cube, axes=0)


def angle_fft(doppler_cube: np.ndarray, cfg: RadarConfig) -> np.ndarray:
    """Run the third FFT over virtual antennas.

    Input shape:
        [doppler_bin, tx, rx, range_bin]

    Output shape:
        [doppler_bin, angle_bin, range_bin]

    This simple implementation flattens TX/RX into a virtual ULA. For strict
    IWR6843 azimuth/elevation imaging, replace the flattening order with the
    calibrated virtual antenna geometry.
    """
    virtual_cube = doppler_cube.reshape(
        cfg.doppler_fft_size,
        cfg.virtual_antennas,
        cfg.range_fft_size,
    )

    window = np.hanning(cfg.virtual_antennas).astype(np.float32)
    windowed = virtual_cube * window[None, :, None]
    cube = np.fft.fft(windowed, n=cfg.angle_fft_size, axis=1)
    return np.fft.fftshift(cube, axes=1)


def build_angle_cube(frame_cube: np.ndarray, cfg: RadarConfig) -> np.ndarray:
    """Run range FFT -> Doppler FFT -> angle FFT for one frame."""
    r_cube = range_fft(frame_cube, cfg)
    rd_cube = doppler_fft(r_cube, cfg)
    return angle_fft(rd_cube, cfg)
