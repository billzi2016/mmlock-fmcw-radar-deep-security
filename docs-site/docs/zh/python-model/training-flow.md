# 训练流程

`cnn_blstm_pointcloud_training.ipynb` 的训练流程从点云文件开始，不从 raw ADC 数据开始。前面的 FFT pipeline 负责把雷达原始数据转成逐帧点云，训练 notebook 负责把这些点云组织成动作片段。

## 数据入口

训练需要两类输入：

- 点云文件：逐帧 NPZ，或合并后的 HDF5。
- 标签文件：CSV，记录动作片段、类别和帧范围。

notebook 中提供了 `load_label_rows`、`point_cloud_path`、`RadarPointSequenceDataset` 和 `H5RadarPointSequenceDataset` 等组件。

## 规整和归一化

雷达每帧检测到的点数不固定。模型训练前要把每帧点云规整到固定点数，常见做法是截断、补零或采样。

特征归一化也很关键。距离、速度、角度和强度的数值范围不同，直接混在一起会让模型训练不稳定。notebook 中的 `PointFeatureNormalizer` 负责处理这个问题。

## 训练步骤

```text
读取标签
-> 读取连续帧点云
-> 规整每帧点数
-> 特征归一化
-> 构造 DataLoader
-> 初始化 CNN + BiLSTM
-> 训练与验证
-> 单片段推理
```

## 当前还缺什么

仓库当前没有完整公开数据集，所以这里不能写完整复现实验指标。后续如果补充数据，需要继续完善：

- 数据目录规范。
- 标签 CSV 示例。
- 训练/验证/测试划分。
- 模型配置文件。
- 评估指标和混淆矩阵。
- 与论文实验设置的对应关系。
