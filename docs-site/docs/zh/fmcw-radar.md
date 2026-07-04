# FMCW 雷达

FMCW 是 `Frequency-Modulated Continuous Wave`，意思是频率调制连续波。它不只是发一个短脉冲，而是持续发射一段频率随时间变化的信号，这段信号通常叫 `chirp`。

## chirp 可以怎么理解

chirp 像一段不断升高音调的哨声，只不过雷达发的是电磁波，不是声音。发射端知道自己每一刻正在发什么频率；接收端拿到的是延迟后的回波。

如果目标很近，回波回来得快，接收信号和当前发射信号差得不多。如果目标更远，回波回来得更晚，此时发射端已经扫到更高频率了，二者的频率差就更大。

这就是 FMCW 的妙处：它把“时间延迟”变成了“频率差”。频率差比直接测极短的飞行时间更容易处理。

## FMCW 为什么不直接测时间

雷达测距离最直觉的方法是：信号发出去，反射回来，测中间隔了多久。问题是电磁波太快了。光速大约是每秒 3 亿米，1 米距离对应的往返时间只有几纳秒量级。

对普通硬件来说，直接精确测这么短的时间并不容易。FMCW 换了一个更工程化的办法：不直接测飞行时间，而是让发射频率持续变化，然后把延迟转换成频率差。

```text
直接测时间：要分辨非常短的纳秒级延迟
FMCW：把延迟变成 beat frequency，再用 FFT 找频率
```

所以 FMCW 和 FFT 是配套的。FMCW 负责把距离信息编码到频率差里，FFT 负责把频率差从采样数据里拆出来。

可以把 chirp 想成一段“频率坡道”：开始频率较低，随后按固定斜率升高。目标反射回来的信号会比当前发射信号晚一点到达。雷达把发射信号和接收信号混频后，会得到一个频率差，这个差叫 `beat frequency`。

## 距离来自频率差

目标越远，回波延迟越大。因为发射信号的频率一直在爬坡，延迟越大，接收信号和当前发射信号之间的频率差也越大。

简化关系可以写成：

```text
range = c * beat_frequency / (2 * slope)
```

这里 `c` 是光速，`slope` 是 chirp 的扫频斜率。分母里的 `2` 来自往返路径：信号从雷达到目标再回来，走了两倍距离。

一个直观版本：

```text
目标越远 -> 回波越晚 -> beat frequency 越大 -> Range FFT 里的距离 bin 越靠后
```

## 速度来自多个 chirp 之间的变化

一次 chirp 可以提供距离线索，但速度需要看连续 chirp。运动目标会让回波相位在慢时间维度上产生规律变化。沿 chirp 维度做 Doppler FFT，就能把这种变化转成速度相关的频率分量。

这也是为什么 radar 数据通常不是一维数组。它至少会包含：

- fast-time：一个 chirp 内的 ADC sample，用于 Range FFT。
- slow-time：一帧内连续 chirp 或 loop，用于 Doppler FFT。
- channel：多个 RX/TX 组合形成的天线通道，用于角度估计。

所以一个 frame 不是“一张图”，而是一小段时间里的多通道采样。它同时包含一个 chirp 内的快采样、多个 chirp 之间的慢变化，以及多个天线之间的空间差异。

## 角度来自天线阵列

多个接收天线排成阵列时，同一个目标的回波到达各天线会有相位差。沿虚拟天线维度做 Angle FFT，或者使用更细的阵列处理算法，就能估计目标方向。

仓库里的 `radar_fft_cube_progress_parallel/src/fft_layers.py` 用了一个直接的三步流程：

```text
range_fft(frame_cube)
-> doppler_fft(range_cube)
-> angle_fft(doppler_cube)
```

这三步正好对应距离、速度和方向。后续点云检测会在这个三维频域结构上找能量较强的候选点。

## TX 和 RX

`TX` 是 transmit antenna，发射天线。`RX` 是 receive antenna，接收天线。

一套毫米波雷达板上通常有多个 TX 和多个 RX。TX 负责把 chirp 发出去，RX 负责接收人体、桌面、墙面反射回来的信号。一个 TX 和一个 RX 的组合可以看成一条收发通道。

如果有 3 个 TX、4 个 RX，理论上能形成：

```text
3 * 4 = 12 条 TX/RX 通道
```

这些通道不是随便堆起来的。它们在空间中有不同位置，所以同一个目标的回波到达各通道时，相位会不一样。这个相位差就是角度估计的来源。

## TDM-MIMO 是怎么排列的

TDM-MIMO 的意思是 Time-Division Multiplexed MIMO。多个 TX 不同时发，而是按时间轮流发 chirp。这样 RX 收到回波时，系统能知道这次回波对应的是哪个 TX。

一个简化的发射顺序可以画成这样：

```mermaid
flowchart LR
  F[One frame] --> L1[Loop 1]
  L1 --> C11[TX1 chirp]
  C11 --> C12[TX2 chirp]
  C12 --> C13[TX3 chirp]
  F --> L2[Loop 2]
  L2 --> C21[TX1 chirp]
  C21 --> C22[TX2 chirp]
  C22 --> C23[TX3 chirp]
```

每个 chirp 都会被所有 RX 接收。于是一个 frame 可以被整理成：

```text
[loop, tx, rx, sample]
```

这正是仓库代码里 `range_fft` 的输入形状。

## 虚拟天线怎么来

TDM-MIMO 的好处是可以把 TX 和 RX 的组合当成更多“虚拟天线”。如果物理上有 3 个 TX 和 4 个 RX，经过组合后可以得到 12 个 virtual antennas。

```mermaid
flowchart TB
  TX1[TX1] --> RX1[RX1]
  TX1 --> RX2[RX2]
  TX1 --> RX3[RX3]
  TX1 --> RX4[RX4]
  TX2[TX2] --> RX5[RX1]
  TX2 --> RX6[RX2]
  TX2 --> RX7[RX3]
  TX2 --> RX8[RX4]
  TX3[TX3] --> RX9[RX1]
  TX3 --> RX10[RX2]
  TX3 --> RX11[RX3]
  TX3 --> RX12[RX4]
```

代码里的 `angle_fft` 做了这件事：

```python
virtual_cube = doppler_cube.reshape(
    cfg.doppler_fft_size,
    cfg.virtual_antennas,
    cfg.range_fft_size,
)
```

也就是把 `[tx, rx]` 展开成 `virtual_antennas`。这一步的前提是通道顺序要和真实天线几何匹配。当前代码里写得很清楚：这是一个简单展开版本，如果要做严格 IWR6843 方位/俯仰成像，需要换成经过标定的虚拟天线几何顺序。

## 数据维度怎么一路变化

```mermaid
flowchart LR
  A["Raw ADC stream"] --> B["frame cube<br/>[loop, tx, rx, sample]"]
  B --> C["Range FFT<br/>[loop, tx, rx, range_bin]"]
  C --> D["Doppler FFT<br/>[doppler_bin, tx, rx, range_bin]"]
  D --> E["Virtual antenna reshape<br/>[doppler_bin, virtual_ant, range_bin]"]
  E --> F["Angle FFT<br/>[doppler_bin, angle_bin, range_bin]"]
  F --> G["Point detection<br/>range / velocity / angle / power"]
```

看懂这个图，后面的 notebook 就顺了。`sample` 维度解决距离，`loop` 维度解决速度，`tx/rx` 展开的虚拟天线维度解决方向。

## 这和 notebook 怎么对应

[`radar_fft_cube_progress_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_zh.ipynb) 里的函数顺序其实就是一条教学路径：

```text
read_dca1000_complex_bin
```

先把采集卡写出来的二进制 ADC 数据读成复数采样。

```text
reshape_tdm_mimo_frames
```

再按雷达配置把线性采样重排成 `[frame, loop, tx, rx, sample]`。这一步做错，后面的距离可能还像对的，但速度和角度会开始偏。

```text
range_fft -> doppler_fft -> angle_fft
```

最后依次沿 sample、loop、virtual antenna 三个维度做 FFT。每一步都不是“为了用 FFT 而 FFT”，而是在回答不同的物理问题。

## WiFi CSI 和 FMCW 的工程差异

WiFi CSI 也有幅度和相位，也能看到人体运动带来的扰动。但 WiFi 的子载波、天线和信道估计是围绕通信设计的。它能做感知，是因为人体改变了通信信道。

FMCW 雷达的 chirp 则是围绕感知设计的。扫频斜率、采样率、chirp 数量、天线阵列都会直接影响距离分辨率、速度分辨率和角度估计。

一个直观对比：

| 问题 | WiFi CSI 常见做法 | FMCW 雷达常见做法 |
| --- | --- | --- |
| 人在哪里 | 从 CSI 模式间接推断 | Range/Angle 结构更直接 |
| 人动得多快 | 从时间扰动中学习 | Doppler 维度直接建模 |
| 数据像什么 | 子载波和天线上的信道序列 | range-Doppler-angle cube 或点云 |
| 工程优势 | 设备常见、部署方便 | 空间解释强、测距测速自然 |
| 工程难点 | 场景泛化、多径复杂 | 硬件成本、标定、点云噪声 |

这也是为什么 mmLock 的论文会强调 high-quality mmWave radar imaging。它不是只要判断“有人动了”，而是要尽量稳定地理解用户离开设备的空间过程。
