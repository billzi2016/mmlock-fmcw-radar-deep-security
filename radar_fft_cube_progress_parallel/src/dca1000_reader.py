"""Frame-wise reader for TI DCA1000 complex ADC bin files."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from .config import RadarConfig


def count_complete_frames(path: Path, cfg: RadarConfig) -> int:
    """Return the number of complete frames available in a raw ADC bin."""
    file_size = path.stat().st_size
    return file_size // cfg.bytes_per_frame


def _raw_int16_to_complex_stream(raw: np.ndarray) -> np.ndarray:
    """Recover complex ADC stream from common DCA1000 complex LVDS ordering.

    TI's common parser consumes four int16 values and produces two complex
    samples:

        sample_0 = raw[0] + 1j * raw[2]
        sample_1 = raw[1] + 1j * raw[3]

    If the capture lane configuration is different, replace this function with
    the matching lane reorder logic.
    """
    if raw.size % 4 != 0:
        raise ValueError(f"Raw int16 count {raw.size} is not divisible by 4.")

    raw4 = raw.reshape(-1, 4)
    complex_stream = np.empty(raw4.shape[0] * 2, dtype=np.complex64)
    complex_stream[0::2] = raw4[:, 0].astype(np.float32) + 1j * raw4[:, 2].astype(np.float32)
    complex_stream[1::2] = raw4[:, 1].astype(np.float32) + 1j * raw4[:, 3].astype(np.float32)
    return complex_stream


def read_frame_adc_cube(path: Path, cfg: RadarConfig, frame_index: int) -> np.ndarray:
    """Read one complete frame as [loop, tx, rx, sample].

    The function reads only the byte range needed for one frame. This keeps each
    worker memory footprint bounded when processing very large raw bin files.
    """
    offset = frame_index * cfg.bytes_per_frame

    raw = np.memmap(
        path,
        dtype=np.int16,
        mode="r",
        offset=offset,
        shape=(cfg.int16_values_per_frame,),
    )

    # Materialize the memmap slice before FFT so each worker owns a compact array.
    raw = np.asarray(raw)
    complex_stream = _raw_int16_to_complex_stream(raw)

    chirp_cube = complex_stream.reshape(
        cfg.chirps_per_frame,
        cfg.num_rx,
        cfg.num_adc_samples,
    )

    # TDM-MIMO chirp order is assumed to be loop-major then TX-major:
    # loop 0: TX0, TX1, TX2; loop 1: TX0, TX1, TX2; ...
    frame_cube = chirp_cube.reshape(
        cfg.num_loops_per_frame,
        cfg.num_tx,
        cfg.num_rx,
        cfg.num_adc_samples,
    )
    return frame_cube
