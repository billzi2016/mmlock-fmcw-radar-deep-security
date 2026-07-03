# Notebook 总览

仓库里有三份 notebook，它们分别对应论文阅读、信号处理和模型训练。不要把它们当成三个孤立文件看，它们其实是一条链：

```text
论文问题和系统设计
-> 雷达原始数据怎样变成点云
-> 点云序列怎样进入模型
-> 模型输出怎样服务用户离开检测
```

如果只打开 notebook 看代码，很容易被函数名和数组 shape 淹没。更好的读法是先问清楚每份 notebook 在回答哪个问题。

| Notebook | 主要问题 | 对应站点页面 |
| --- | --- | --- |
| [`mmlock_c61_paper_reading_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_zh.ipynb) | mmLock 为什么要这样设计，论文图和实验在说明什么。 | [mmLock 论文解读](../mmlock-paper.md)、[无线感知](../wireless-sensing.md) |
| [`radar_fft_cube_progress.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress.ipynb) | raw ADC 数据怎样经过重排和三次 FFT 变成点。 | [ADC 到 Radar Cube](../signal-processing/adc-to-cube.md)、[FFT 处理流程](../signal-processing/fft-pipeline.md) |
| [`cnn_blstm_pointcloud_training.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training.ipynb) | 一段点云序列怎样进入 CNN + BiLSTM 做分类。 | [CNN + BiLSTM](cnn-blstm.md)、[训练流程](training-flow.md) |

## [`mmlock_c61_paper_reading_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_zh.ipynb)

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

### 读这份 notebook 的顺序

先看“系统图”和“Threat Model”，再看“Point Cloud Generation”和“三次 FFT”。原因很简单：如果不知道论文要防什么、系统要判断什么，后面的点云和模型就会变成孤立技术。

建议按这条线读：

```text
一句话理解 mmLock
-> 系统图：雷达、成像、模型、安全动作怎么连
-> Threat Model：用户离开后发生什么风险
-> Point Cloud Generation：论文如何把雷达信号变成人体表示
-> Range/Doppler/Angle FFT：距离、速度、方向从哪里来
-> PointNet + LSTM：为什么要同时看空间和时间
-> 实验结果：哪些场景验证了离开检测
```

### 这份 notebook 在站点里应该展开成什么

论文阅读 notebook 里最值得展开的不是摘要，而是“图怎么读”。比如系统图不能只放出来，还要解释每个模块的输入输出；训练曲线不能只说 accuracy 高，还要说明它对应哪个模型阶段、验证集在看什么。

后续写站点时，这份 notebook 应继续拆成这些专题：

- mmLock 的威胁模型：用户离开后，系统为什么需要快速反应。
- 雷达成像和点云：论文里的 high-quality imaging 到底服务哪个后续模块。
- 目标用户和附近攻击者：为什么多目标场景比单人场景难。
- 实验变量：离开角度、位置、速度、高度和环境变化分别在测试什么。
- 论文方法边界：雷达负责感知，不替代认证和访问控制。

## [`radar_fft_cube_progress.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress.ipynb)

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

### 每一步的输入输出

| 步骤 | 输入 | 输出 | 读者要看懂的点 |
| --- | --- | --- | --- |
| `read_dca1000_complex_bin` | DCA1000 采集的 raw ADC bin | 复数 ADC 采样 | 原始数据不是图，也不是点云，只是按采集顺序写下来的 I/Q 样本。 |
| `reshape_tdm_mimo_frames` | 线性 ADC 样本和雷达配置 | `[frame, loop, tx, rx, sample]` | TX/RX 和 chirp 顺序必须还原对，否则角度维会错。 |
| `range_fft` | `[loop, tx, rx, sample]` | `[loop, tx, rx, range_bin]` | 沿 sample 维做 FFT，把 beat frequency 换成距离结构。 |
| `doppler_fft` | `[loop, tx, rx, range_bin]` | `[doppler_bin, tx, rx, range_bin]` | 沿 loop 维做 FFT，看连续 chirp 之间的相位变化。 |
| `angle_fft` | `[doppler_bin, tx, rx, range_bin]` | `[doppler_bin, angle_bin, range_bin]` | 把 TX/RX 展成虚拟天线，用空间相位差估方向。 |
| `detect_points_from_angle_cube` | 三维 FFT cube | 点云候选点 | 从能量图里挑反射点，并换算成 range、velocity、angle、power。 |

### 这份 notebook 的教学价值

这份 notebook 最适合拿来解释“雷达数据为什么是多维数组”。很多人第一次看 raw ADC 到点云会卡在 shape 上：为什么一会儿是 sample，一会儿是 loop，一会儿又是 tx/rx。

可以把它理解成三类轴：

```text
sample：一个 chirp 内的快采样，负责距离
loop：一帧里的 chirp 重复，负责速度
tx/rx：天线组合，负责角度
frame：时间上的连续片段，负责动作过程
```

所以这份 notebook 不只是代码演示，它是整个项目的数据入口。后面的模型训练能不能解释清楚，很大程度上取决于这里有没有把点云字段和物理意义讲明白。

## [`cnn_blstm_pointcloud_training.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training.ipynb)

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

### 从点云到动作片段

FFT notebook 输出的是一帧一帧的点云。模型 notebook 不能直接把所有点丢进分类器，它要先把连续帧组织成一个动作片段。

一个训练样本可以这样理解：

```text
frame 120: 用户仍坐在设备前
frame 121: 上半身开始移动
frame 122: 用户起身
frame 123: 用户转身
frame 124: 用户离开
```

模型看到的不是“frame 124 这一帧有没有人”，而是“120 到 124 这一段变化像不像离开”。这就是 BiLSTM 存在的原因。

### 点云为什么要规整

每帧点云的点数不固定。有时人体反射点多，有时被噪声、姿态或阈值影响，点会少。神经网络通常需要固定形状输入，所以 notebook 里要把每帧点云处理成固定点数。

这一步不是无关紧要的工程细节。点数规整会影响模型看到什么：

- 截断太狠，可能丢掉人体关键反射。
- 补零太多，模型可能学到无意义的空点模式。
- 采样策略不稳定，训练和推理分布可能不一致。

### CNN 和 BiLSTM 分别承担什么

CNN 处理每一帧的点云特征。它更像是在问：“这一帧里，人体反射分布是什么形态？”

BiLSTM 处理帧之间的变化。它更像是在问：“这段时间里，反射分布是稳定、靠近、远离，还是正在离开？”

最终输出才是离开检测相关的类别。安全系统接到这个输出后，才决定是否触发锁屏或其他保护动作。

## 当前限制

这些 notebook 给出了处理和训练框架，但仓库没有公开完整数据集。文档可以解释流程、接口和数据形态，不能凭空写完整复现实验结果。
