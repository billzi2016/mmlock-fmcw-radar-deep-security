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

## 维护原则

- 文档先解释概念，再解释代码。
- 论文图要配说明，不只堆图片。
- notebook 内容要整理成数据流和接口说明。
- 没有数据支撑的实验指标不要写。
- CI 只构建文档，不训练模型，不跑大规模雷达处理。
