# 图片索引

论文图片保留在仓库根目录的 `img/`。站点使用 GitHub raw 链接引用，不把图片复制进 `docs-site/`，避免同一批二进制文件保存两份。

## 从论文里抽取出来的图

这些图来自 [`img/embedded/`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/tree/main/img/embedded)。它们不是整页截图，而是从论文页面里单独抽出来的图，更适合放进正文解释。读的时候可以把它们分成几类：硬件长什么样、雷达看到什么、FFT/点云中间结果是什么、实验和训练结果怎么展示。

### 雷达硬件与传感器

![pdf_image-002-000](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-000.png)

- 原图：`img/embedded/pdf_image-002-000.png`
- 内容：毫米波雷达开发板正面图。它回答的是“这个项目里的雷达硬件大概长什么样”，不是算法结果图。
- 建议位置：[雷达基础](radar-basics.md)、[项目说明](project-notes.md)。

![pdf_image-008-015](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-008-015.png)

- 原图：`img/embedded/pdf_image-008-015.png`
- 内容：另一张雷达板图片，和 `pdf_image-002-000.png` 属于同一类硬件图。写实验设置时可以用它说明传感器本体。
- 建议位置：[mmLock 论文解读](mmlock-paper.md)。

![pdf_image-008-018](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-008-018.png)

- 原图：`img/embedded/pdf_image-008-018.png`
- 内容：雷达板重复视角，可能来自论文后续实验设置图组。
- 建议位置：实验设置补充页，或保留在图集索引中。

![pdf_image-009-021](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-009-021.png)

- 原图：`img/embedded/pdf_image-009-021.png`
- 内容：雷达板重复视角，适合和其他实验条件图放在一起。
- 建议位置：实验设置或附录图集。

### 雷达视野与感知示意

![pdf_image-002-001](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-001.png)

- 原图：`img/embedded/pdf_image-002-001.png`
- 内容：黑白雷达成像或目标轮廓示意。它适合用来说明一件事：毫米波雷达输出不是可见光照片，而是由回波信号恢复出的空间结构。
- 建议位置：[mmLock 论文解读](mmlock-paper.md)、[点云生成](signal-processing/point-cloud.md)。

![pdf_image-008-016](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-008-016.png)

- 原图：`img/embedded/pdf_image-008-016.png`
- 内容：黑白成像/目标轮廓图，和硬件图配套出现，适合说明雷达观测结果。
- 建议位置：[FMCW 雷达](fmcw-radar.md)、[mmLock 论文解读](mmlock-paper.md)。

![pdf_image-008-019](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-008-019.png)

- 原图：`img/embedded/pdf_image-008-019.png`
- 内容：黑白成像/轮廓示意，可能对应不同实验条件下的雷达视角。
- 建议位置：实验条件说明或附录图集。

![pdf_image-009-022](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-009-022.png)

- 原图：`img/embedded/pdf_image-009-022.png`
- 内容：黑白成像/轮廓示意，适合与同组雷达硬件图一起展示。
- 建议位置：实验设置或附录图集。

![pdf_image-008-017](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-008-017.png)

- 原图：`img/embedded/pdf_image-008-017.png`
- 内容：雷达波束或无线感知示意图，用来解释“发射信号、接收反射”的直觉。
- 建议位置：[雷达基础](radar-basics.md)。

![pdf_image-008-020](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-008-020.png)

- 原图：`img/embedded/pdf_image-008-020.png`
- 内容：雷达波束示意图，和上一张类似，可用于不同实验场景说明。
- 建议位置：[雷达基础](radar-basics.md)。

![pdf_image-009-023](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-009-023.png)

- 原图：`img/embedded/pdf_image-009-023.png`
- 内容：雷达波束示意图，适合作为感知范围或雷达视场的视觉解释。
- 建议位置：[FMCW 雷达](fmcw-radar.md)、实验设置页。

### FFT、热力图与点云

![pdf_image-002-002](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-002.png)

- 原图：`img/embedded/pdf_image-002-002.png`
- 内容：热力图形式的雷达中间结果。颜色越亮，通常表示某些距离或区域上的反射能量越强。它适合放在 FFT 页面里解释“原始信号变成能量图”这一步。
- 建议位置：[FFT 处理流程](signal-processing/fft-pipeline.md)。

![pdf_image-005-006](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-005-006.png)

- 原图：`img/embedded/pdf_image-005-006.png`
- 内容：另一张雷达热力图，适合说明预处理前后的能量分布或人体反射区域。
- 建议位置：[ADC 到 Radar Cube](signal-processing/adc-to-cube.md)、[FFT 处理流程](signal-processing/fft-pipeline.md)。

![pdf_image-002-003](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-003.png)

- 原图：`img/embedded/pdf_image-002-003.png`
- 内容：三维点云图。图里的点不是人体表面扫描点，而是从雷达能量峰里挑出来的反射证据。
- 建议位置：[点云生成](signal-processing/point-cloud.md)。

![pdf_image-002-004](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-002-004.png)

- 原图：`img/embedded/pdf_image-002-004.png`
- 内容：人体形态相关的三维点云，更适合解释毫米波点云如何表示人体。
- 建议位置：[点云生成](signal-processing/point-cloud.md)、[CNN + BiLSTM](python-model/cnn-blstm.md)。

![pdf_image-006-008](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-006-008.png)

- 原图：`img/embedded/pdf_image-006-008.png`
- 内容：多目标或聚类后的三维点云，不同颜色可能表示不同目标或不同簇。
- 建议位置：[点云生成](signal-processing/point-cloud.md)、[安全场景](security-scenario.md)。

![pdf_image-004-005](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-004-005.png)

- 原图：`img/embedded/pdf_image-004-005.png`
- 内容：颜色条，通常是热力图或点云强度图的图例。
- 建议位置：与对应热力图或点云图一起使用，不建议单独成段解释。

![pdf_image-005-007](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-005-007.png)

- 原图：`img/embedded/pdf_image-005-007.png`
- 内容：颜色条，可能对应论文中的热力图或点云强度刻度。
- 建议位置：与对应图组合展示。

### 实验装置

![pdf_image-006-009](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-006-009.png)

- 原图：`img/embedded/pdf_image-006-009.png`
- 内容：实验采集装置照片，能看到支架、雷达设备和桌面环境。
- 建议位置：[mmLock 论文解读](mmlock-paper.md)、[项目说明](project-notes.md)。

![pdf_image-006-010](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-006-010.png)

- 原图：`img/embedded/pdf_image-006-010.png`
- 内容：雷达板与开发板连接的近景图，用于说明实验硬件连接。
- 建议位置：[项目说明](project-notes.md)。

### 模型训练曲线

![pdf_image-007-011](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-007-011.png)

- 原图：`img/embedded/pdf_image-007-011.png`
- 内容：训练 loss 和 validation loss 曲线，显示模型训练过程中的损失变化。
- 建议位置：[CNN + BiLSTM](python-model/cnn-blstm.md)、[训练流程](python-model/training-flow.md)。

![pdf_image-007-012](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-007-012.png)

- 原图：`img/embedded/pdf_image-007-012.png`
- 内容：训练 accuracy 和 validation accuracy 曲线，显示分类性能随 epoch 的变化。
- 建议位置：[训练流程](python-model/training-flow.md)。

![pdf_image-007-013](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-007-013.png)

- 原图：`img/embedded/pdf_image-007-013.png`
- 内容：另一组 loss / validation loss 曲线，可能对应另一阶段模型或实验设置。
- 建议位置：[训练流程](python-model/training-flow.md)，需要结合论文上下文标注具体模型。

![pdf_image-007-014](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/embedded/pdf_image-007-014.png)

- 原图：`img/embedded/pdf_image-007-014.png`
- 内容：另一组 accuracy / validation accuracy 曲线，可能对应另一阶段模型或实验设置。
- 建议位置：[训练流程](python-model/training-flow.md)，需要结合论文上下文标注具体模型。

## 论文页面截图

这些图来自 `img/pages/`，适合做论文导读上下文，不建议替代正文解释。

| 页面图 | 说明 |
| --- | --- |
| ![page-01](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-01.png) | 论文第 1 页，通常包含标题、作者、摘要和引言开头。 |
| ![page-02](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-02.png) | 论文第 2 页，可用于系统动机、背景或早期方法图的上下文。 |
| ![page-03](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-03.png) | 论文第 3 页，适合跟随论文结构做方法导读。 |
| ![page-04](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-04.png) | 论文第 4 页，适合定位点云生成或系统模块说明。 |
| ![page-05](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-05.png) | 论文第 5 页，适合定位 FFT、热力图或预处理相关内容。 |
| ![page-06](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-06.png) | 论文第 6 页，适合定位点云处理、实验设置或模型说明。 |
| ![page-07](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-07.png) | 论文第 7 页，适合定位训练曲线或实验结果。 |
| ![page-08](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-08.png) | 论文第 8 页，适合定位不同实验条件下的结果图。 |
| ![page-09](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-09.png) | 论文第 9 页，适合定位更多实验结果、讨论或相关工作。 |
| ![page-10](https://raw.githubusercontent.com/billzi2016/mmlock-fmcw-radar-deep-security/main/img/pages/page-10.png) | 论文第 10 页，通常用于结论、参考文献或收尾内容。 |
