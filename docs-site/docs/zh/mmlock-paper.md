# mmLock 论文解读

论文题目是 *mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging*。它研究的不是一般意义上的人体识别，而是一个更窄的安全动作：当用户离开设备时，系统及时检测并触发数据保护。

## 论文信息

- 仓库 PDF：[`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf)
- 作者：Jiawei Xu, Ziqian Bi, Amit Singha, Tao Li, Yimin Chen, Yanchao Zhang
- 会议：2023 32nd International Conference on Computer Communications and Networks (ICCCN)
- DOI：https://doi.org/10.1109/ICCCN58024.2023.10230151
- ASU 论文记录：https://asu.elsevierpure.com/en/publications/mmlock-user-leaving-detection-against-data-theft-via-high-quality/
- 公开 PDF 来源：[ASU CNSG 公开 PDF](https://labs.engineering.asu.edu/cnsg/wp-content/uploads/sites/147/2024/02/C61.pdf)

## 研究问题

办公设备或个人终端经常会出现一个空档：用户已经离开，但屏幕、文件或业务系统还没有及时锁定。旁边的人可能在这段时间接触敏感信息。mmLock 想解决的就是这个空档。

雷达在这里的角色是感知用户离开过程。它不替代认证系统，也不直接决定权限策略。它提供一个状态判断：用户是否正在离开，是否已经离开，附近是否有干扰目标。

## 系统流程

![mmLock system figure](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-001.png)

这张图可以按数据流读：毫米波雷达先采集人体反射信号；信号处理模块把原始回波转成更容易建模的人体表示；模型根据连续帧判断用户状态；安全模块再根据判断结果触发保护动作。

## 论文和 notebook 的对应关系

[`mmlock_c61_paper_reading_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_zh.ipynb) 已经把论文拆成了多个主题：

- 系统图和主流程。
- Abstract 和 Introduction 的问题背景。
- Threat Model。
- Point Cloud Generation。
- 三次 FFT：Range、Doppler、Angle。
- MIMO 虚拟天线阵列。
- 点云去噪、DBSCAN 聚类和点数规整。
- PointNet + LSTM 的建模思路。
- 单用户实验和附近攻击者实验。

站点后续扩展时，应优先从这份 notebook 抽取解释，而不是重新写一套和项目材料脱节的论文摘要。

## 方法边界

mmLock 的安全意义在于减少用户离开后的暴露窗口。它不是完整的访问控制系统，也不能保证任何环境下都没有误报或漏报。毫米波雷达会受到姿态、速度、环境反射和多目标干扰影响，所以论文里会特别讨论攻击者场景、离开角度、位置、速度、高度和环境变化。

文档写实验结果时要回到论文原文和 notebook，不要在没有依据的情况下补数字。

## 放在无线感知谱系里看

mmLock 可以和 WiFi sensing、RFID sensing、UWB sensing 放在同一类问题里看：它们都用无线信号变化推断人的状态。不同点在于，mmLock 选择的是毫米波 FMCW 雷达，所以它能把信号处理链路组织成比较清楚的空间结构：

```text
chirp 回波
-> range-Doppler-angle cube
-> 人体点云/成像表示
-> 连续帧行为判断
-> 安全动作
```

如果换成 WiFi CSI，数据流通常会变成：

```text
WiFi packet / CSI
-> 子载波幅度和相位序列
-> 去噪、校准、时间窗切片
-> 动作或存在状态分类
```

两条路线都能做“人是否在、是否移动、是否离开”这类任务。但 mmLock 需要处理的是设备前方用户离开这个空间过程，FMCW 雷达的距离、速度、角度结构更容易解释，也更适合和点云建模接上。
