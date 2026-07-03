# 图片索引

论文图片保留在仓库根目录的 `img/`。站点使用 GitHub raw 链接引用，不把图片复制进 `docs-site/`，避免同一批二进制文件保存两份。

## 从论文里抽取出来的图：去重图组

这些图来自 [`img/embedded/`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/tree/main/img/embedded)。PDF 抽图工具会把同一页里重复出现的硬件图、轮廓图、波束图切成多个文件，所以这里按“内容组”合并解释，不再把重复图片当成不同论文信息。

### 图组 A：毫米波雷达板

![毫米波雷达板](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-000.png)

- 代表图：`img/embedded/pdf_image-002-000.png`
- 同组文件：`pdf_image-008-015.png`、`pdf_image-008-018.png`、`pdf_image-009-021.png`
- 这组图讲什么：这是 TI 毫米波雷达板的外观图，用来让读者知道传感器本体长什么样。它不是算法输出，也不是雷达成像结果。
- 该怎么用：在 [雷达基础](radar-basics.md) 或 [项目说明](project-notes.md) 里放一张代表图即可，不需要把四张重复硬件图都放进正文。

### 图组 B：雷达观测轮廓/黑白成像结果

![黑白雷达轮廓](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-001.png)

- 代表图：`img/embedded/pdf_image-002-001.png`
- 同组文件：`pdf_image-008-016.png`、`pdf_image-008-019.png`、`pdf_image-009-022.png`
- 这组图讲什么：这类黑白图展示的是雷达观测或轮廓化后的空间结构。它适合说明“雷达看到的不是照片”，而是由反射信号恢复出的结构。
- 该怎么用：正文里只需要选一张放在 [mmLock 论文解读](mmlock-paper.md) 或 [点云生成](signal-processing/point-cloud.md)，重点解释它和可见光图像的区别。

### 图组 C：无线波束/雷达感知示意

![雷达波束示意](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-008-017.png)

- 代表图：`img/embedded/pdf_image-008-017.png`
- 同组文件：`pdf_image-008-020.png`、`pdf_image-009-023.png`
- 这组图讲什么：这是“发射信号、信号传播、接收反射”的视觉符号。它更像概念图，不是实验结果。
- 该怎么用：适合放在 [无线感知](wireless-sensing.md) 或 [雷达基础](radar-basics.md)，配合解释“信号被人体和环境改变”。

### 图组 D：热力图和颜色条

![雷达热力图](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-002.png)

- 代表图：`img/embedded/pdf_image-002-002.png`
- 同组文件：`pdf_image-005-006.png`
- 配套颜色条：`pdf_image-004-005.png`、`pdf_image-005-007.png`
- 这组图讲什么：热力图展示某个时间/距离/频率区域上的反射能量分布。颜色条只是图例，不应该单独作为正文内容解释。
- 该怎么用：放在 [FFT 处理流程](signal-processing/fft-pipeline.md) 或 [ADC 到 Radar Cube](signal-processing/adc-to-cube.md)，解释 raw ADC 经过 FFT 后为什么会变成能量图。

### 图组 E：点云和聚类结果

![人体点云](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-004.png)

- 代表图：`img/embedded/pdf_image-002-004.png`
- 同组文件：`pdf_image-002-003.png`、`pdf_image-006-008.png`
- 这组图讲什么：点云图展示从 radar cube 中提取出的反射点。它不是人体表面扫描，而是“哪些空间位置有较强回波”的结果。
- 该怎么用：放在 [点云生成](signal-processing/point-cloud.md)。如果讲多目标或攻击者场景，可以使用 `pdf_image-006-008.png` 说明不同簇对应不同人体或反射区域。

### 图组 F：实验装置和硬件连接

![实验装置](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-006-009.png)

- 代表图：`img/embedded/pdf_image-006-009.png`
- 同组文件：`pdf_image-006-010.png`
- 这组图讲什么：实验采集装置、雷达支架、开发板连接和桌面环境。它帮助读者理解论文实验不是纯仿真，而是用 COTS mmWave radar + DCA1000EVM 做采集。
- 该怎么用：放在 [mmLock 论文解读](mmlock-paper.md) 或 [项目说明](project-notes.md)，配合说明硬件、采样和实验环境。

### 图组 G：训练曲线

![训练曲线](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-007-011.png)

- 代表图：`img/embedded/pdf_image-007-011.png`
- 同组文件：`pdf_image-007-012.png`、`pdf_image-007-013.png`、`pdf_image-007-014.png`
- 这组图讲什么：两组 loss/accuracy 曲线，分别对应 PointNet 预训练和 LSTM 训练。它们展示模型是否收敛，但不能脱离训练设置单独解读。
- 该怎么用：放在 [训练流程](python-model/training-flow.md) 或 [CNN + BiLSTM](python-model/cnn-blstm.md)，说明 PointNet 学单帧空间特征，LSTM 学连续动作变化。

## 论文页面截图

这些图来自 [`img/pages/`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/tree/main/img/pages)。它们是论文整页截图，适合做逐页导读。这里不只列“第几页”，而是说明这一页在论文叙事里负责哪一段。

| 页面图 | 说明 |
| --- | --- |
| ![page-01](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-01.png) | **第 1 页：问题提出和摘要。** 这一页先给出论文标题、作者和摘要，然后进入 Introduction。摘要里已经把 mmLock 的主线说完整：用 mmWave FMCW radar 捕捉 3D mesh/point cloud，用 PointNet-LSTM 判断用户离开，目标是比声学 ranging 更快、更稳地触发锁定。Introduction 的前半部分从手机、平板、笔记本丢失和数据泄露讲起，强调“用户离开但设备未锁”是实际安全窗口。读这一页时要抓住论文的动机：它不是做通用手势识别，而是做离开检测以降低数据被旁人访问的风险。 |
| ![page-02](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-02.png) | **第 2 页：系统总览和方法路线。** 这一页顶部的 Figure 1 是 mmLock 全流程：IF signals 先做 preprocessing，得到 range heatmap，再做 point cloud generation 和 point cloud preprocessing，随后用 PointNet 提取单帧空间特征，再用 LSTM 建模时间序列。正文解释为什么 RSSI/CSI 或声学方法不够：它们可能依赖场景、用户或 LOS，而且解释性较弱。这里还交代了实验规模：COTS TI mmWave radar、16 名参与者、超过 1 TB 数据。读这一页要把“信号处理链”和“模型链”连起来。 |
| ![page-03](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-03.png) | **第 3 页：威胁模型和点云生成开头。** 左栏先结束系统概览，进入 Threat Model：假设攻击者拿到或偷到设备，目标是在攻击者接触数据前让设备已锁定；论文不处理破解密码或重装系统这类问题。随后进入 Point Cloud Generation，解释 FMCW chirp、IF signal、Range/Velocity/Angle 如何从回波中提取。读这一页要注意：论文开始把安全问题落到物理信号处理，离开检测不是直接从 raw signal 分类，而是先恢复人体空间点。 |
| ![page-04](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-04.png) | **第 4 页：FMCW、天线阵列和初始点云。** Figure 2 展示 chirp、物理天线阵列和 MIMO 虚拟天线阵列：3 个 TX、4 个 RX 通过 TDM-MIMO 形成 12 个虚拟天线，用于提高角度估计能力。Figure 3 展示离开用户的 raw point cloud，能看到人体相关反射和环境噪声。页面后半进入 Data Preprocessing，开始讲 range heatmap 为什么要筛帧。读这一页要把 TX/RX、虚拟天线、Angle FFT 和点云质量联系起来。 |
| ![page-05](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-05.png) | **第 5 页：热力图预处理、DBSCAN 和 PointNet-LSTM 架构。** Figure 4 是 range heatmap，说明有些 frame 有强人体反射，有些 frame 信息少，所以需要筛出有用帧。Figure 5 是 DBSCAN 后的点云聚类，绿色簇对应目标用户。正文还讲了把相邻 5 帧点云合并、从 1200 点到 6000 点、再通过聚类/能量阈值/点数规整得到 2048 点输入。Figure 6 给出 PointNet + LSTM 网络结构。读这一页要看清楚：模型前面有大量点云清洗，不是 raw point cloud 直接进网络。 |
| ![page-06](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-06.png) | **第 6 页：LSTM 细节、攻击者场景和实验平台。** 左栏继续给出 LSTM 门控公式和最终分类层。随后进入有攻击者的场景：Figure 7 展示合法用户和攻击者形成的两个点云簇，论文用 cluster center 和 center of mass 在相邻帧之间关联目标用户；如果两个簇靠得太近，还要处理簇合并。右栏开始 Implementation and Evaluation，Figure 8 是测试平台：IWR6843ISK-ODS + DCA1000EVM。读这一页要关注“多目标追踪”如何把安全场景变难。 |
| ![page-07](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-07.png) | **第 7 页：模型训练和单用户评估。** Figure 9 是 PointNet 预训练 loss/accuracy，Figure 10 是 LSTM 训练 loss/accuracy。正文给出训练细节：PointNet 用 34 个静态姿态预训练，输入是 2048×3 点云；LSTM 用动态手势，5 类离开动作和 4 类无关动作，每个 gesture 重复 110 次，每个样本 30 个点云。右栏开始单用户评估：false negative、false positive、不同离开动作。读这一页要把“静态姿态学空间特征”和“动态动作学时间特征”区分开。 |
| ![page-08](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-08.png) | **第 8 页：姿态表和环境变量实验。** 上半部分 Table I 列出 34 个用于 PointNet 预训练的静态姿态，覆盖坐姿、起身中间态、站立、转身、迈步、举手等动作形态。下半部分 Figure 11/12 展示离开角度和离开位置实验设置。正文讨论不同 departing gesture、leaving angle、departing speed、vertical radar position、experimental environment 的影响。读这一页要关注论文如何证明系统不是只对一个固定动作或一个固定位置有效。 |
| ![page-09](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-09.png) | **第 9 页：附近攻击者实验和相关工作。** Figure 13 给出附近攻击者的位置设置，Figure 14 给出不同攻击者位置下的 precision/recall。正文说明合法用户和攻击者同时运动时，系统需要识别目标用户而不是被旁人动作误导。右栏进入 Related Work，比较一次性认证、连续认证、离开后立即锁定、声学 ranging 等路线。读这一页要看论文的安全贡献：不是只检测“有人动了”，而是要在多移动目标中跟踪合法用户离开。 |
| ![page-10](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-10.png) | **第 10 页：相关工作收束、结论和参考文献。** 页面开头继续比较已有 mmWave sensing/imaging 工作：有些依赖视觉系统提供 ground truth，有些使用定制 radar 或面向静态物体；mmLock 强调用 COTS mmWave radar 生成高质量点云，直接服务用户离开检测。Conclusion 总结系统设计和实验结果：生成目标用户点云、识别离开手势、相比 acoustic ranging 更能处理多移动物体。后半是致谢和参考文献。读这一页要把 mmLock 放回无线感知、安全认证和 mmWave imaging 三条相关工作线里看。 |
