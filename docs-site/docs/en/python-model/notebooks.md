# Notebooks

The repository contains three notebooks. Together they cover paper reading, radar signal processing, and point-cloud sequence modeling.

## `mmlock_c61_paper_reading_zh.ipynb`

Chinese paper-reading notes for mmLock. It covers the system flow, threat model, point-cloud generation, three FFT stages, MIMO virtual antennas, denoising, PointNet/LSTM modeling, and experiment notes.

## `radar_fft_cube_progress.ipynb`

Signal-processing notebook:

```text
read DCA1000 bin
-> reshape TDM-MIMO frame cube
-> Range FFT
-> Doppler FFT
-> Angle FFT
-> physical-axis conversion
-> point detection
-> visualization
```

## `cnn_blstm_pointcloud_training.ipynb`

Model-training notebook. It loads radar point clouds, builds fixed-length sequences, normalizes features, creates PyTorch datasets, trains CNN + BiLSTM, and provides segment-level inference.

The repository does not include a full public dataset, so the docs describe workflow and interfaces rather than claiming complete reproduction metrics.
