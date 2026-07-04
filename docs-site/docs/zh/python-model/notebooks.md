# Notebook 总览

仓库里现在有六份 notebook：三份中文、三份英文。中文文档先列中文版本，再列英文版本。代码单元保持同一套逻辑，英文版主要服务英文读者阅读标题和说明。

## 中文版本

| Notebook | 作用 |
| --- | --- |
| [`mmlock_c61_paper_reading_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_zh.ipynb) | 论文阅读主线：系统流程、威胁模型、FFT、点云、PointNet/LSTM、实验结果。 |
| [`radar_fft_cube_progress_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_zh.ipynb) | 信号处理主线：raw ADC、TDM-MIMO 重排、Range/Doppler/Angle FFT、点检测。 |
| [`cnn_blstm_pointcloud_training_zh.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training_zh.ipynb) | 模型训练主线：点云序列、固定点数规整、特征归一化、CNN + BiLSTM。 |

## 英文版本

| Notebook | 作用 |
| --- | --- |
| [`mmlock_c61_paper_reading_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/mmlock_c61_paper_reading_en.ipynb) | 英文论文阅读版本，和中文论文阅读 notebook 对齐。 |
| [`radar_fft_cube_progress_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/radar_fft_cube_progress_en.ipynb) | 英文雷达 FFT 处理流程，代码单元和中文版本对齐。 |
| [`cnn_blstm_pointcloud_training_en.ipynb`](https://github.com/billzi2016/mmlock-fmcw-radar-deep-security/blob/main/cnn_blstm_pointcloud_training_en.ipynb) | 英文点云序列模型流程，代码单元和中文版本对齐。 |

## 推荐阅读路径

1. 先读论文阅读 notebook，知道 mmLock 要解决什么安全问题。
2. 再读 FFT notebook，理解 raw ADC 怎么变成 radar cube 和点云。
3. 最后读模型 notebook，理解点云序列怎么进入 CNN + BiLSTM。

这三类 notebook 是一条链，不是三个孤立示例：论文定义任务，FFT notebook 生成模型输入，训练 notebook 把输入变成离开检测结果。
