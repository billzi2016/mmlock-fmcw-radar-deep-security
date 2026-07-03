# 点云生成

点云是把 radar cube 里的候选目标点抽出来之后得到的结构。一个点不是一个像素，而是一条雷达反射证据：它告诉我们某个距离、速度、角度位置上有比较明显的回波。

仓库里的 `detect_points` 输出字段包括：

| 字段 | 含义 |
| --- | --- |
| `range_m` | 距离，单位米 |
| `velocity_mps` | 径向速度，单位米每秒 |
| `angle_deg` | 角度，单位度 |
| `power_db` | 反射强度，单位 dB |
| `doppler_bin` | Doppler FFT bin |
| `angle_bin` | Angle FFT bin |
| `range_bin` | Range FFT bin |

## 物理量换算

`point_cloud.py` 里有三个轴换算函数：

- `range_axis_m(cfg)`：把 range bin 换算成距离。
- `velocity_axis_mps(cfg)`：把 Doppler bin 换算成速度。
- `angle_axis_deg(cfg)`：把 angle bin 换算成角度。

这些函数很重要，因为模型最终不应该只看抽象的 bin index。距离、速度和方向才更接近人体行为本身。

## 点云为什么适合后续模型

用户离开不是静态姿势，而是连续动作。单帧点云可以描述某一刻的反射分布，连续点云序列则能描述身体如何移动。CNN + BiLSTM 的思路就是先从每一帧点云里提取空间特征，再让序列模型看时间变化。

## 噪声和稀疏性

雷达点云通常比较稀疏，也会包含环境反射。桌面、墙、椅子边缘都可能产生点。点检测、距离范围过滤、聚类、点数规整和时间序列建模，都是为了减少这些噪声对离开检测的影响。
