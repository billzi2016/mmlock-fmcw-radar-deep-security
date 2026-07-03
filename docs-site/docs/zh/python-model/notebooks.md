# Notebook 总览

仓库里有三份 notebook，它们分别对应论文阅读、信号处理和模型训练。站点内容应该围绕这三份材料继续扩展。

## `mmlock_c61_paper_reading_zh.ipynb`

这份 notebook 是论文阅读主线。它不是简单翻译论文，而是按工程理解顺序拆解 mmLock：

- 一句话理解 mmLock。
- 系统图和主流程。
- Threat Model。
- Point Cloud Generation。
- 三次 FFT 的直觉和数据形态。
- MIMO 虚拟天线阵列。
- 点云去噪、DBSCAN 聚类和点数规整。
- PointNet + LSTM。
- 实验结果和工程代码对应关系。

这份 notebook 适合继续沉淀到 [mmLock 论文解读](../mmlock-paper.md)、[FFT 处理流程](../signal-processing/fft-pipeline.md) 和 [安全场景](../security-scenario.md)。

## `radar_fft_cube_progress.ipynb`

这份 notebook 是信号处理主线。它把 raw ADC 数据一步步处理成 radar cube 和点：

```text
读取 DCA1000 bin
-> 重排 TDM-MIMO frame cube
-> Range FFT
-> Doppler FFT
-> Angle FFT
-> bin 到物理量换算
-> 点检测
-> 简单可视化
```

它适合用来解释 [ADC 到 Radar Cube](../signal-processing/adc-to-cube.md)、[FFT 处理流程](../signal-processing/fft-pipeline.md) 和 [点云生成](../signal-processing/point-cloud.md)。

## `cnn_blstm_pointcloud_training.ipynb`

这份 notebook 是模型训练主线。它从点云文件开始，构造连续帧动作片段，并训练 CNN + BiLSTM 分类器：

- 设备选择：CUDA / MPS / CPU。
- 点云存储：逐帧 NPZ 或合并 HDF5。
- 标签 CSV。
- 点云读取和固定点数规整。
- 特征归一化。
- Dataset：连续帧组成一个动作样本。
- FramePointCNN。
- CNNBiLSTMClassifier。
- 训练、验证和单片段推理。

它适合继续沉淀到 [CNN + BiLSTM](cnn-blstm.md) 和 [训练流程](training-flow.md)。

## 当前限制

这些 notebook 给出了处理和训练框架，但仓库没有公开完整数据集。文档可以解释流程、接口和数据形态，不能凭空写完整复现实验结果。
