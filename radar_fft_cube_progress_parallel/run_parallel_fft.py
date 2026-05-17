"""CLI entry point for frame-wise parallel radar FFT processing."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.config import RadarConfig
from src.parallel_pipeline import process_bin_parallel


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Process TI mmWave Studio/DCA1000 ADC bin with parallel 3-FFT radar pipeline."
    )
    parser.add_argument(
        "--adc-bin",
        type=Path,
        default=Path("adc_data_Raw_0.bin"),
        help="Path to raw ADC bin, for example adc_data_Raw_0.bin.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/point_clouds"),
        help="Directory for per-frame point cloud .npz files.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="Number of worker processes. Default is cpu_count() // 2.",
    )
    parser.add_argument(
        "--num-frames",
        type=int,
        default=None,
        help="Optional number of complete frames to process from the beginning.",
    )
    parser.add_argument(
        "--start-frame",
        type=int,
        default=0,
        help="First frame index to process.",
    )
    parser.add_argument(
        "--threshold-db",
        type=float,
        default=18.0,
        help="Detection threshold in dB above median noise floor.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    cfg = RadarConfig(
        adc_bin_path=args.adc_bin,
        output_dir=args.output_dir,
        max_workers=args.workers,
        threshold_db_above_median=args.threshold_db,
    )

    summary = process_bin_parallel(
        cfg=cfg,
        start_frame=args.start_frame,
        num_frames=args.num_frames,
    )

    print("Parallel radar FFT finished.")
    print(f"Input bin: {summary['adc_bin_path']}")
    print(f"Output dir: {summary['output_dir']}")
    print(f"Workers: {summary['workers']}")
    print(f"Frames requested: {summary['frames_requested']}")
    print(f"Frames processed: {summary['frames_processed']}")
    print(f"Frames failed: {summary['frames_failed']}")


if __name__ == "__main__":
    # multiprocessing on macOS/Windows needs this guard.
    main()
