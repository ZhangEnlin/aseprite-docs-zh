'''
    递归检查当前文件夹下所有子文件夹中的 *.md 文件，如果有就输出文件名。
'''
import os
from pathlib import Path

def find_md_files():
    """
    递归检查当前文件夹下所有子文件夹中的 *.md 文件
    """
    current_dir = Path.cwd()
    md_files = []
    
    # 遍历当前目录下的所有子目录（不包括当前文件夹本身）
    for item in current_dir.iterdir():
        if item.is_dir():
            # 递归搜索该子文件夹中的所有 .md 文件
            for md_file in item.rglob('*.md'):
                md_files.append(md_file)
    
    # 输出结果到控制台
    if md_files:
        print("找到以下 Markdown 文件：")
        print("-" * 50)
        for file in md_files:
            # 显示相对路径，这样更清晰
            print(f"  {file.relative_to(current_dir)}")
        print("-" * 50)
        print(f"总共找到 {len(md_files)} 个 Markdown 文件")
    else:
        print("未找到任何 Markdown 文件")
    
    return md_files

if __name__ == "__main__":
    find_md_files()