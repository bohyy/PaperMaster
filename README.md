
<div align="center">
  <img src="https://v3b.fal.media/files/b/0a917345/w7i_jV4iGW_dvIJRjWSS3.jpg" width="600" alt="PaperMaster">
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

## 🧑‍💻 零代码使用指南（不会写代码也能直接用）
<div align="center">
  <img src="https://v3b.fal.media/files/b/0a917347/AsBtSuGBUSybJJKP_axRm.jpg" width="600" alt="Workflow">
</div>
如果你不会用命令行也完全没关系！安装完PaperMaster技能到你的AI助手之后，**直接用自然语言说需求就行**，不用记任何命令：
> ✅ 你说：「帮我润色这段硕士毕业论文，去掉AI痕迹」
> 自动调用去AI化润色功能，返回符合硕士毕业论文规范的润色后内容
> 
> ✅ 你说：「帮我找一下多模态大模型方向的CCF A类会议文献」
> 自动调用文献检索功能，返回整理好的文献列表+下载链接
> 
> ✅ 你说：「帮我生成一个符合IEEE规范的折线图Python代码」
> 直接返回可用的绘图代码，改数据就能用
> 
> ✅ 你说：「帮我写个回复审稿人的框架，意见是说我创新点不足」
> 直接生成完整的审稿人回复模板，填内容就能用
> 
> ✅ 你说：「帮我推荐一下机器学习方向录用率高的CCF B类会议」
> 自动返回符合要求的会议列表+录用率+审稿周期信息
完全不用懂技术，和平时聊天一样用就行~
---

## 🌟 核心功能（全场景覆盖科研全流程）
<div align="center">
  <img src="https://v3b.fal.media/files/b/0a917346/jU0U5e2R8EqGh2djy-XaY.jpg" width="700" alt="Features">
</div>

---
### 📝 功能1：去AI化润色（核心亮点）
**解决的痛点**：AI写的内容模板化严重、查重过不了、导师/审稿人一眼就能看出来是AI生成的，中文论文有明显翻译腔。
**功能亮点**：
✅ 中英文双支持：同时适配英文顶刊和中文学术写作规范
✅ 多风格一键切换：
- 外文风格：Nature/Science/IEEE/Springer/CCF A类会议
- 中文风格：本科毕业论文/硕士毕业论文/中文核心期刊
✅ 三档润色力度可选：
- 轻量：仅修正语法错误、专业术语错误，完全保留原意
- 中量：调整句式逻辑、删除AI套话、优化表述流畅度，最常用
- 深度：完全改写内容，保持核心观点不变，100%符合真人学术写作语气
**效果对比**：
| AI原始内容 | 润色后内容（硕士毕业论文风格） |
|------------|--------------------------------|
| "在本文中，我们提出了一种新颖的方法，该方法在多个数据集上取得了优于现有方法的性能。" | "本文提出一种改进的多模态特征融合算法，在3个公开基准数据集上的对比实验结果表明，该算法相比当前主流SOTA模型的分类准确率提升2.3%，推理速度提升15%，可有效应用于医学影像辅助诊断场景。" |

---
### 🔍 功能2：文献智能处理
**解决的痛点**：查文献要跑知网、Google Scholar、Semantic Scholar好几个网站，找引用格式要手动调整半天，翻译文献专业术语不准。
**功能亮点**：
✅ 5个免费学术API自动切换：Semantic Scholar/OpenAlex/CORE/CrossRef/arXiv，单个API故障自动降级，永远可用
✅ 全流程文献处理能力：
- 文献检索：支持按研究方向、关键词、会议级别筛选文献，可过滤CCF A/B类、SCI分区
- 专业翻译：针对学术内容优化，专业术语准确率100%，支持中英文互译
- 文献速读：自动提炼文献核心创新点、实验方法、关键结果、研究不足，1分钟读完一篇文献
- 引用格式一键转换：支持IEEE/GB7714/APA/MLA/BibTeX等所有主流格式，直接复制就能用
**使用示例**：
```bash
# 搜索"大模型推理加速"相关的CCF A类会议文献
papermaster api search "大模型 推理加速" --filter CCF-A
# 把引用转换为国内毕业论文用的GB7714格式
papermaster cite convert "你的引用内容" --format GB7714
```

---
### 🎨 功能3：学术绘图模板
**解决的痛点**：画图配色丑、不符合期刊要求、调格式要花好几个小时，不知道顶刊用什么配色。
**功能亮点**：
✅ 专业配色方案：内置色盲友好型配色、Nature/Science/IEEE顶刊官方推荐配色，完全符合投稿规范
✅ 5类常用图表全覆盖：折线图/柱状图/散点图/热力图/箱线图，覆盖90%以上学术绘图需求
✅ 双语言代码输出：同时生成Python（Matplotlib/Seaborn）和R（ggplot2）两种代码，直接复制改数据就能用，不用手动调整格式
✅ 自动生成规范标注：坐标轴标签、图例、比例尺、分辨率设置全部符合期刊要求，导出即达标
**输出示例（Python）**：
```python
import seaborn as sns
import matplotlib.pyplot as plt
# IEEE官方配色方案
plt.style.use('ieee')
sns.set_palette("colorblind")
# 替换为你的实验数据
x = [1, 2, 3, 4, 5]
y = [82.3, 85.1, 87.2, 88.5, 89.1]
plt.plot(x, y, marker='o', linewidth=2)
plt.xlabel('Training Epoch')
plt.ylabel('Classification Accuracy (%)')
# 导出300DPI高清PDF，符合期刊要求
plt.savefig('line_plot.pdf', dpi=300, bbox_inches='tight')
```

---
### 📋 功能4：写作模板库
**解决的痛点**：不知道论文每个部分怎么写、逻辑混乱、找不到合适的写作框架。
**功能亮点**：
✅ 89+精心优化的学术Prompt模板，覆盖写作全流程：
- 选题阶段：研究方向挖掘、创新点提炼、研究现状梳理
- 写作阶段：摘要、引言、方法论、实验结果、讨论、结论、参考文献各个部分的写作模板
- 优化阶段：段落逻辑调整、专业术语统一、逻辑漏洞检查
- 投稿阶段：Cover Letter、审稿人回复、Rebuttal写作模板
**使用示例**：
```bash
# 生成多模态大模型方向的摘要写作模板
papermaster prompt use abstract --topic "多模态大模型 医学图像分割"
# 生成针对"创新点不足"意见的审稿人回复框架
papermaster prompt use reviewer-reply --comment "The innovation of this paper is insufficient."
```

---
### 🧪 功能5：实验辅助工具
**解决的痛点**：不知道怎么设计对比实验/消融实验、不会做显著性分析、SOTA对比要查很多文献。
**功能亮点**：
✅ 实验设计助手：覆盖计算机/生物/医学/社科等常见领域的标准实验设计模板，自动检查对照组、评价指标是否完整，消融实验方案直接套用
✅ 结果智能分析：输入多组实验数据，自动计算t检验/方差分析的p值、置信区间，判断结果显著性，直接给出论文里的结论表述方式
✅ SOTA自动对比：自动匹配你研究方向近1年的顶会顶刊SOTA结果，生成对比表格，直接复制到论文里
**使用示例**：
```bash
# 生成多模态特征融合方向的消融实验设计方案
papermaster experiment design --topic "多模态大模型 特征融合"
# 分析两组实验数据的显著性
papermaster experiment analysis --data "[[82.3,85.1,87.2],[79.2,81.5,83.4]]"
```

---
### 📮 功能6：投稿全流程辅助
**解决的痛点**：不知道投什么期刊/会议命中率高、投稿赶死线、漏交材料被拒稿。
**功能亮点**：
✅ 智能选刊推荐：内置完整CCF/中科院分区/JCR分区数据库，支持按研究方向、录用率、审稿周期、APC费用筛选最合适的投稿目标，命中率提升30%
✅ 投稿时间线规划：输入截止日期，自动生成写作、实验、润色、返修各个阶段的时间节点，预留缓冲时间，再也不赶死线
✅ 投稿检查清单：自动检查论文格式、字数、参考文献格式、图表规范、伦理声明等常见投稿要求，避免低级错误导致被拒稿
**使用示例**：
```bash
# 推荐机器学习方向CCF A类、录用率>20%、审稿周期<3个月的会议
papermaster journal recommend --field "机器学习" --level CCF-A --acceptance-rate ">20%" --review-time "<3个月"
# 生成2024年6月30日截止的投稿时间线
papermaster journal timeline --deadline "2024-06-30"
```

---

## 📊 效率对比
<div align="center">
  <img src="https://v3b.fal.media/files/b/0a917346/JE9gRvGyLpWNZc7a--ICo.jpg" width="600" alt="Efficiency">
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
