# 项目说明

## 仓库定位

这个仓库用于整理 mmLock 论文材料、雷达信号处理流程、点云建模思路和安全场景说明。它目前不是完整数据集发布，也不是一键复现实验仓库。

## 主要材料

- [`C61.pdf`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/C61.pdf)：论文原文。
- [`mmlock_c61_paper_reading_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_zh.ipynb)：中文论文阅读笔记。
- [`radar_fft_cube_progress.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress.ipynb)：raw ADC 到 FFT cube 和点云的 notebook。
- [`cnn_blstm_pointcloud_training.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training.ipynb)：点云序列分类训练 notebook。
- `radar_fft_cube_progress_parallel/`：批量 FFT 和点云生成代码。
- `img/`：论文页面图和抽取图。

## 相关代码仓库

- [mmwave-fmcw-cascade-mimo-sensing-platform](https://github.com/billzi2016/mmwave-fmcw-cascade-mimo-sensing-platform)：雷达数据处理平台。适合继续看真实 mmWave FMCW 数据处理、cascade/MIMO 感知、工程化 pipeline 和更完整的处理代码。
- [MIMO-FMCW-Radar-Simulator-Multiprocess](https://github.com/billzi2016/MIMO-FMCW-Radar-Simulator-Multiprocess)：MIMO FMCW 雷达模拟器。适合在没有硬件和真实采集数据时，用模拟方式理解 chirp、目标回波、虚拟天线、FFT 和点云生成。

这两个仓库和当前站点的关系可以这样理解：

```text
当前仓库：论文、notebook、mmLock 安全场景和教学文档
真实处理平台：更完整的雷达数据处理代码
模拟器：用可控场景理解 MIMO/FMCW/FFT 的物理和算法
```

## 维护原则

- 文档先解释概念，再解释代码。
- 论文图要配说明，不只堆图片。
- notebook 内容要整理成数据流和接口说明。
- 没有数据支撑的实验指标不要写。
- CI 只构建文档，不训练模型，不跑大规模雷达处理。
