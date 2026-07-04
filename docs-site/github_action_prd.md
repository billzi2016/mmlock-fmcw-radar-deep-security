# mmLock 文档站点 GitHub Actions PRD

## 1. 文档目的

本 PRD 用于定义 `mmLock FMCW Radar Deep Security` 项目文档站点的自动构建与部署要求。

目标是让 `docs-site/` 中的 MkDocs 站点可以稳定构建，并部署到 GitHub Pages。自动化流程只服务文档站点，不承担模型训练、notebook 执行、论文处理或数据生成任务。

## 2. 适用范围

本 PRD 适用于以下内容：

- `docs-site/` 下的 MkDocs 文档站点构建。
- 文档依赖安装。
- 文档资源检查。
- 静态站点产物上传。
- GitHub Pages 部署。

本 PRD 不要求自动运行以下任务：

- 执行 `radar_fft_cube_progress_zh.ipynb`。
- 执行 `cnn_blstm_pointcloud_training_zh.ipynb`。
- 重新训练 CNN + BiLSTM 模型。
- 重新从 PDF 中抽取图片。
- 处理大规模 radar raw ADC 数据。
- 运行 `radar_fft_cube_progress_parallel/` 批处理流程。

这些任务可能依赖数据集、GPU、较长运行时间或本地环境，不适合塞进文档部署工作流。

## 3. 建设目标

需要提供一套 GitHub Actions 工作流，满足以下目标：

- 当文档相关文件变化时自动构建站点。
- 支持手动触发构建和部署。
- 使用稳定的 Python 环境安装 MkDocs 依赖。
- 在 `docs-site/` 目录中执行构建。
- 构建失败时明确暴露 Markdown、导航、资源路径或依赖问题。
- 将生成的静态站点部署到 GitHub Pages。
- 工作流保持简单，方便后续维护。

## 4. 工作流文件要求

建议工作流文件放置在：

```text
.github/workflows/docs.yml
```

工作流名称建议为：

```yaml
name: Deploy docs site
```

如果项目中已有其他 CI 文件，不应把文档部署逻辑混入模型训练、数据处理或代码测试流程。

## 5. 触发策略

### 5.1 自动触发

工作流应在主分支文档相关内容变化时触发。

推荐触发范围：

```yaml
on:
  push:
    branches:
      - main
    paths:
      - "docs-site/**"
      - "img/**"
      - "README_CN.md"
      - ".github/workflows/docs.yml"
  workflow_dispatch:
```

说明：

- `docs-site/**` 是文档站点主体。
- `img/**` 包含论文页面图和 embedded 图，站点可能引用这些资源。
- `README_CN.md` 可能作为项目说明来源。
- 工作流自身变化也应触发验证。

如果仓库默认分支不是 `main`，实现时应改成实际默认分支。

### 5.2 手动触发

必须保留 `workflow_dispatch`，用于手动补发部署或验证构建问题。

### 5.3 并发控制

建议添加并发控制，避免多次 push 导致部署互相覆盖：

```yaml
concurrency:
  group: pages
  cancel-in-progress: false
```

`cancel-in-progress` 可根据团队习惯调整。文档部署通常不需要并发执行。

## 6. 权限要求

GitHub Pages 部署建议使用 GitHub 官方 Pages 工作流权限：

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

不要授予与文档部署无关的高权限，例如写 issue、写 pull request、管理 package 等。

## 7. 构建环境

### 7.1 Python 版本

建议使用稳定 Python 版本，例如：

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: "3.11"
```

不要求和 notebook 训练环境完全一致。文档构建只需要 MkDocs 及其插件。

### 7.2 依赖安装

文档依赖应由 `docs-site/requirements.txt` 管理。

建议至少包含：

```text
mkdocs
mkdocs-material
```

如果使用 i18n、图片插件、notebook 渲染插件或其他 Markdown 扩展，应写入同一个依赖文件。

工作流中安装方式建议为：

```yaml
- name: Install docs dependencies
  working-directory: docs-site
  run: pip install -r requirements.txt
```

不应依赖 GitHub runner 里预装的隐式包。

## 8. 构建要求

### 8.1 构建命令

构建应在 `docs-site/` 目录执行：

```yaml
- name: Build docs
  working-directory: docs-site
  run: mkdocs build --strict
```

使用 `--strict` 的原因是尽早发现：

- 导航指向不存在的 Markdown 文件。
- 图片路径错误。
- 页面链接错误。
- Markdown 语法或插件配置问题。

如果当前站点早期建设阶段存在大量临时链接，可以暂时不用 `--strict`，但 PRD 目标应是最终启用严格构建。

### 8.2 图片资源

站点会使用论文图和 notebook 相关图。工作流不负责生成图片，但必须能检查引用是否有效。

实现时应选择一种稳定策略：

- 直接引用仓库已有 `img/embedded/` 的 GitHub raw 链接，避免二进制图片重复入库。
- 或只复制少量核心图到 `docs-site/docs/assets/`，文档只引用这些精选资源。

推荐第一种策略。它不会让同一批论文图在仓库里保存两份。

### 8.3 Notebook 处理

工作流不应默认执行 notebook。原因：

- notebook 可能依赖本地数据。
- radar FFT 处理可能耗时较长。
- 模型训练可能依赖 GPU 或较大数据集。
- 自动部署文档不应该因为训练环境缺失而失败。

如果站点要展示 notebook 内容，应优先将关键解释、代码片段和图片整理成 Markdown。需要自动转换 notebook 时，应单独设计轻量检查流程，不与部署强绑定。

## 9. GitHub Pages 部署

推荐使用 GitHub 官方 Pages Actions：

```yaml
- name: Setup Pages
  uses: actions/configure-pages@v5

- name: Upload artifact
  uses: actions/upload-pages-artifact@v3
  with:
    path: docs-site/site

- name: Deploy to GitHub Pages
  id: deployment
  uses: actions/deploy-pages@v4
```

部署 job 应声明：

```yaml
environment:
  name: github-pages
  url: ${{ steps.deployment.outputs.page_url }}
```

## 10. 推荐工作流结构

推荐使用一个 job 完成构建和部署：

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install docs dependencies
        working-directory: docs-site
        run: pip install -r requirements.txt

      - name: Build docs
        working-directory: docs-site
        run: mkdocs build --strict

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: docs-site/site

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

如果后续需要把 build 和 deploy 拆成两个 job，也可以，但不要为了形式复杂化。

## 11. 质量要求

### 11.1 可读性

- Step 名称要直接说明动作。
- 不要写大段难维护的 shell 脚本。
- 不要把部署路径藏在复杂变量里。
- 如果使用环境变量，必须有明确用途。

### 11.2 可维护性

- 文档依赖集中在 `docs-site/requirements.txt`。
- MkDocs 配置集中在 `docs-site/mkdocs.yml`。
- 站点页面集中在 `docs-site/docs/`。
- 工作流只调用这些稳定入口。

### 11.3 可靠性

- 构建失败应直接失败，不要用 `|| true` 忽略错误。
- 不要在部署前执行会修改仓库内容的命令。
- 不要在 CI 中自动提交生成文件。
- 不要在 CI 中运行大规模数据处理。

## 12. 验收标准

完成后应满足以下条件：

1. 仓库中存在 `.github/workflows/docs.yml`。
2. 工作流支持 `push` 和 `workflow_dispatch`。
3. `push` 触发范围限制在文档、图片、README 或工作流相关文件。
4. 工作流使用 Python 安装 `docs-site/requirements.txt` 中的依赖。
5. 工作流在 `docs-site/` 中执行 `mkdocs build`。
6. 构建产物来自 `docs-site/site`。
7. 工作流使用 GitHub Pages 官方部署 Action 或同等稳定方案。
8. 工作流权限遵循最小必要原则。
9. 工作流不执行 notebook、模型训练或大规模雷达数据处理。
10. 构建失败时能暴露错误，而不是静默跳过。

## 13. 实施约束

- 不要把 notebook 执行放进默认部署链路。
- 不要把模型训练放进文档部署链路。
- 不要在工作流中生成、覆盖或提交项目文件。
- 不要对所有代码变更都触发文档部署。
- 不要依赖本地绝对路径。
- 不要使用过时或不维护的 Action。
- 不要把 GitHub token 打印到日志里。

## 14. 对执行者的明确指令

请基于本 PRD 为 mmLock 文档站点实现 GitHub Actions 自动部署。

实现时先保证一件事：`docs-site/` 能稳定构建并部署。论文图片、notebook 结果和模型说明应该作为文档内容被引用，而不是在 CI 里临时生成。

如果构建因图片路径或 notebook 资源缺失失败，应优先修正文档资源组织方式，而不是放宽 CI 到忽略错误。
