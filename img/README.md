# 图片提取说明

本目录保存从 `C61.pdf` 中提取和整理出的论文图片。

## 目录结构

```text
img/
├── embedded/
└── pages/
```

- `embedded/`：使用 `pdfimages` 从 PDF 里直接提取的内嵌图片对象，共 24 个。
- `pages/`：使用 `pdftoppm` 将 10 页 PDF 渲染成整页 PNG，避免遗漏矢量图、组合图或无法直接抽取的图表。
- 中文解读 notebook 优先直接引用 `embedded/` 中的原始图片，并用文字说明无法直接抽取的矢量图、表格和示意图。

## 主要内嵌图

- `pdf_image-002-000.png`：TI IWR6843ISK-ODS 雷达板。
- `pdf_image-002-002.png`：range heatmap 示例。
- `pdf_image-002-003.png`：原始人体点云示例。
- `pdf_image-002-004.png`：点云聚类中的目标用户示例。
- `pdf_image-005-006.png`：静态用户 range heatmap。
- `pdf_image-006-008.png`：攻击者场景中的两个点云 cluster。
- `pdf_image-006-009.png`：实验台和雷达采集设备。
- `pdf_image-007-011.png`、`pdf_image-007-012.png`：PointNet 训练曲线。
- `pdf_image-007-013.png`、`pdf_image-007-014.png`：LSTM 训练曲线。

如果需要回看论文排版上下文，可打开 `pages/` 中对应整页图片。
