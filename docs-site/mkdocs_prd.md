# mmLock 文档站点 PRD

## 1. 文档目的

本 PRD 用于指导 `mmLock FMCW Radar Deep Security` 项目的 `docs-site/` 文档站点建设。

这个站点不是简单摆放论文和代码说明，而是要把项目讲清楚：先解释雷达是什么，再解释 FMCW 毫米波雷达为什么能做人体感知，接着讲论文里的 mmLock 系统，最后落到 FFT 数据处理、点云生成、Python 模型训练和安全场景。

写作要像认真带读者入门一门技术：不端着，不堆术语，不写空泛宣传，也不要把内容写成求职考核材料。读者可以没有雷达背景，但内容本身必须准确、逐层推进。

## 2. 项目背景

目标项目路径：

```text
/Users/bizi/Desktop/GitHub/old/mmlock-fmcw-radar-deep-security
```

现有材料包括：

- `C61.pdf`：论文原文，题为 `mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging`。
- `mmlock_c61_paper_reading_zh.ipynb`：中文论文阅读笔记。
- `radar_fft_cube_progress_zh.ipynb`：从 raw ADC 数据到 radar FFT cube / 点云的处理流程。
- `cnn_blstm_pointcloud_training_zh.ipynb`：基于点云序列的 CNN + BiLSTM 识别模型流程。
- `radar_fft_cube_progress_parallel/`：面向批量数据的并行 FFT 处理代码。
- `img/pages/`：论文页面截图。
- `img/embedded/`：从论文中抽取出的系统图、流程图、实验图等图片。
- `README_CN.md`：项目中文说明和论文来源说明。

文档站点必须充分利用这些材料，尤其是 notebook 中的处理流程、论文图片和已提取图像资源。不能只写一套空壳页面。

## 3. 建设目标

站点需要完成以下目标：

- 建成一个以中文为主、英文可扩展的 MkDocs 文档站点。
- 用科普式路径讲清楚雷达、FMCW 雷达、毫米波感知和 mmLock 的关系。
- 把论文内容转化为可阅读的系统介绍，而不是只复述摘要。
- 把 FFT、range-Doppler、range-angle、radar cube、点云这些处理步骤讲成连续的数据流。
- 把 Python notebook 中的代码流程整理成文档页面，说明输入、输出、关键函数和中间结果。
- 把 CNN + BiLSTM 模型训练流程讲清楚，包括数据形态、模型输入、时间序列建模和分类目标。
- 把 `img/pages/` 和 `img/embedded/` 中适合展示的图放进对应页面，并配上解释。
- 保留工程可维护性，后续可以继续补充代码复现、实验记录和英文版本。

## 4. 内容风格要求

### 4.1 写作语气

- 使用自然、直接的中文。
- 允许用生活化类比解释概念，但不能牺牲技术准确性。
- 避免“关键、重要、赋能、深入探索、显著提升、体现价值”这类空泛表达。
- 不要使用居高临下的口吻。
- 不要出现与求职筛选、岗位考核无关的场景词汇。
- 不要把文章写成问答背诵材料。
- 不要每段都用“首先、其次、最后”硬凑结构。

### 4.2 教学方式

内容应按“能看懂 -> 知道为什么 -> 知道怎么做”的顺序展开：

1. 先解释直觉：雷达通过发射信号和接收反射信号来感知环境。
2. 再解释机制：FMCW 通过连续扫频，让距离、速度、角度能从频率差和相位差中恢复出来。
3. 再解释数据：ADC 采样、chirp、frame、天线通道、range bin、Doppler bin、angle bin。
4. 再解释算法：FFT 如何把原始时域数据变成可用于感知的频域结构。
5. 再解释系统：mmLock 如何用高质量毫米波成像判断用户是否离开。
6. 最后解释模型：点云序列如何进入 CNN + BiLSTM，模型为什么需要同时看空间形状和时间变化。

### 4.3 读者定位

默认读者具备基本计算机和 Python 阅读能力，但不假设读者学过雷达信号处理。

页面要降低进入门槛，但不要把技术细节删掉。正确做法是把术语拆开解释，并配合图、公式、代码片段和数据流说明。

## 5. 信息架构

站点建议采用以下结构。

```text
docs-site/
├── mkdocs.yml
├── requirements.txt
├── docs/
│   ├── index.md
│   ├── radar-basics.md
│   ├── fmcw-radar.md
│   ├── mmlock-paper.md
│   ├── signal-processing/
│   │   ├── adc-to-cube.md
│   │   ├── fft-pipeline.md
│   │   └── point-cloud.md
│   ├── python-model/
│   │   ├── notebooks.md
│   │   ├── cnn-blstm.md
│   │   └── training-flow.md
│   ├── security-scenario.md
│   ├── figures.md
│   └── project-notes.md
└── overrides/ 或 assets/ 可按需要补充
```

如果后续需要英文版本，可以扩展为 `docs/zh/` 与 `docs/en/`。当前优先把中文内容写扎实，不强行铺空英文页。

## 6. 页面内容要求

### 6.1 首页 `index.md`

首页要回答四件事：

- 这个项目研究什么：用毫米波 FMCW 雷达检测用户离开，服务于数据防盗。
- 为什么用雷达：相比摄像头，毫米波雷达不直接采集可见光图像，能在隐私和感知之间取得不同平衡。
- 站点怎么读：建议从雷达基础、FMCW、论文系统、FFT、点云、模型依次阅读。
- 仓库里有哪些材料：论文、notebook、图片、并行处理代码和模型训练流程。

首页可以放一张论文系统图或代表性成像图，但必须配文字解释图中每个模块的作用。

### 6.2 雷达基础 `radar-basics.md`

该页负责把雷达讲明白：

- 雷达的基本动作：发射电磁波、遇到目标反射、接收回波。
- 距离为什么能测：信号往返需要时间。
- 速度为什么能测：运动目标会带来频率或相位变化。
- 角度为什么能测：多个天线收到信号的相位不同。
- 雷达数据不是照片：它更像由反射强度、距离、速度、角度组成的测量结果。

写法要从直觉出发，再逐步引入术语。不要一开始就堆公式。

### 6.3 FMCW 雷达 `fmcw-radar.md`

该页负责解释 FMCW：

- FMCW 的全称和基本思路：Frequency-Modulated Continuous Wave。
- chirp 是什么：一段频率随时间变化的连续信号。
- beat frequency 是什么：发射信号和接收信号混频后得到的频率差。
- 距离如何从 beat frequency 中恢复。
- 速度如何通过多个 chirp 之间的相位变化估计。
- 多天线如何用于角度估计。
- 为什么毫米波雷达适合近距离人体感知。

可以使用简化公式，但每个公式后必须解释变量含义和它在工程里对应什么数据。

### 6.4 论文解读 `mmlock-paper.md`

该页负责把 `C61.pdf` 和 `mmlock_c61_paper_reading_zh.ipynb` 转成可读文档：

- 论文要解决的问题：用户离开后，终端或办公设备上的敏感数据可能被旁人访问。
- mmLock 的基本思路：通过高质量毫米波雷达成像识别用户离开行为，并触发数据保护。
- 系统流程：雷达采集、成像、人体表示、离开检测、安全动作。
- 论文中的关键图必须进入页面，优先使用 `img/embedded/` 中的系统图、流程图和实验图。
- 每张图下面要写“这张图在说什么”，而不是只写“Figure 1”。
- 论文方法、实验设置、结果和限制要分开写。

注意：不要把论文写成广告。要说明它做了什么、为什么这样做、数据怎么流动、方法有什么边界。

### 6.5 ADC 到 Radar Cube `signal-processing/adc-to-cube.md`

该页负责解释原始数据形态：

- raw ADC 数据是什么。
- sample、chirp、frame、RX/TX channel 分别是什么。
- 为什么原始数据通常是多维数组，而不是一张图。
- radar cube 的维度含义：range、Doppler、angle 或 channel。
- 数据重排、窗口函数、零填充等步骤的作用。

必须参考 `radar_fft_cube_progress_zh.ipynb` 和 `radar_fft_cube_progress_parallel/src/` 中的实现命名，避免写成纯理论页面。

### 6.6 FFT 流程 `signal-processing/fft-pipeline.md`

该页要重点讲 FFT：

- FFT 解决什么问题：把时域采样变成频率分量。
- Range FFT：沿 fast-time 维度处理，用于估计距离。
- Doppler FFT：沿 chirp 维度处理，用于估计速度。
- Angle FFT 或角度估计：利用天线阵列的空间相位差估计方向。
- 为什么需要窗口函数：减少频谱泄漏。
- 为什么需要阈值、CFAR 或峰值检测：从能量图里找出可能的目标点。
- 中间结果应该配图说明，例如 range profile、range-Doppler map、range-angle map 或点云示意。

如果 notebook 中已有可视化结果，应优先转入文档。若还没有图，应在 PRD 中标注需要后续生成。

### 6.7 点云 `signal-processing/point-cloud.md`

该页负责解释点云输出：

- 点云中的一个点代表什么。
- 点的常见字段：x、y、z、range、velocity、intensity、frame id。
- 如何从 radar cube 或检测结果得到点云。
- 点云为什么适合送入后续模型。
- 点云有什么噪声和稀疏性问题。

页面要结合 mmLock 的人体感知场景，不要只写通用点云定义。

### 6.8 Notebook 总览 `python-model/notebooks.md`

该页负责把三个 notebook 的作用讲清楚：

- `mmlock_c61_paper_reading_zh.ipynb`：论文阅读和图文解释。
- `radar_fft_cube_progress_zh.ipynb`：单样本或演示性质的 FFT 处理流程。
- `cnn_blstm_pointcloud_training_zh.ipynb`：点云序列分类模型训练流程。

每个 notebook 需要说明：

- 输入是什么。
- 输出是什么。
- 主要步骤是什么。
- 哪些图或结果应该放入站点。
- 哪些代码适合抽成正式脚本。

### 6.9 CNN + BiLSTM `python-model/cnn-blstm.md`

该页负责解释模型：

- CNN 负责从单帧或局部点云表示里提取空间特征。
- BiLSTM 负责看一段时间内动作如何变化。
- 为什么用户离开检测不是只看某一帧，而要看连续过程。
- 输入张量的形状要写清楚。
- 标签、训练集、验证集、损失函数和评价指标要写清楚。
- 需要说明模型输出如何映射到安全动作。

该页必须来自 `cnn_blstm_pointcloud_training_zh.ipynb` 的实际流程，不要凭空设计一个模型。

### 6.10 训练流程 `python-model/training-flow.md`

该页负责整理训练执行路径：

- 数据准备。
- 点云或特征加载。
- 批处理和序列构造。
- 模型训练。
- 验证与测试。
- 推理输出。
- 后续可复现实验还缺什么。

如果当前仓库材料不足，要明确写“当前材料中未包含完整数据集，因此该页记录的是流程和接口预期”。

### 6.11 安全场景 `security-scenario.md`

该页负责解释为什么这是 security 项目：

- 威胁场景：用户离开设备后，旁人可能接触屏幕或数据。
- mmLock 的角色：检测用户离开状态，辅助触发锁屏或数据保护。
- 传感器边界：雷达负责感知，不负责替代身份认证和权限系统。
- 隐私讨论：毫米波雷达不等于摄像头，但仍然需要谨慎处理感知数据。
- 误报和漏报的影响：安全系统不能只看平均准确率。

语气要务实，避免夸大“绝对安全”。

### 6.12 图片索引 `figures.md`

该页负责管理论文图像资源：

- 列出 `img/pages/` 中的论文页面截图。
- 列出 `img/embedded/` 中适合直接嵌入文档的图。
- 给每张关键图写用途说明。
- 标注建议放入哪个页面。

图片优先引用仓库已有 `img/` 资源，避免在 `docs-site/` 中整批复制二进制图片。若确实需要复制，只复制少量核心图，并保留来源说明。

## 7. 资源处理要求

### 7.1 论文图片

- 优先使用 `img/embedded/` 中已抽取图片。
- 页面级截图 `img/pages/` 可用于论文导读或引用上下文，但不要让整站只堆页面截图。
- 每张图都要有解释文字。
- 图片文件名如果不可读，可以在站点文档中用标题补足含义。

### 7.2 Notebook 内容

- 不要求把 notebook 原样搬进文档。
- 应提炼 notebook 的流程、关键代码片段、输入输出和图。
- 代码片段要短，重点解释数据如何变化。
- 如果 notebook 里有运行结果图，应纳入对应页面。

### 7.3 论文内容

- 可以引用论文题目、作者、会议、 DOI 和公开来源。
- 不要大段复制论文正文。
- 对方法和实验结果应进行中文转述。
- 对不确定或材料不足的地方要写清楚，不要编造数据。

## 8. 技术实现要求

### 8.1 MkDocs

站点使用 `MkDocs`，推荐使用 `mkdocs-material` 主题。

基础配置应包含：

- `site_name`
- `site_description`
- `repo_url`
- `theme`
- `nav`
- `plugins`
- `markdown_extensions`
- `extra_css` 或 `assets` 配置

### 8.2 目录与资源

文档站点相关内容放在 `docs-site/`。

不要把 `img/` 中的论文图整批复制到 `docs-site/`。推荐直接引用仓库已有 `img/embedded/` 的 GitHub raw 链接；如果必须使用站点内部资源，只复制少量核心图，并在 `figures.md` 中记录来源。

### 8.3 双语策略

当前优先完成中文站点。英文可以作为后续扩展，不应为了形式完整创建大量空英文页。

如果实现者决定加入英文版本，应满足：

- 中文内容为主版本。
- 英文页面结构与中文一致。
- 不要机器直译后不校对。
- 英文版本可以滞后，但导航不能指向明显空内容。

## 9. GitHub Actions 要求

站点应提供自动构建与部署能力，具体要求见 `github_action_prd.md`。

MkDocs PRD 中只要求站点结构与内容可被构建，不在这里展开 CI/CD 细节。

## 10. 验收标准

完成后应满足以下条件：

1. `docs-site/` 中存在可构建的 MkDocs 站点。
2. 首页能清楚说明 mmLock 项目、阅读路径和仓库材料。
3. 站点包含雷达基础、FMCW 雷达、论文解读、FFT 流程、点云、Python 模型和安全场景页面。
4. 至少部分论文图被放入对应页面，并配有解释。
5. notebook 的内容被整理成文档流程，而不是只列文件名。
6. FFT 页面能解释 Range FFT、Doppler FFT 和角度估计各自处理哪一维数据。
7. 模型页面能解释 CNN + BiLSTM 的输入、作用和输出。
8. 内容语气自然，不出现空泛宣传和居高临下表达。
9. 不出现与求职筛选、岗位考核无关的场景词汇。
10. 文档中明确当前材料不足或无法复现的部分，不编造实验结果。

## 11. 实施约束

- 不要改动论文 PDF 原文。
- 不要把 notebook 直接删除或替换。
- 不要为了站点好看而篡改论文结论。
- 不要把安全能力写成绝对防护。
- 不要把站点做成只有 README 风格的项目介绍。
- 不要只搭框架不写核心内容。
- 不要在没有依据的情况下补造实验指标、数据集规模或模型性能。
- 不要引入明显增加维护成本的复杂前端框架。

## 12. 对执行者的明确指令

请基于本 PRD，把 `docs-site/` 建设成 mmLock 项目的教学型技术文档站点。

优先级如下：

1. 先写清楚雷达和 FMCW 雷达。
2. 再把论文 mmLock 的系统、动机和方法讲明白。
3. 再整理 FFT 到 radar cube / 点云的数据处理流程。
4. 再整理 Python notebook 和 CNN + BiLSTM 模型。
5. 最后补齐图片索引、项目说明和自动部署。

内容宁可少一点，也要准确、有上下文、有图、有数据流。不要写成空泛项目宣传页。
