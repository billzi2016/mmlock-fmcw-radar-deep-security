# Project Notes

This repository organizes the mmLock paper, radar signal-processing notes, point-cloud modeling workflow, and security scenario explanation.

It is not yet a complete dataset release or a one-command reproduction repository.

## Main Materials

- [`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf): paper PDF.
- `mmlock_c61_paper_reading_zh.ipynb`: Chinese paper-reading notes.
- `radar_fft_cube_progress.ipynb`: raw ADC to radar cube and point-cloud workflow.
- `cnn_blstm_pointcloud_training.ipynb`: point-cloud sequence training workflow.
- `radar_fft_cube_progress_parallel/`: batch FFT and point extraction code.
- `img/`: extracted paper figures.

## Maintenance Rules

- Explain concepts before code.
- Do not duplicate large binary images inside the docs site.
- Convert notebook content into data-flow and interface explanations.
- Do not invent metrics that are not supported by the paper or notebooks.
