# CNN + BiLSTM

用户离开检测不能只看单帧。人从坐着、起身、转身、离开雷达视野，是一个连续过程。[`cnn_blstm_pointcloud_training_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training_zh.ipynb) 用 CNN + BiLSTM 来处理这种“每帧有空间结构、帧间有时间变化”的数据。

## 模型到底在学什么

可以把输入想成一小段视频，但每一帧不是 RGB 图像，而是一组雷达点：

```text
frame 0: 用户坐着，点云集中在设备前方
frame 1: 用户起身，点云高度和形状变化
frame 2: 用户转身，点云角度变化
frame 3: 用户走开，距离和速度变化
```

CNN 负责从每一帧里提取“这一刻的空间形态”。BiLSTM 负责把多帧连起来，看这段变化是不是离开过程。

## FramePointCNN 看单帧

单帧点云里，每个点都有距离、速度、角度、强度等特征。FramePointCNN 的作用是从一帧点云里提取空间特征。它关注的是这一帧里点的分布形态，而不是完整动作过程。

## BiLSTM 看时间

BiLSTM 会读取连续帧特征。它同时看正向和反向的时间关系，因此适合判断一个动作片段整体上是不是“离开”。这比只看最后一帧更稳，因为用户离开往往有过渡过程。

## 输入和输出

模型输入来自点云序列。典型结构可以理解为：

```text
[batch, sequence_length, num_points, point_features]
```

其中：

- `sequence_length` 是连续帧数量。
- `num_points` 是每帧规整后的点数。
- `point_features` 是点的特征，例如距离、速度、角度、强度。

模型输出是分类结果。这个结果再映射到安全动作，例如是否触发锁屏、是否进入更严格的保护状态。

这里的重点不是模型名字，而是输入结构。只要输入还是点云序列，模型就必须同时处理空间和时间：空间告诉它人在哪里，时间告诉它人往哪里走。

## 和论文模型的关系

论文阅读 notebook 中提到了 PointNet + LSTM。当前仓库的训练 notebook 用 CNN + BiLSTM 组织点云序列，属于同一类思路：先处理每帧空间结构，再建模时间变化。后续如果要严格复现论文模型，应把模型结构、输入格式和训练设置对齐论文描述。
