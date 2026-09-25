# Math261 数学分析讲义：Obsidian / MyST 版

这是 Math261 数学分析讲义的独立 Markdown 阅读版，共 18 讲。它使用 Obsidian 与 MyST 共同支持的语法，适合在 Obsidian 中阅读，也可以构建为 MyST 网站。

## 在 Obsidian 中阅读

选择 **Open folder as vault** 打开本仓库，然后从 [`index.md`](index.md) 进入。无需安装第三方插件。

- 行内与陈列公式由 Obsidian 自带的 MathJax 渲染。
- 图形是从原始 TikZ/pgfplots 编译而来的自包含矢量 SVG。
- 定义、定理、例题、练习、AI Lab 与 IOU 使用 Obsidian callout 显示。
- 目录链接中的少量数学符号使用 Unicode，因为 Obsidian 不会在链接文字内部排版 MathJax；正文公式仍使用完整 LaTeX 数学。

## 用 MyST 构建

安装 [MyST Markdown](https://mystmd.org/) 后，在仓库根目录运行：

```bash
myst start
```

或者生成 HTML：

```bash
myst build --html
```

## 完整性检查

```bash
python3 tools/validate.py
```

当前版本包含 18 个 Markdown 讲义文件和 79 幅 SVG 图。详细验证结果见 [`VALIDATION.md`](VALIDATION.md)。

LaTeX 正式源文件与项目记录保存在主项目 [`dazhima/math-teaching`](https://github.com/dazhima/math-teaching)；本仓库用于发布可直接阅读的 Markdown 版本。

## 第三讲修订版（2026-09-25）

第三讲已完成中文例题、习题及提示，新增调和和的面积解释、欧拉常数误差修正与配图，删除 AI Lab。 [下载第三讲 PDF](pdf/L03.pdf)。

L03 是经人工审阅的 Markdown 修订稿，已同步回 LaTeX；不要用旧的整套转换器覆盖它。其他讲仍沿用原转换流程。

