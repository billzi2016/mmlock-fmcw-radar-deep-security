# mmLock FMCW Radar Deep Security

## 项目简介

mmLock FMCW Radar Deep Security 是一个面向设备安全场景的毫米波雷达感知项目，围绕用户离开检测、数据防盗保护和高质量 mmWave radar imaging 展开。项目基于公开论文材料整理，突出 FMCW radar sensing、deep learning 建模和 security 防护三个核心方向。

**技术标签**：`fmcw` · `deeplearning` · `security` · `mmwave-radar` · `point-cloud`

## 文档站点

GitHub Pages：https://billzi2016.github.io/mmlock-fmcw-radar-deep-security/

文档站点位于 `docs-site/`，按从浅到深的路径组织：先讲无线感知、雷达基础和 FMCW 雷达，再讲 mmLock 论文系统，随后解释 FFT 处理、点云生成、Python notebook 和 CNN + BiLSTM 模型流程。无线感知部分会把 WiFi CSI 和 FMCW 雷达的相似点、差异和工程取舍讲清楚。

## 论文

- 仓库 PDF：[`C61.pdf`](C61.pdf)
- 论文标题：mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging
- 作者：Jiawei Xu, Ziqian Bi, Amit Singha, Tao Li, Yimin Chen, Yanchao Zhang
- 会议：2023 32nd International Conference on Computer Communications and Networks (ICCCN)
- DOI：https://doi.org/10.1109/ICCCN58024.2023.10230151
- ASU 论文记录：https://asu.elsevierpure.com/en/publications/mmlock-user-leaving-detection-against-data-theft-via-high-quality/
- 公开 PDF 来源：[ASU CNSG 公开 PDF](https://labs.engineering.asu.edu/cnsg/wp-content/uploads/sites/147/2024/02/C61.pdf)

## Notebook

| Notebook | 用途 |
| --- | --- |
| [`mmlock_c61_paper_reading_zh.ipynb`](mmlock_c61_paper_reading_zh.ipynb) | mmLock 中文论文阅读笔记，覆盖系统流程、威胁模型、FFT、点云生成、PointNet/LSTM 思路和实验解读。 |
| [`radar_fft_cube_progress.ipynb`](radar_fft_cube_progress.ipynb) | 雷达信号处理流程 notebook，从 DCA1000 raw ADC bin 到 TDM-MIMO frame cube、Range/Doppler/Angle FFT 和点检测。 |
| [`cnn_blstm_pointcloud_training.ipynb`](cnn_blstm_pointcloud_training.ipynb) | 点云序列建模 notebook，用于准备 radar point sequence，并训练 CNN + BiLSTM 分类器。 |

## 项目目标

- 整理 mmLock 论文及相关项目材料，形成可展示、可维护的 FMCW radar security 项目仓库。
- 突出毫米波 FMCW 雷达在安全感知中的工程价值。
- 保留后续扩展空间，便于补充代码复现、模型结构说明、数据处理流程和实验记录。

## 核心功能

- 用户离开检测：利用毫米波雷达感知用户离开行为，为自动锁屏和数据防护提供触发依据。
- 高质量雷达成像：围绕 mmWave radar imaging 和三维人体点云/网格表达组织项目内容。
- 深度学习识别：将深度学习模型用于雷达感知数据的行为识别与安全判断。
- 安全场景落地：服务于终端设备、办公设备和智能空间中的数据防盗保护需求。

## 技术栈

- FMCW mmWave radar sensing
- Radar imaging and point-cloud processing
- Deep learning for behavior recognition
- Security-oriented user presence detection

## 项目结构

```text
mmlock-fmcw-radar-deep-security/
├── C61.pdf
├── citation.bib
├── cnn_blstm_pointcloud_training.ipynb
├── docs-site/
│   ├── docs/
│   ├── mkdocs.yml
│   └── requirements.txt
├── img/
│   ├── embedded/
│   └── pages/
├── mmlock_c61_paper_reading_zh.ipynb
├── radar_fft_cube_progress.ipynb
├── radar_fft_cube_progress_parallel/
│   ├── README.md
│   ├── run_parallel_fft.py
│   └── src/
├── README.md
└── .gitignore
```

## 运行方式

当前仓库以论文材料归档和项目说明为主，暂未包含可运行代码。后续如补充代码，可在 README 中继续完善环境配置、数据准备、训练流程和复现实验说明。

## 当前进度

- 已整理论文 PDF。
- 已建立独立项目目录。
- 已补充项目说明、技术标签和来源说明。
- 已在 `docs-site/` 补充 GitHub Pages 文档站点。
- 已补充 raw ADC bin 到 radar FFT cube/点云的 notebook 流程。
- 已补充面向大规模样本的多进程并行处理框架。
- 已提取论文图片到 `img/`，并补充中文逐段解读 notebook。
- 已补充基于并行 FFT 点云输出格式的 CNN + BiLSTM 识别 notebook。

## 后续计划

- 补充系统架构图与数据流说明。
- 整理 FMCW 雷达数据处理流程。
- 补充 deep learning 模型结构与训练/推理流程。
- 增加 security 场景说明、威胁模型和适用边界。
- 如代码开放，补充安装、运行和实验复现文档。

## 论文来源与版权说明

论文文件：[`C61.pdf`](C61.pdf)

论文标题：mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging

作者：Jiawei Xu, Ziqian Bi, Amit Singha, Tao Li, Yimin Chen, Yanchao Zhang

会议：2023 32nd International Conference on Computer Communications and Networks (ICCCN), 2023

Google Scholar 条目可按如下形式识别：

```text
mmLock: User leaving detection against data theft via high-quality mmWave radar imaging
J Xu, Z Bi, A Singha, T Li, Y Chen, Y Zhang
2023 32nd International Conference on Computer Communications and Networks ..., 2023
```

BibTeX：

```bibtex
@inproceedings{xu2023mmlock,
  title={mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging},
  author={Xu, Jiawei and Bi, Ziqian and Singha, Amit and Li, Tao and Chen, Yimin and Zhang, Yanchao},
  booktitle={2023 32nd International Conference on Computer Communications and Networks (ICCCN)},
  pages={1--10},
  year={2023},
  organization={IEEE},
  doi={10.1109/ICCCN58024.2023.10230151},
  url={https://doi.org/10.1109/ICCCN58024.2023.10230151}
}
```

ASU 论文记录：https://asu.elsevierpure.com/en/publications/mmlock-user-leaving-detection-against-data-theft-via-high-quality/

公开来源：[ASU CNSG 公开 PDF](https://labs.engineering.asu.edu/cnsg/wp-content/uploads/sites/147/2024/02/C61.pdf)

DOI：https://doi.org/10.1109/ICCCN58024.2023.10230151

本仓库中的论文 PDF 是作者自有论文材料，用于项目材料归档、工程说明和学术展示。ASU CNSG 网站提供了公开 PDF 链接，ASU 官方论文记录中也收录了该论文及 DOI 信息。

对于 NSF 支持产生的同行评议论文或正式会议论文，NSF Public Access Policy 要求相关论文版本进入 NSF 指定的公开访问仓储并在规定时间内可公开访问。该仓库保留 ASU 公开来源、ASU 论文记录和 DOI，便于追溯正式出版信息与公开访问来源。

论文版权、出版版本和再分发权限仍以 IEEE、作者出版协议、ASU 公开页面及 NSF public access 相关政策为准；引用、传播或再分发时应优先使用正式出版信息和上述公开来源链接。
