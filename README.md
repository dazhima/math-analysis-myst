# Math261 数学分析讲义：Obsidian / MyST 阅读版

本仓库提供数学分析讲义的 Markdown 阅读版。**第 1–8 讲是当前修订稿；第 9–18 讲保留为历史稿，尚未按新课程设计重写。** 请从 [目录](index.md) 进入。

在 Obsidian 中使用 **Open folder as vault** 打开本仓库即可阅读。公式用内置 MathJax 排版，图形使用自包含 SVG；不需要第三方插件。第 1–8 讲对应的 PDF 在 [`pdf/`](pdf/) 中。另有 [有理逼近扩展阅读](supplements/rational-approximation.md)，连接第 1、3 讲与 Dirichlet、连分数和 Roth 定理。

MyST 用户可在仓库根目录运行 `myst start` 预览，或运行 `myst build --html` 构建网站。离线完整性检查：

```bash
python3 tools/validate.py
```

讲义的 LaTeX 源码及项目记录保存在主项目 [`dazhima/math-teaching`](https://github.com/dazhima/math-teaching)。第 1–8 讲 Markdown 经人工修改；不要用旧的整套转换器覆盖它们。本仓库不包含教材扫描件或项目内部审查材料。
