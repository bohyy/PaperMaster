# PaperMaster - 学术写作全能助手

## 🎯 项目简介

**PaperMaster** 是专为学术研究者设计的一体化智能写作工具，涵盖从论文选题、文献检索、内容写作到图表绘制的全流程。

> **核心理念**：让 AI 成为你的学术助手，而非替代者。提供专业 Prompt 模板、自动去 AI 化润色、学术图表生成等核心功能，显著提升科研效率。

## ✨ 核心功能

### 1️⃣ 学术 Prompt 模板库（89+ 精心设计的 Prompt）

**覆盖全流程**：
- 📌 **论文选题**：生成 100+ 选题候选、5 维度科学评估、深度学术分析
- 🔍 **论文查找**：8 种快速检索方案、AI 直接列举相关论文
- 📚 **文献综述**：智能分类论文、生成综述框架、高效撰写指导
- ✍️ **论文写作**：从创新性评估到结构设计、各部分专业写作
- 🎨 **图表设计**：学术规范图表模板、配色方案、代码生成

**特色**：
- 即复制即用，无需二次加工
- 针对不同期刊风格定制
- 包含最佳实践和常见陷阱

### 2️⃣ ⭐ 去AI化润色（核心功能）

**解决痛点**：AI 生成的学术文本常出现：
- 模板化套话（"在当今时代"、"值得注意的是"等）
- 生硬表述（缺乏自然的学术语气）
- 风格不统一（段落间文风跳跃）
- 期刊不适配（未按目标期刊调整）

**PaperMaster 解决方案**：
- ✅ **智能识别 AI 模板**：自动检测并标记套话
- ✅ **真人学术语气重写**：转换为自然、专业的学术表达
- ✅ **期刊风格适配**：支持 Nature、Science、IEEE、Springer 等主流期刊
- ✅ **分层次润色**：从粗到细，分步优化
- ✅ **一致性检查**：确保全文文风统一

### 3️⃣ 学术图表生成

**提供**：
- 🎨 **配色方案**：色盲友好型、期刊推荐配色
- 📊 **绘图模板**：折线图、柱状图、散点图、热力图、箱线图等
- 💻 **代码生成**：Python (Matplotlib/Seaborn)、R (ggplot2)
- 📏 **规范检查**：字体、字号、线宽、图例位置等符合学术要求

## 🚀 触发场景

当用户以下需求时，使用此 Skill：

### 学术 Prompt 相关
- **论文选题**：「论文选题」、「选题建议」、「帮我选题」、「生成论文题目」
- **文献检索**：「找论文」、「相关论文」、「文献查找」、「帮我找文献」
- **文献综述**：「文献总结」、「文献综述」、「整理文献」、「综述框架」
- **论文写作**：「写论文」、「论文写作」、「学术写作」、「论文各部分」

### 去AI化润色（优先推荐）
- **润色需求**：「润色论文」、「优化论文」、「改进表达」
- **去AI化**：「降低AI率」、「去AI化」、「真人语气」、「自然表达」
- **期刊适配**：「适配期刊」、「Nature风格」、「IEEE风格」
- **一致性**：「统一文风」、「保持一致」

### 图表设计
- **绘图需求**：「论文图表」、「学术图」、「配色方案」、「绘图模板」

## 📖 技能结构

```
PaperMaster/
├── SKILL.md                    (本文件)
├── prompts/                    (Prompt 模板目录)
│   ├── 论文选题系列/
│   │   ├── 论文选题AI提示词库.md
│   │   └── 论文选题论证方案模板.md
│   ├── 论文查找系列/
│   │   ├── 论文查找和文献综述AI提示词库.md
│   │   └── AI直接找论文的Prompt.md
│   ├── 文献综述系列/
│   │   └── 文献综述AI提示词库.md
│   ├── 论文撰写系列/
│   │   └── 顶刊论文写作AI提示词库-2.md
│   ├── 去AI化润色系列/          (⭐ 新增核心模块)
│   │   ├── 去AI化润色核心Prompt.md
│   │   ├── 期刊风格适配.md
│   │   └── 文风一致性检查.md
│   └── 绘图模板系列/            (⭐ 新增模块)
│       ├── 配色方案库.md
│       ├── 绘图代码模板.md
│       └── 期刊绘图规范.md
└── cli/                        (CLI 工具目录)
    └── papermaster              (CLI 可执行文件)
```

## 🎓 使用方法

### 方法一：在 OpenClaw 中直接使用

根据用户需求自动匹配：

**去AI化润色（推荐优先使用）**：
```
场景1：全文润色
- 读取 `prompts/去AI化润色系列/去AI化润色核心Prompt.md`
- 使用 Prompt 1.1（全文去AI化润色）
- 自动识别AI模板、重写为真人语气

场景2：适配期刊风格
- 读取 `prompts/去AI化润色系列/期刊风格适配.md`
- 选择目标期刊（Nature/Science/IEEE等）
- 按期刊规范调整格式、措辞、文风

场景3：一致性检查
- 读取 `prompts/去AI化润色系列/文风一致性检查.md`
- 检查全文风格是否统一
- 提供修改建议
```

**传统学术 Prompt**：
```
论文选题 → prompts/论文选题系列/
论文查找 → prompts/论文查找系列/
文献综述 → prompts/文献综述系列/
论文写作 → prompts/论文撰写系列/
```

**学术图表**：
```
配色方案 → prompts/绘图模板系列/配色方案库.md
绘图代码 → prompts/绘图模板系列/绘图代码模板.md
期刊规范 → prompts/绘图模板系列/期刊绘图规范.md
```

### 方法二：使用 CLI 工具

CLI 工具安装在 `/usr/local/bin/papermaster`，支持以下命令：

```bash
# ==================== Prompt 管理 ====================

# 列出所有可用的 prompt 模板
papermaster prompt list

# 按分类筛选
papermaster prompt list -c 论文选题系列

# 使用指定 prompt（交互式填写参数）
papermaster prompt use <prompt_id>

# 搜索相关 prompt
papermaster prompt search <关键词>

# 添加自定义 prompt
papermaster prompt add <文件路径>

# ==================== 去AI化润色（核心功能）====================

# 全文去AI化润色
papermaster refine <论文文件> [选项]

# 适配期刊风格
papermaster refine --journal Nature <论文文件>
papermaster refine --journal IEEE <论文文件>

# 仅检查一致性
papermaster refine --check-only <论文文件>

# 指定润色等级（light/medium/heavy）
papermaster refine --level heavy <论文文件>

# ==================== 学术图表 ====================

# 列出所有绘图模板
papermaster figure list

# 生成绘图代码
papermaster figure use <模板名> --language python
papermaster figure use <模板名> --language r

# 查看配色方案
papermaster figure colors

# 检查图表规范
papermaster figure check <图表文件>

# ==================== 其他 ====================

# 查看帮助
papermaster --help
papermaster <命令> --help
```

## 🌟 核心亮点

### 去AI化润色模块详解

**为什么需要去AI化？**
- 审稿人能识别出 AI 生成内容，影响评审印象
- AI 模板化语言降低论文可信度
- 不同期刊有不同的风格偏好
- 真人学术语气更具说服力和亲和力

**PaperMaster 的独特之处**：

1. **智能识别 AI 模板库**
   - 内置 500+ 常见 AI 套话模式
   - 自动标记需要修改的句子
   - 区分必要的学术修辞和冗余套话

2. **真人学术语气重写策略**
   - 使用学者常用的自然表达
   - 保持学术严谨性的同时提升可读性
   - 避免过度修辞和冗长句子

3. **期刊风格适配**
   - Nature: 简medi、有力、突出创新
   - Science: 结构清晰、逻辑严密、数据说话
   - IEEE: 技术细节、方法详细、可复现性强
   - Springer: 国际化、标准学术表达

4. **分层次润色**
   - Level 1（Light）：去除明显套话
   - Level 2（Medium）：调整句式、统一文风
   - Level 3（Heavy）：深度改写、适配期刊

### 学术图表模块详解

**配色方案**：
- 色盲友好型配色（Deuteranopia、Protanopia、Tritanopia）
- 期刊推荐配色（Nature、Science、Cell 等）
- 自定义配色库

**绘图模板**：
- 折线图（带误差线、多系列对比）
- 柱状图（分组堆叠、带显著性标记）
- 散点图（带拟合线、置信区间）
- 热力图（相关性矩阵、基因表达）
- 箱线图（统计分布、异常值）

**代码生成**：
- Python: Matplotlib、Seaborn、Plotly
- R: ggplot2
- 支持 Jupyter Notebook 集成

## 📋 使用流程推荐

### 🎯 完整论文写作流程

**阶段 1：选题（3-5 天）**
```bash
1. 使用 Prompt 1.1 生成 100 个选题
   papermaster prompt use 论文选题系列_Prompt1.1

2. 用 5 维度评估表评分

3. 对比分析 Top 选题
   papermaster prompt use 论文选题系列_Prompt3.2

4. 深度分析最佳选题
   papermaster prompt use 论文选题系列_Prompt3.1

5. 准备导师讨论稿
   papermaster prompt use 论文选题系列_Prompt4.2
```

**阶段 2：文献检索（5 分钟）**
```bash
1. AI 直接列举相关论文
   papermaster prompt use 论文查找系列_方案1

2. 在 Google Scholar 验证并下载
```

**阶段 3：文献综述**
```bash
1. 使用文献综述 Prompt
   papermaster prompt use 文献综述系列_相应Prompt

2. 生成综述框架
```

**阶段 4：论文写作（2-3 周）**
```bash
1. 使用写作 Prompt 生成各部分
   papermaster prompt use 论文撰写系列_相应Prompt

2. ⭐ 去AI化润色（关键步骤）
   papermaster refine paper.md --level medium

3. 适配目标期刊
   papermaster refine --journal Nature paper.md

4. 检查文风一致性
   papermaster refine --check-only paper.md
```

**阶段 5：图表设计**
```bash
1. 选择配色方案
   papermaster figure colors

2. 生成绘图代码
   papermaster figure use lineplot --language python

3. 检查图表规范
   papermaster figure check figure.pdf
```

## 💡 最佳实践

### ✅ 推荐做法

1. **先去AI化，再适配期刊**：这样效果更好
2. **分步润色**：不要一次性用 heavy 级别，逐步提升
3. **保留原始版本**：润色前备份，对比效果
4. **结合人工检查**：AI 润色后仍需人工审阅
5. **按期刊规范绘图**：不同期刊有不同要求

### ⚠️ 注意事项

- AI 润色不是万能的，仍需人工审阅
- 期刊风格适配需要明确目标期刊
- 图表规范要仔细检查，避免返工
- 去AI化会改变表达，注意不要丢失原意

## 📊 效果对比

| 任务 | 传统方式 | 使用 PaperMaster | 提升 |
|------|---------|-----------------|------|
| 论文选题 | 2-3 周纠结 | 3-5 天确定 | 节省 2-3 个月 |
| 论文查找 | 10-20 小时 | 5 分钟 | 节省 80% 时间 |
| 文献综述 | 无框架低效 | 有框架高效 | 提速 50% |
| AI 内容润色 | 手工 5-10 小时 | 自动 5 分钟 | 节省 90%+ |
| 期刊适配 | 手工 2-3 小时 | 自动 10 分钟 | 节省 80%+ |
| 图表设计 | 反复调整 | 一次到位 | 节省 70%+ |
| **整体效率** | **40-60 小时** | **10-15 小时** | **提升 3-4 倍** |

## 🔧 技能维护

- 所有 Prompt 模板在 `prompts/` 目录下
- 添加新 Prompt 时遵循现有格式
- 更新去AI化模板库需同步更新索引
- 配色方案和绘图模板可独立扩展

## 📞 技术支持

遇到问题或建议，请：
1. 查看命令帮助：`papermaster --help`
2. 检查 Prompt 模板是否存在
3. 确认文件路径和格式正确

---

**版本**：v3.0 | **名称**：PaperMaster | **定位**：学术写作全能助手 | **核心特色**：去AI化润色 + 学术图表
