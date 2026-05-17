"""Configuration for IWR6843/DCA1000 parallel radar FFT processing."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


LAB_CPU_SPEC = {
    "model": "AMD Ryzen Threadripper PRO 5995WX",
    "cores": 64,
    "threads": 128,
    "architecture": "Zen 3",
    "process": "7nm",
    "base_frequency": "2.7 GHz",
    "boost_frequency": "4.5 GHz",
    "l3_cache": "256 MB",
    "tdp": "280W",
    "memory_channels": "8-channel DDR4",
}


@dataclass(frozen=True)
class RadarConfig:
    """All parameters needed to decode ADC bin and build FFT cubes.

    The default values are placeholders for a common IWR6843 TDM-MIMO setup.
    Replace them with the exact mmWave Studio profile/chirp/frame settings before
    processing real experiment data.
    """

    adc_bin_path: Path = Path("adc_data_Raw_0.bin")
    output_dir: Path = Path("outputs/point_clouds")

    # Common IWR6843 TDM-MIMO setting: 3 TX x 4 RX = 12 virtual antennas.
    num_tx: int = 3
    num_rx: int = 4
    num_adc_samples: int = 256
    num_loops_per_frame: int = 128

    range_fft_size: int = 256
    doppler_fft_size: int = 128
    angle_fft_size: int = 64

    # Physical conversion parameters. Must match mmWave Studio profile values.
    sample_rate_hz: float = 5.0e6
    slope_hz_per_s: float = 60.0e12
    start_freq_hz: float = 60.0e9
    chirp_period_s: float = 60.0e-6

    # Detection/output settings.
    threshold_db_above_median: float = 18.0
    max_points_per_frame: int = 4096
    min_range_m: float = 0.15
    max_range_m: float | None = None

    # Parallel settings. None means cpu_count() // 2.
    max_workers: int | None = None
    pool_chunksize: int = 8

    @property
    def chirps_per_frame(self) -> int:
        return self.num_tx * self.num_loops_per_frame

    @property
    def virtual_antennas(self) -> int:
        return self.num_tx * self.num_rx

    @property
    def complex_samples_per_frame(self) -> int:
        return self.chirps_per_frame * self.num_rx * self.num_adc_samples

    @property
    def int16_values_per_frame(self) -> int:
        # Complex ADC samples use I and Q int16 values.
        return self.complex_samples_per_frame * 2

    @property
    def bytes_per_frame(self) -> int:
        return self.int16_values_per_frame * 2

    def worker_count(self) -> int:
        if self.max_workers is not None:
            return max(1, self.max_workers)
        return max(1, (os.cpu_count() or 2) // 2)
