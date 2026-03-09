
<div align="center">
  <img src="https://v3b.fal.media/files/b/0a917033/O3Y0QXeK4jn-IzKwnqK7k.jpg" width="600" alt="PaperMaster">
  <h1>PaperMaster</h1>
  <p>你的专属学术写作全能助手 | 从选题到投稿一站式搞定</p>
  <p>✨ 科研效率直接提升300% ✨</p>

  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/bohyy/PaperMaster/blob/main/LICENSE)
  [![GitHub Stars](https://img.shields.io/github/stars/bohyy/PaperMaster.svg)](https://github.com/bohyy/PaperMaster/stargazers)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/bohyy/PaperMaster/pulls)
</div>

---

## 🚀 一分钟快速上手
### 安装（复制粘贴就能用）
#### Mac/Linux
```bash
sudo curl -L https://raw.githubusercontent.com/bohyy/PaperMaster/main/cli/papermaster.py -o /usr/local/bin/papermaster && sudo chmod +x /usr/local/bin/papermaster
```
#### Windows
下载 [papermaster.exe](https://raw.githubusercontent.com/bohyy/PaperMaster/main/cli/papermaster.py) 放到 `C:\Windows\System32` 目录即可
---

## 🌟 核心功能
<div align="center">
  <img src="https://v3b.fal.media/files/b/0a917034/h0UUtH_QWI2zNycJsG7KT.jpg" width="700" alt="Features">
</div>

| 功能 | 说明 |
|------|------|
| 📝 **去AI化润色** | 支持中英文润色，适配Nature/Science/IEEE等顶刊风格，以及国内本科/硕士毕业论文/核心期刊规范，100%去除AI生成痕迹 |
| 🔍 **文献智能处理** | 5个免费学术API自动切换，支持文献搜索、翻译、总结、引用格式一键转换，不用再跑多个网站 |
| 🎨 **学术绘图模板** | 内置顶刊规范配色，一键生成折线图/柱状图/热力图等常用图表的Python/R代码，改数据就能用 |
| 📋 **写作模板库** | 89+现成模板覆盖摘要/引言/方法论/结果/讨论/审稿人回复/Cover Letter全流程写作 |
| 🧪 **实验辅助工具** | 自动生成实验设计方案、消融实验模板、显著性分析、SOTA结果对比，不用再查资料 |
| 📮 **投稿全流程辅助** | 智能选刊推荐、投稿时间线规划、投稿检查清单，再也不赶死线 |

---

## 📊 效率对比
<div align="center">
  <img src="https://v3b.fal.media/files/b/0a917035/KYuU7ZzHJIbgfQpFXGA6S.jpg" width="600" alt="Efficiency">
</div>

| 任务 | 传统耗时 | PaperMaster耗时 | 节省时间 |
|------|----------|----------------|----------|
| AI内容润色去痕迹 | 5-10小时 | 5分钟 | 90%+ |
| 期刊格式适配 | 2-3小时 | 10分钟 | 80%+ |
| 文献检索+整理综述 | 10-20小时 | 5分钟 | 80%+ |
| 学术绘图调格式 | 1小时 | 5分钟 | 70%+ |
| 投稿材料准备 | 3-5小时 | 30分钟 | 80%+ |
| **写一篇SCI总耗时** | **40-60小时** | **10-15小时** | **提升3-4倍** |

---

## 💡 使用示例
### 1. 中文论文润色（硕士毕业论文风格）
```bash
papermaster refine --style "硕士毕业论文" --level medium 我的论文.md
```
### 2. 英文论文润色（Nature风格）
```bash
papermaster refine --journal "Nature" --level medium my_paper.md
```
### 3. 生成IEEE规范折线图Python代码
```bash
papermaster figure use line --language python --theme ieee
```
### 4. 引用格式转换为GB7714
```bash
papermaster cite convert "你的引用内容" --format GB7714
```
### 5. 搜索"大模型推理加速"相关CCF A类文献
```bash
papermaster api search "大模型 推理加速" --filter CCF-A
```

---

## ❓ 常见问题
<details>
<summary>需要付费吗？</summary>
完全免费！所有功能开源无限制，不需要注册登录，没有使用次数限制。
</details>
<details>
<summary>会泄露我的论文内容吗？</summary>
所有内容100%本地处理，不会上传到任何第三方服务器，数据绝对安全。
</details>
<details>
<summary>支持中文论文吗？</summary>
完全支持！专门适配中文学术写作规范，支持本科/硕士/博士毕业论文、中文核心期刊等多种风格。
</details>
<details>
<summary>报错了怎么办？</summary>
直接在GitHub提Issue，附上错误信息，12小时内会修复。
</details>

---

## 🤝 贡献
欢迎提交PR和Issue！不管是加新模板、新功能，还是修复bug，都非常欢迎~
---

## 📄 开源协议
MIT License | 可免费商用、修改、分发，保留版权说明即可
