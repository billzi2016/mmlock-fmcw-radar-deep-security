# mmLock: From Radar Sensing to Data Protection

mmLock studies a focused device-security problem: after a user leaves a device, the screen or application may remain accessible for a short time. The paper uses mmWave FMCW radar to sense the leaving process and trigger data-protection actions.

This site starts from radar intuition, then explains FMCW sensing, the mmLock paper, FFT-based radar processing, point-cloud generation, and the CNN + BiLSTM notebook workflow.

## Reading Path

1. [Radar Basics](radar-basics.md): what radar measures and why it is not a camera.
2. [Wireless Sensing](wireless-sensing.md): how WiFi CSI, radar, and other signal-based sensing methods are related.
3. [FMCW Radar](fmcw-radar.md): chirps, beat frequency, range, velocity, and angle.
4. [mmLock Paper](mmlock-paper.md): system flow, threat model, and method boundaries.
5. [FFT Pipeline](signal-processing/fft-pipeline.md): how raw ADC samples become radar cubes.
6. [Point Cloud](signal-processing/point-cloud.md): what each radar point means.
7. [Notebooks](python-model/notebooks.md): the three project notebooks and their roles.
8. [CNN + BiLSTM](python-model/cnn-blstm.md): point-cloud sequence classification.

## Project Notebooks

| Notebook | Role |
| --- | --- |
| [`mmlock_c61_paper_reading_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_en.ipynb) | English paper-reading notebook for mmLock. |
| [`radar_fft_cube_progress_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_en.ipynb) | English radar FFT processing workflow. |
| [`cnn_blstm_pointcloud_training_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training_en.ipynb) | English point-cloud sequence modeling workflow. |
| [`mmlock_c61_paper_reading_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_zh.ipynb) | Chinese paper-reading notebook for mmLock. |
| [`radar_fft_cube_progress_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_zh.ipynb) | Chinese radar FFT processing workflow. |
| [`cnn_blstm_pointcloud_training_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training_zh.ipynb) | Chinese point-cloud sequence modeling workflow. |

## Related Code Repositories

- Radar data-processing platform: [mmwave-fmcw-cascade-mimo-sensing-platform](https://github.com/billzi2016/mmwave-fmcw-cascade-mimo-sensing-platform)
- MIMO FMCW radar simulator: [MIMO-FMCW-Radar-Simulator-Multiprocess](https://github.com/billzi2016/MIMO-FMCW-Radar-Simulator-Multiprocess)

The data-processing platform is closer to real mmWave FMCW radar pipelines. The simulator is useful for understanding chirps, MIMO, FFT, virtual antennas, and point-cloud generation in a controlled setting.

## Paper

- Repository PDF: [`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf)
- Title: *mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging*
- DOI: https://doi.org/10.1109/ICCCN58024.2023.10230151
- ASU record: https://asu.elsevierpure.com/en/publications/mmlock-user-leaving-detection-against-data-theft-via-high-quality/
- Public PDF source: [ASU CNSG public PDF](https://labs.engineering.asu.edu/cnsg/wp-content/uploads/sites/147/2024/02/C61.pdf)

![mmLock paper figure](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-000.png)
