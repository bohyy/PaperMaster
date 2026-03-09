#!/usr/bin/env python3
"""
PaperMaster CLI - 学术写作全能助手
"""

import os
import sys
import json
import argparse
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import shutil

# 获取 skill 目录
SCRIPT_DIR = Path(__file__).parent.parent
PROMPTS_DIR = SCRIPT_DIR / "prompts"

class PromptManager:
    """Prompt 管理器"""

    def __init__(self, prompts_dir: Path):
        self.prompts_dir = prompts_dir
        self.prompts: Dict[str, Dict] = {}
        self._load_prompts()

    def _load_prompts(self):
        """加载所有 Prompt 模板"""
        prompt_categories = [
            "论文选题系列",
            "论文查找系列",
            "文献综述系列",
            "论文撰写系列",
            "去AI化润色系列",
            "学术API检索系列",
            "绘图模板系列"
        ]

        for category in prompt_categories:
            category_dir = self.prompts_dir / category
            if not category_dir.exists():
                continue

            for md_file in category_dir.glob("*.md"):
                self._parse_prompt_file(md_file)

    def _parse_prompt_file(self, file_path: Path):
        """解析 Markdown Prompt 文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 提取文件名作为分类
            category = file_path.parent.name
            file_name = file_path.stem

            # 查找所有 Prompt 块
            prompt_blocks = re.findall(
                r'###?\s*Prompt\s*([\d.]+)\s*[-–]\s*([^\n]+)',
                content
            )

            for prompt_id, title in prompt_blocks:
                prompt_key = f"{category}_{file_name}_{prompt_id}"
                self.prompts[prompt_key] = {
                    'id': prompt_key,
                    'prompt_id': prompt_id,
                    'title': title.strip(),
                    'category': category,
                    'file': file_name,
                    'file_path': str(file_path.relative_to(self.prompts_dir))
                }
        except Exception as e:
            print(f"警告: 解析文件 {file_path} 时出错: {e}")

    def list_prompts(self, category: Optional[str] = None) -> List[Dict]:
        """列出所有 Prompt"""
        prompts = list(self.prompts.values())

        if category:
            prompts = [p for p in prompts if p['category'] == category]

        # 按类别和 ID 排序
        prompts.sort(key=lambda x: (x['category'], x['prompt_id']))

        return prompts

    def search_prompts(self, query: str) -> List[Dict]:
        """搜索 Prompt"""
        query = query.lower()
        results = []

        for prompt in self.prompts.values():
            # 在标题、分类中搜索
            if (query in prompt['title'].lower() or
                query in prompt['category'].lower()):
                results.append(prompt)

        return results

    def get_prompt_file(self, prompt_key: str) -> Optional[Path]:
        """获取 Prompt 文件路径"""
        prompt = self.prompts.get(prompt_key)
        if not prompt:
            return None
        return self.prompts_dir / prompt['file_path']

    def add_custom_prompt(self, file_path: str, category: str = "自定义Prompt") -> Path:
        """添加自定义 Prompt"""
        custom_dir = self.prompts_dir / category
        custom_dir.mkdir(exist_ok=True)

        source_path = Path(file_path)
        if not source_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        # 复制文件到自定义目录
        dest_path = custom_dir / source_path.name
        shutil.copy2(source_path, dest_path)

        # 重新加载 Prompt
        self._load_prompts()

        return dest_path


def print_prompt_table(prompts: List[Dict]):
    """打印 Prompt 表格"""
    if not prompts:
        print("没有找到匹配的 Prompt")
        return

    print(f"\n{'=' * 100}")
    print(f"找到 {len(prompts)} 个 Prompt")
    print(f"{'=' * 100}\n")

    for prompt in prompts:
        print(f"📋 ID: {prompt['id']}")
        print(f"   标题: {prompt['title']}")
        print(f"   分类: {prompt['category']}")
        print(f"   来源: {prompt['file_path']}")
        print(f"{'-' * 100}\n")


def print_help_header(title: str, description: str):
    """打印帮助标题"""
    print(f"\n{'=' * 100}")
    print(f"{title}")
    print(f"{'=' * 100}")
    print(f"{description}\n")


def open_file_in_editor(file_path: Path):
    """在默认编辑器中打开文件"""
    try:
        if sys.platform == 'darwin':  # macOS
            subprocess.run(['open', str(file_path)])
        elif sys.platform == 'linux':  # Linux
            subprocess.run(['xdg-open', str(file_path)])
        else:  # Windows
            os.startfile(str(file_path))
        print(f"✅ 已在默认编辑器中打开: {file_path}")
    except Exception as e:
        print(f"⚠️ 无法自动打开文件: {e}")
        print(f"请手动打开: {file_path}")


# ==================== Prompt 命令 ====================

def cmd_prompt_list(args, manager: PromptManager):
    """列出所有 Prompt"""
    prompts = manager.list_prompts(args.category)

    if args.json:
        print(json.dumps(prompts, indent=2, ensure_ascii=False))
    else:
        print_prompt_table(prompts)


def cmd_prompt_use(args, manager: PromptManager):
    """使用指定 Prompt"""
    file_path = manager.get_prompt_file(args.prompt_id)

    if not file_path or not file_path.exists():
        print(f"❌ 错误: 找不到 ID 为 '{args.prompt_id}' 的 Prompt")
        print(f"\n💡 提示: 使用 'papermaster prompt list' 查看所有可用的 Prompt")
        return 1

    print(f"\n{'=' * 100}")
    print(f"📋 Prompt 文件: {file_path.name}")
    print(f"📁 分类: {file_path.parent.name}")
    print(f"{'=' * 100}\n")

    if args.open:
        open_file_in_editor(file_path)
    else:
        # 显示文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print(content)
        print(f"\n{'=' * 100}")
        print(f"💡 提示:")
        print(f"   - 复制上方 Prompt 到 ChatGPT/Claude 使用")
        print(f"   - 使用 'papermaster prompt use {args.prompt_id} --open' 在编辑器中打开")
        print(f"{'=' * 100}\n")

    return 0


def cmd_prompt_search(args, manager: PromptManager):
    """搜索 Prompt"""
    results = manager.search_prompts(args.query)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(f"\n🔍 搜索关键词: '{args.query}'")
        print_prompt_table(results)


def cmd_prompt_add(args, manager: PromptManager):
    """添加自定义 Prompt"""
    try:
        dest_path = manager.add_custom_prompt(args.file_path, args.category)
        print(f"✅ 已添加自定义 Prompt: {dest_path}")
        print(f"💡 使用 'papermaster prompt list' 查看新添加的 Prompt")
    except Exception as e:
        print(f"❌ 错误: 添加 Prompt 失败 - {e}")
        return 1

    return 0


# ==================== Refine (去AI化润色) 命令 ====================

def cmd_refine(args, manager: PromptManager):
    """去AI化润色命令"""
    print_help_header("🎨 PaperMaster 去AI化润色", "核心功能：去除 AI 模板化痕迹，转换为自然学术语气")

    if not args.input_file:
        print("⚠️ 请指定要润色的论文文件")
        print("\n使用示例:")
        print("  papermaster refine paper.md")
        print("  papermaster refine --level medium paper.md")
        print("  papermaster refine --journal Nature paper.md")
        return 1

    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"❌ 文件不存在: {input_path}")
        return 1

    # 确定润色等级
    level = args.level or 'medium'

    # 选择 Prompt
    if args.check_only:
        # 一致性检查
        prompt_key = "去AI化润色系列_文风一致性检查_Prompt1.5"
        print("📋 模式: 文风一致性检查\n")
    elif args.journal:
        # 期刊风格适配
        journal_map = {
            'nature': '去AI化润色系列_期刊风格适配_Prompt2.1',
            'science': '去AI化润色系列_期刊风格适配_Prompt2.2',
            'ieee': '去AI化润色系列_期刊风格适配_Prompt2.3',
            'springer': '去AI化润色系列_期刊风格适配_Prompt2.4'
        }
        prompt_key = journal_map.get(args.journal.lower())
        print(f"📋 模式: 期刊风格适配（{args.journal}）\n")
    else:
        # 标准去AI化润色
        prompt_key = f"去AI化润色系列_去AI化润色核心Prompt_Prompt1.2"  # 使用分层次润色
        print(f"📋 模式: 去AI化润色（等级: {level}）\n")

    # 获取 Prompt 文件
    prompt_file = manager.get_prompt_file(prompt_key)

    if not prompt_file or not prompt_file.exists():
        print(f"❌ 找不到相关 Prompt: {prompt_key}")
        return 1

    print(f"📄 输入文件: {input_path}")
    print(f"📄 Prompt 文件: {prompt_file.name}\n")

    # 读取论文内容
    with open(input_path, 'r', encoding='utf-8') as f:
        paper_content = f.read()

    print(f"📊 论文字数: {len(paper_content)} 字符\n")

    print("💡 使用说明:")
    print("   1. 将 Prompt 文件内容复制到 ChatGPT/Claude")
    print("   2. 将你的论文内容粘贴到 [论文内容] 占位符处")
    print(f"   3. 如果是分层次润色，选择等级: {level}")
    if args.journal:
        print(f"   4. 指定期刊风格: {args.journal}")
    print("   5. AI 返回润色后的文本\n")

    print("🔗 下一步操作:")
    print(f"   - 打开 Prompt 文: papermaster prompt use {prompt_key} --open")
    print(f"   - 打开论文文件: open {input_path}")
    print()

    if args.open:
        open_file_in_editor(prompt_file)

    return 0


# ==================== Figure (学术图表) 命令 ====================

def cmd_figure_list(args, manager: PromptManager):
    """列出所有绘图模板"""
    print_help_header("🎨 PaperMaster 学术图表", "配色方案 + 绘图代码模板 + 期刊规范")

    figures = [
        ("配色方案库", "色盲友好型、Nature、Science、Cell 等期刊配色"),
        ("绘图代码模板", "折线图、柱状图、散点图、热力图、箱线图等"),
        ("期刊绘图规范", "不同期刊的图表要求和规范")
    ]

    print("📋 可用绘图模板:\n")
    for name, desc in figures:
        print(f"   📊 {name}")
        print(f"      {desc}\n")

    print("💡 使用方法:")
    print("   papermaster figure use <模板名> --language <python|r>")
    print("   papermaster figure colors\n")


def cmd_figure_use(args, manager: PromptManager):
    """使用绘图模板"""
    template_map = {
        'colors': '配色方案库',
        'colormap': '配色方案库',
        'lineplot': '绘图代码模板',
        'barplot': '绘图代码模板',
        'scatter': '绘图代码模板',
        'heatmap': '绘图代码模板',
        'boxplot': '绘图代码模板'
    }

    template_name = args.template.lower()
    file_name = template_map.get(template_name, '绘图代码模板')

    prompt_key = f"绘图模板系列_{file_name}"
    prompt_file = manager.get_prompt_file(prompt_key)

    if not prompt_file or not prompt_file.exists():
        print(f"❌ 找不到模板: {args.template}")
        return 1

    print(f"\n📋 绘图模板: {file_name}")
    print(f"💻 语言: {args.language or 'python'}\n")

    if args.open:
        open_file_in_editor(prompt_file)
    else:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 如果指定了语言，尝试提取对应部分
        if args.language:
            lang_section = f"### {args.language.capitalize()} ({'ggplot2' if args.language == 'r' else 'Matplotlib'})"
            if lang_section in content:
                idx = content.find(lang_section)
                if idx != -1:
                    content = content[idx:]

        print(content)
        print(f"\n💡 提示: 复制上方代码到你的项目中\n")

    return 0


def cmd_figure_colors(args, manager: PromptManager):
    """查看配色方案"""
    prompt_key = "绘图模板系列_配色方案库"
    prompt_file = manager.get_prompt_file(prompt_key)

    if prompt_file and prompt_file.exists():
        print_help_header("🎨 配色方案", "色盲友好型 + 期刊推荐配色")
        if args.open:
            open_file_in_editor(prompt_file)
        else:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                print(f.read())
        return 0

    return 1


# ==================== API (学术 API) 命令 ====================

def cmd_api_info(args, manager: PromptManager):
    """显示 API 信息"""
    print_help_header("🔍 PaperMaster 学术 API 多源检索", "5 个免费 API，自动降级切换")

    apis = [
        ("Semantic Scholar", "数据质量最高，推荐论文、引用分析", "100次/分钟"),
        ("OpenAlex", "开放学术图谱，全球最全的学术数据", "基本无限制"),
        ("CORE", "开放获取论文库，优先返回 OA 论文", "10万次/月"),
        ("CrossRef", "DOI 解析权威，元数据最准确", "基本无限制"),
        ("arXiv", "预印本库，最新论文抢先看", "10万次/月")
    ]

    print("📚 支持的学术 API:\n")
    for name, desc, limit in apis:
        print(f"   ✨ {name}")
        print(f"      {desc}")
        print(f"      限额: {limit}\n")

    print("🔄 自动降级切换逻辑:")
    print("   - API 调用失败 → 自动切换到下一个 API")
    print("   - 速率限制 → 自动切换")
    print("   - 额度耗尽 → 自动切换")
    print("   - 超时 → 自动切换")
    print()

    print("💡 使用 Prompt:")
    print("   papermaster prompt use 学术API检索系列_README_Prompt1.1 --open")
    print()


def main():
    parser = argparse.ArgumentParser(
        prog='papermaster',
        description='PaperMaster - 学术写作全能助手',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  papermaster prompt list                    # 列出所有 Prompt
  papermaster prompt use <prompt_id>         # 使用指定 Prompt
  papermaster refine paper.md                 # 去AI化润色
  papermaster refine --journal Nature paper.md # 适配期刊风格
  papermaster figure list                    # 列出绘图模板
  papermaster figure use colors               # 查看配色方案
  papermaster api info                       # 查看 API 信息
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # ==================== Prompt 命令 ====================
    prompt_parser = subparsers.add_parser('prompt', help='Prompt 模板管理')
    prompt_subparsers = prompt_parser.add_subparsers(dest='prompt_cmd', help='Prompt 子命令')

    # prompt list
    list_parser = prompt_subparsers.add_parser('list', help='列出所有 Prompt')
    list_parser.add_argument('-c', '--category', help='按分类过滤')
    list_parser.add_argument('-j', '--json', action='store_true', help='JSON 格式输出')

    # prompt use
    use_parser = prompt_subparsers.add_parser('use', help='使用指定 Prompt')
    use_parser.add_argument('prompt_id', help='Prompt ID')
    use_parser.add_argument('--open', action='store_true', help='在编辑器中打开')

    # prompt search
    search_parser = prompt_subparsers.add_parser('search', help='搜索 Prompt')
    search_parser.add_argument('query', help='搜索关键词')
    search_parser.add_argument('-j', '--json', action='store_true', help='JSON 格式输出')

    # prompt add
    add_parser = prompt_subparsers.add_parser('add', help='添加自定义 Prompt')
    add_parser.add_argument('file_path', help='Prompt 文件路径')
    add_parser.add_argument('-c', '--category', default='自定义Prompt', help='目标分类')

    # ==================== Refine 命令 ====================
    refine_parser = subparsers.add_parser('refine', help='去AI化润色')
    refine_parser.add_argument('input_file', nargs='?', help='论文文件路径')
    refine_parser.add_argument('--level', choices=['light', 'medium', 'heavy'],
                            help='润色等级')
    refine_parser.add_argument('--journal', help='适配期刊风格 (Nature/Science/IEEE/Springer)')
    refine_parser.add_argument('--check-only', action='store_true',
                            help='仅检查文风一致性')
    refine_parser.add_argument('--open', action='store_true',
                            help='打开 Prompt 文件')

    # ==================== Figure 命令 ====================
    figure_parser = subparsers.add_parser('figure', help='学术图表')
    figure_subparsers = figure_parser.add_subparsers(dest='figure_cmd', help='Figure 子命令')

    # figure list
    figure_list_parser = figure_subparsers.add_parser('list', help='列出所有绘图模板')

    # figure use
    figure_use_parser = figure_subparsers.add_parser('use', help='使用绘图模板')
    figure_use_parser.add_argument('template', help='模板名称 (colors/lineplot/barplot/scatter/heatmap/boxplot)')
    figure_use_parser.add_argument('-l', '--language', choices=['python', 'r'],
                                  help='编程语言')
    figure_use_parser.add_argument('--open', action='store_true', help='在编辑器中打开')

    # figure colors
    figure_colors_parser = figure_subparsers.add_parser('colors', help='查看配色方案')
    figure_colors_parser.add_argument('--open', action='store_true', help='在编辑器中打开')

    # ==================== API 命令 ====================
    api_parser = subparsers.add_parser('api', help='学术 API 检索')
    api_subparsers = api_parser.add_subparsers(dest='api_cmd', help='API 子命令')

    # api info
    api_info_parser = api_subparsers.add_parser('info', help='查看 API 信息')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    # 初始化 Prompt 管理器
    try:
        manager = PromptManager(PROMPTS_DIR)
    except Exception as e:
        print(f"❌ 错误: 初始化失败 - {e}")
        return 1

    # 执行命令
    try:
        if args.command == 'prompt':
            if args.prompt_cmd == 'list':
                return cmd_prompt_list(args, manager)
            elif args.prompt_cmd == 'use':
                return cmd_prompt_use(args, manager)
            elif args.prompt_cmd == 'search':
                return cmd_prompt_search(args, manager)
            elif args.prompt_cmd == 'add':
                return cmd_prompt_add(args, manager)
            else:
                prompt_parser.print_help()

        elif args.command == 'refine':
            return cmd_refine(args, manager)

        elif args.command == 'figure':
            if args.figure_cmd == 'list':
                return cmd_figure_list(args, manager)
            elif args.figure_cmd == 'use':
                return cmd_figure_use(args, manager)
            elif args.figure_cmd == 'colors':
                return cmd_figure_colors(args, manager)
            else:
                figure_parser.print_help()

        elif args.command == 'api':
            if args.api_cmd == 'info':
                return cmd_api_info(args, manager)
            else:
                api_parser.print_help()

    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
