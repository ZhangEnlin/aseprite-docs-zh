'''
    图片链接如果以当前文件夹为根目录的话，则在 `src` 前方加上 `./` 以明确表示当前文件夹。
'''
import os
import re
from pathlib import Path

def fix_image_paths_in_md():
    """
    递归检查当前文件夹内所有 .md 文件，
    修复不以 . / \ 开头的图片路径，在前面加上 ./
    """
    current_dir = Path.cwd()
    md_files = list(current_dir.rglob('*.md'))
    
    if not md_files:
        print("当前目录下未找到任何 Markdown 文件")
        return
    
    print(f"找到 {len(md_files)} 个 Markdown 文件，开始处理...")
    print("-" * 50)
    
    total_fixed = 0
    files_modified = 0
    
    for md_file in md_files:
        fixed_count = process_md_file(md_file, current_dir)
        if fixed_count > 0:
            total_fixed += fixed_count
            files_modified += 1
    
    print("-" * 50)
    print(f"处理完成！共修改 {files_modified} 个文件，修复 {total_fixed} 处图片路径")
    
    return total_fixed

def process_md_file(file_path, current_dir):
    """
    处理单个 Markdown 文件，修复图片路径
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixed_count = 0
        
        # 修复 Markdown 图片语法：![alt](path)
        # 匹配 ![任意文本](路径)
        content, count1 = fix_markdown_image_syntax(content)
        fixed_count += count1
        
        # 修复 HTML img 标签：<img src="path" />
        # 匹配 src="路径"
        content, count2 = fix_html_image_syntax(content)
        fixed_count += count2
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            relative_path = file_path.relative_to(current_dir)
            print(f"✓ {relative_path} - 修复了 {fixed_count} 处图片路径")
            return fixed_count
        
        return 0
        
    except Exception as e:
        relative_path = file_path.relative_to(current_dir)
        print(f"✗ 处理文件 {relative_path} 时出错: {e}")
        return 0

def fix_markdown_image_syntax(content):
    """
    修复 Markdown 语法的图片路径
    匹配 ![任意内容](路径)
    """
    fixed_count = 0
    
    # 正则表达式匹配 Markdown 图片语法
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    def replace_markdown_path(match):
        nonlocal fixed_count
        alt_text = match.group(1)  # 图片描述文本
        img_path = match.group(2).strip()  # 图片路径
        
        # 检查路径是否需要修复
        if needs_fix(img_path):
            fixed_path = './' + img_path
            fixed_count += 1
            return f'![{alt_text}]({fixed_path})'
        
        return match.group(0)
    
    new_content = re.sub(pattern, replace_markdown_path, content)
    return new_content, fixed_count

def fix_html_image_syntax(content):
    """
    修复 HTML img 标签的图片路径
    匹配 src="路径" 或 src='路径'
    """
    fixed_count = 0
    
    # 匹配 <img 标签中的 src 属性
    # 支持单引号和双引号
    pattern = r'(<img[^>]*?\s+src=)("|\')([^"\']+)\2'
    
    def replace_html_path(match):
        nonlocal fixed_count
        prefix = match.group(1)  # <img ... src=
        quote = match.group(2)   # 引号类型 " 或 '
        img_path = match.group(3).strip()  # 图片路径
        
        # 检查路径是否需要修复
        if needs_fix(img_path):
            fixed_path = './' + img_path
            fixed_count += 1
            return f'{prefix}{quote}{fixed_path}{quote}'
        
        return match.group(0)
    
    new_content = re.sub(pattern, replace_html_path, content, flags=re.IGNORECASE)
    return new_content, fixed_count

def needs_fix(path):
    """
    判断路径是否需要添加 ./
    需要修复的情况：不是以 . / \ 开头
    """
    if not path:
        return False
    
    # 去除可能的空白字符
    path = path.strip()
    
    # 检查是否以 . / \ 开头
    if path.startswith('.') or path.startswith('/') or path.startswith('\\'):
        return False
    
    # 如果是 URL（包含 ://），不修改
    if '://' in path:
        return False
    
    # 如果是 data URI，不修改
    if path.startswith('data:'):
        return False
    
    return True

if __name__ == "__main__":
    print("Markdown 图片路径修复工具")
    print("=" * 50)
    print("功能：将不以 . / \\ 开头的图片路径前添加 ./")
    print("支持：![alt](path) 和 <img src=\"path\" /> 两种格式")
    print("=" * 50)
    
    # 询问用户确认
    confirm = input("\n是否开始处理？(y/n): ").strip().lower()
    
    if confirm == 'y' or confirm == 'yes':
        fix_image_paths_in_md()
    else:
        print("已取消操作")