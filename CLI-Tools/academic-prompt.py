#!/usr/bin/env python3
"""
academic-prompt CLI 工具
学术 AI Prompt 库的命令行工具
"""

import os
import sys
import json
import argparse
import re
from pathlib import Path
from typing import Dict, List, Optional
import inquirer

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
            "论文撰写系列"
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
                r'###?\s*Prompt\s*([\d.]+)\s*[-–]\s*([^\n]+)\*\*\n使用场景[：:]\s*([^\n]*?)\*\*\s*```([^\n]*?)\n(.*?)```',
                content,
                re.DOTALL
            )

            if not prompt_blocks:
                # 如果没有找到标准格式的 Prompt，尝试另一种格式
                prompt_blocks = re.findall(
                    r'###?\s*Prompt\s*([\d.]+)\s*[-–]\s*([^\n]+)\n\s*\*\*使用场景[：:]\s*([^\n]*?)\*\*\s*```([^\n]*?)\n(.*?)```',
                    content,
                    re.DOTALL
                )

            for idx, (prompt_id, title, usage, lang, prompt_text) in enumerate(prompt_blocks):
                prompt_key = f"{category}_{file_name}_{prompt_id}"
                self.prompts[prompt_key] = {
                    'id': prompt_key,
                    'prompt_id': prompt_id,
                    'title': title.strip(),
                    'category': category,
                    'file': file_name,
                    'usage': usage.strip(),
                    'language': lang.strip() if lang else 'text',
                    'content': prompt_text.strip(),
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
            # 在标题、使用场景、内容中搜索
            if (query in prompt['title'].lower() or
                query in prompt['usage'].lower() or
                query in prompt['content'].lower()):
                results.append(prompt)

        return results

    def get_prompt(self, prompt_key: str) -> Optional[Dict]:
        """获取指定的 Prompt"""
        return self.prompts.get(prompt_key)

    def add_custom_prompt(self, file_path: str):
        """添加自定义 Prompt"""
        custom_dir = self.prompts_dir / "自定义Prompt"
        custom_dir.mkdir(exist_ok=True)

        source_path = Path(file_path)
        if not source_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        # 复制文件到自定义目录
        dest_path = custom_dir / source_path.name
        import shutil
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
        print(f"   使用场景: {prompt['usage']}")
        print(f"   来源: {prompt['file_path']}")
        print(f"{'-' * 100}\n")

def interactive_fill_parameters(prompt_text: str) -> str:
    """交互式填写 Prompt 参数"""
    # 查找所有占位符 [ ]
    placeholders = re.findall(r'\[([^\]]+)\]', prompt_text)

    if not placeholders:
        return prompt_text

    print(f"\n检测到 {len(placeholders)} 个参数需要填写:\n")

    filled_text = prompt_text
    for placeholder in placeholders:
        # 检查这个占位符是否已经被替换
        if f'[{placeholder}]' not in filled_text:
            continue

        print(f"📝 请填写: {placeholder}")
        value = input(f"   > ").strip()

        # 替换所有出现的这个占位符
        filled_text = filled_text.replace(f'[{placeholder}]', value)
        print()

    return filled_text

def export_prompt(prompt: Dict, output_format: str = 'markdown'):
    """导出 Prompt"""
    if output_format == 'markdown':
        content = f"""# {prompt['title']}

**分类**: {prompt['category']}
**使用场景**: {prompt['usage']}

---

{prompt['content']}
"""
    else:  # plain text
        content = prompt['content']

    return content

def main():
    parser = argparse.ArgumentParser(
        description='学术 AI Prompt 库命令行工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  academic-prompt list                    # 列出所有 Prompt
  academic-prompt list -c 论文选题系列  # 列出特定分类的 Prompt
  academic-prompt use <prompt_id>         # 使用指定 Prompt
  academic-prompt search "选题"           # 搜索 Prompt
  academic-prompt add /path/to/prompt.md # 添加自定义 Prompt
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # list 命令
    list_parser = subparsers.add_parser('list', help='列出所有可用的 Prompt 模板')
    list_parser.add_argument('-c', '--category', help='按分类过滤')
    list_parser.add_argument('-j', '--json', action='store_true', help='以 JSON 格式输出')

    # use 命令
    use_parser = subparsers.add_parser('use', help='调用指定 Prompt')
    use_parser.add_argument('prompt_id', help='Prompt ID')
    use_parser.add_argument('-o', '--output', choices=['markdown', 'text', 'json'],
                          default='markdown', help='输出格式')
    use_parser.add_argument('-f', '--file', help='输出到文件')
    use_parser.add_argument('--no-interactive', action='store_true',
                          help='不交互式填写参数，直接输出模板')

    # search 命令
    search_parser = subparsers.add_parser('search', help='搜索相关 Prompt 模板')
    search_parser.add_argument('query', help='搜索关键词')
    search_parser.add_argument('-j', '--json', action='store_true', help='以 JSON 格式输出')

    # add 命令
    add_parser = subparsers.add_parser('add', help='添加自定义 Prompt')
    add_parser.add_argument('file_path', help='Prompt 文件路径')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    # 初始化 Prompt 管理器
    try:
        manager = PromptManager(PROMPTS_DIR)
    except Exception as e:
        print(f"错误: 初始化 Prompt 管理器失败 - {e}")
        return 1

    # 执行命令
    if args.command == 'list':
        prompts = manager.list_prompts(args.category)

        if args.json:
            print(json.dumps(prompts, indent=2, ensure_ascii=False))
        else:
            print_prompt_table(prompts)

    elif args.command == 'use':
        prompt = manager.get_prompt(args.prompt_id)

        if not prompt:
            print(f"错误: 找不到 ID 为 '{args.prompt_id}' 的 Prompt")
            print(f"\n提示: 使用 'academic-prompt list' 查看所有可用的 Prompt")
            return 1

        print(f"\n{'=' * 100}")
        print(f"使用 Prompt: {prompt['title']}")
        print(f"{'=' * 100}\n")

        if not args.no_interactive:
            # 交互式填写参数
            filled_content = interactive_fill_parameters(prompt['content'])
        else:
            filled_content = prompt['content']

        # 导出
        if args.output == 'json':
            output_data = {
                'id': prompt['id'],
                'title': prompt['title'],
                'category': prompt['category'],
                'usage': prompt['usage'],
                'content': filled_content
            }
            output_text = json.dumps(output_data, indent=2, ensure_ascii=False)
        else:
            output_text = export_prompt({
                'title': prompt['title'],
                'category': prompt['category'],
                'usage': prompt['usage'],
                'content': filled_content
            }, args.output)

        # 输出到文件或终端
        if args.file:
            try:
                with open(args.file, 'w', encoding='utf-8') as f:
                    f.write(output_text)
                print(f"✅ 已保存到: {args.file}")
            except Exception as e:
                print(f"错误: 写入文件失败 - {e}")
                return 1
        else:
            print(output_text)
            print(f"\n{'=' * 100}")
            print(f"💡 提示: 复制上方内容到 ChatGPT/Claude 使用")
            print(f"{'=' * 100}\n")

    elif args.command == 'search':
        results = manager.search_prompts(args.query)

        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            print(f"\n搜索关键词: '{args.query}'")
            print(f"{'=' * 100}\n")
            print_prompt_table(results)

    elif args.command == 'add':
        try:
            dest_path = manager.add_custom_prompt(args.file_path)
            print(f"✅ 已添加自定义 Prompt: {dest_path}")
            print(f"💡 使用 'academic-prompt list' 查看新添加的 Prompt")
        except Exception as e:
            print(f"错误: 添加 Prompt 失败 - {e}")
            return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
