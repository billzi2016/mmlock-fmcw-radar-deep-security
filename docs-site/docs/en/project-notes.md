# Project Notes

This repository organizes the mmLock paper, radar signal-processing notes, point-cloud modeling workflow, and security scenario explanation.

It is not yet a complete dataset release or a one-command reproduction repository.

## Main Materials

- [`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf): paper PDF.
- [`mmlock_c61_paper_reading_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_en.ipynb): English paper-reading notes.
- [`radar_fft_cube_progress_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_en.ipynb): English raw ADC to radar cube and point-cloud workflow.
- [`cnn_blstm_pointcloud_training_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training_en.ipynb): English point-cloud sequence training workflow.
- [`mmlock_c61_paper_reading_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_zh.ipynb): Chinese paper-reading notes.
- [`radar_fft_cube_progress_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_zh.ipynb): Chinese raw ADC to radar cube and point-cloud workflow.
- [`cnn_blstm_pointcloud_training_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training_zh.ipynb): Chinese point-cloud sequence training workflow.
- `radar_fft_cube_progress_parallel/`: batch FFT and point extraction code.
- `img/`: extracted paper figures.

## Related Code Repositories

- [mmwave-fmcw-cascade-mimo-sensing-platform](https://github.com/billzi2016/mmwave-fmcw-cascade-mimo-sensing-platform): radar data-processing platform for fuller mmWave FMCW / cascade MIMO sensing pipelines.
- [MIMO-FMCW-Radar-Simulator-Multiprocess](https://github.com/billzi2016/MIMO-FMCW-Radar-Simulator-Multiprocess): MIMO FMCW radar simulator for controlled experiments around chirps, target echoes, virtual antennas, FFT, and point-cloud generation.

## Maintenance Rules

- Explain concepts before code.
- Do not duplicate large binary images inside the docs site.
- Convert notebook content into data-flow and interface explanations.
- Do not invent metrics that are not supported by the paper or notebooks.
