# mmLock：从雷达到数据防护

mmLock 关注的是一个很具体的安全问题：用户离开设备之后，屏幕、文件或业务系统可能还停留在可访问状态。论文的做法不是让摄像头盯着人，而是用毫米波 FMCW 雷达感知人体离开过程，再把这个感知结果接到锁屏或数据保护动作上。

这个站点按学习路径组织。先把雷达讲清楚，再讲 FMCW 雷达如何测距离、速度和角度；然后进入 mmLock 论文，理解它怎样把雷达成像用于用户离开检测；最后落到仓库里的 Python notebook：raw ADC 数据如何经过三次 FFT 变成 radar cube 和点云，点云序列又如何进入 CNN + BiLSTM 模型。

## 建议阅读顺序

1. [雷达基础](radar-basics.md)：先建立直觉，雷达看到的不是照片，而是反射信号。
2. [无线感知](wireless-sensing.md)：先把 WiFi、雷达、声波这类“用信号感知人和环境”的共同逻辑讲清楚。
3. [FMCW 雷达](fmcw-radar.md)：理解 chirp、beat frequency、距离、速度和角度。
4. [mmLock 论文解读](mmlock-paper.md)：把论文系统流程和安全目标串起来。
5. [FFT 处理流程](signal-processing/fft-pipeline.md)：看 raw ADC 怎样变成 range、Doppler、angle 结构。
6. [点云生成](signal-processing/point-cloud.md)：理解一个 radar point 里到底有什么。
7. [Notebook 总览](python-model/notebooks.md)：对应仓库里的三个 notebook。
8. [CNN + BiLSTM](python-model/cnn-blstm.md)：理解点云序列识别模型。

## 文件到页面的对应路径

如果你是从仓库文件开始看，可以按这个顺序走：

| 仓库文件 | 站点页面 | 读这部分要弄清楚什么 |
| --- | --- | --- |
| [`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf) | [mmLock 论文解读](mmlock-paper.md) | 论文问题、系统流程、实验设置和方法边界。 |
| [`mmlock_c61_paper_reading_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_zh.ipynb) | [mmLock 论文解读](mmlock-paper.md)、[无线感知](wireless-sensing.md)、[点云生成](signal-processing/point-cloud.md) | 论文里的图、威胁模型、FFT、点云、模型和实验怎样串起来。 |
| [`radar_fft_cube_progress.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress.ipynb) | [ADC 到 Radar Cube](signal-processing/adc-to-cube.md)、[FFT 处理流程](signal-processing/fft-pipeline.md) | raw ADC 怎么重排成 `[loop, tx, rx, sample]`，三次 FFT 分别处理哪一维。 |
| [`radar_fft_cube_progress_parallel/src/fft_layers.py`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_parallel/src/fft_layers.py) | [FFT 处理流程](signal-processing/fft-pipeline.md) | `range_fft`、`doppler_fft`、`angle_fft` 的输入输出 shape。 |
| [`radar_fft_cube_progress_parallel/src/point_cloud.py`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_parallel/src/point_cloud.py) | [点云生成](signal-processing/point-cloud.md) | range、velocity、angle、power 这些字段怎么从 FFT cube 换算出来。 |
| [`cnn_blstm_pointcloud_training.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training.ipynb) | [CNN + BiLSTM](python-model/cnn-blstm.md)、[训练流程](python-model/training-flow.md) | 点云帧怎么组成序列，CNN 和 BiLSTM 分别处理什么。 |

## 仓库里的三份 notebook

| Notebook | 作用 |
| --- | --- |
| `mmlock_c61_paper_reading_zh.ipynb` | 中文论文阅读笔记，包含系统流程、威胁模型、FFT、点云、PointNet/LSTM 和实验解读。 |
| `radar_fft_cube_progress.ipynb` | 从 DCA1000 raw ADC bin 读取、TDM-MIMO 重排、Range/Doppler/Angle FFT 到点检测的流程。 |
| `cnn_blstm_pointcloud_training.ipynb` | 把逐帧点云组织成序列，训练 CNN + BiLSTM 分类器，并给出片段推理接口。 |

## 论文入口

- 仓库 PDF：[`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf)
- 论文标题：mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging
- DOI：https://doi.org/10.1109/ICCCN58024.2023.10230151
- ASU 论文记录：https://asu.elsevierpure.com/en/publications/mmlock-user-leaving-detection-against-data-theft-via-high-quality/
- 公开 PDF 来源：[ASU CNSG 公开 PDF](https://labs.engineering.asu.edu/cnsg/wp-content/uploads/sites/147/2024/02/C61.pdf)

## 系统位置图

![mmLock paper figure](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-000.png)

这类论文图适合放在系统页里读：雷达采集不是终点，它只是数据入口。真正要看的是后面怎样成像、怎样抽取人体表示、怎样判断用户是否离开，以及这个判断如何影响安全动作。

## 项目材料

- 论文：[`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf)
- 中文论文解读：`mmlock_c61_paper_reading_zh.ipynb`
- FFT 流程 notebook：`radar_fft_cube_progress.ipynb`
- 点云序列模型 notebook：`cnn_blstm_pointcloud_training.ipynb`
- 并行处理代码：`radar_fft_cube_progress_parallel/`
- 论文图：`img/pages/` 和 `img/embedded/`

当前仓库更像一份工程化阅读和复现准备材料，不是完整数据集发布。涉及性能指标、数据规模和实验结论时，以论文和已有 notebook 为准，不在文档里补造数字。

## 无线感知背景

mmLock 用的是毫米波雷达，但它属于更大的无线感知问题：发射一个已知信号，观察这个信号被人体和环境改变后的样子，再从变化里推断人的位置、动作或状态。

WiFi 感知也有相似思路。WiFi CSI 看的是无线信道如何被人体运动扰动；FMCW 雷达看的是专门设计的 chirp 回波如何随距离、速度、角度变化。二者都不是靠摄像头“看见人”，而是靠信号变化“推断发生了什么”。区别在于雷达信号更可控，FMCW 的扫频结构更直接服务于距离和速度估计；WiFi 更依赖通信系统本身的信道测量，空间分辨率和可控性通常不同。
