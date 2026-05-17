"""Multiprocessing pipeline for frame-wise radar FFT point-cloud generation."""

from __future__ import annotations

from dataclasses import asdict
from multiprocessing import Pool
from pathlib import Path
import json
import time

import numpy as np

from .config import RadarConfig, LAB_CPU_SPEC
from .dca1000_reader import count_complete_frames, read_frame_adc_cube
from .fft_layers import build_angle_cube
from .point_cloud import detect_points


def process_one_frame(task: tuple[RadarConfig, int]) -> dict:
    """Worker function: read one frame, run 3 FFT layers, save one point cloud."""
    cfg, frame_index = task
    started = time.time()

    try:
        frame_cube = read_frame_adc_cube(cfg.adc_bin_path, cfg, frame_index)
        angle_cube = build_angle_cube(frame_cube, cfg)
        points = detect_points(angle_cube, cfg)

        cfg.output_dir.mkdir(parents=True, exist_ok=True)
        out_path = cfg.output_dir / f"point_cloud_{frame_index:06d}.npz"

        np.savez_compressed(
            out_path,
            points=points,
            frame_index=np.array(frame_index, dtype=np.int64),
            num_points=np.array(points.shape[0], dtype=np.int64),
        )

        return {
            "frame_index": frame_index,
            "ok": True,
            "num_points": int(points.shape[0]),
            "output": str(out_path),
            "seconds": time.time() - started,
        }
    except Exception as exc:  # noqa: BLE001 - keep batch processing alive.
        return {
            "frame_index": frame_index,
            "ok": False,
            "error": repr(exc),
            "seconds": time.time() - started,
        }


def process_bin_parallel(
    cfg: RadarConfig,
    start_frame: int = 0,
    num_frames: int | None = None,
) -> dict:
    """Process a raw ADC bin with multiprocessing.Pool.

    The default process count is cpu_count() // 2. On the lab 5995WX machine,
    that means 64 worker processes instead of saturating all 128 hardware
    threads for a long FFT batch.
    """
    if not cfg.adc_bin_path.exists():
        raise FileNotFoundError(f"ADC bin not found: {cfg.adc_bin_path}")

    available_frames = count_complete_frames(cfg.adc_bin_path, cfg)
    if start_frame >= available_frames:
        raise ValueError(
            f"start_frame={start_frame} is outside available complete frames={available_frames}."
        )

    end_frame = available_frames if num_frames is None else min(
        available_frames,
        start_frame + num_frames,
    )
    frame_indices = list(range(start_frame, end_frame))

    cfg.output_dir.mkdir(parents=True, exist_ok=True)
    workers = min(cfg.worker_count(), len(frame_indices))
    tasks = [(cfg, frame_index) for frame_index in frame_indices]

    print(f"ADC bin: {cfg.adc_bin_path}")
    print(f"Complete frames available: {available_frames}")
    print(f"Frames to process: {len(frame_indices)}")
    print(f"Worker processes: {workers}")
    print("Parallel policy: cpu_count() // 2 by default to reduce thermal load.")

    started = time.time()
    with Pool(processes=workers) as pool:
        results = list(pool.imap_unordered(
            process_one_frame,
            tasks,
            chunksize=cfg.pool_chunksize,
        ))

    ok = [item for item in results if item["ok"]]
    failed = [item for item in results if not item["ok"]]

    summary = {
        "adc_bin_path": str(cfg.adc_bin_path),
        "output_dir": str(cfg.output_dir),
        "cpu_spec": LAB_CPU_SPEC,
        "workers": workers,
        "available_complete_frames": available_frames,
        "start_frame": start_frame,
        "frames_requested": len(frame_indices),
        "frames_processed": len(ok),
        "frames_failed": len(failed),
        "total_points": int(sum(item.get("num_points", 0) for item in ok)),
        "seconds": time.time() - started,
        "failed_examples": failed[:10],
        "config": _jsonable_config(cfg),
    }

    summary_path = cfg.output_dir / "parallel_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def _jsonable_config(cfg: RadarConfig) -> dict:
    data = asdict(cfg)
    for key, value in list(data.items()):
        if isinstance(value, Path):
            data[key] = str(value)
    return data
