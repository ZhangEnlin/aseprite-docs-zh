'''
    跳转 `*.md` 文件的超链接如果以当前文件夹为根目录的话，则在 `src` 前方加上 `./` 以明确表示当前文件夹。
'''
import os
import re
from pathlib import Path

def fix_md_links_in_md():
    """
    递归检查当前文件夹内所有 .md 文件，
    修复不以 . / \ 开头的 .md 超链接路径，在前面加上 ./
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
    print(f"处理完成！共修改 {files_modified} 个文件，修复 {total_fixed} 处 .md 超链接路径")
    
    return total_fixed

def process_md_file(file_path, current_dir):
    """
    处理单个 Markdown 文件，修复 .md 超链接路径
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 修复普通超链接：[]()
        content, fixed_count = fix_markdown_links(content)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            relative_path = file_path.relative_to(current_dir)
            print(f"✓ {relative_path} - 修复了 {fixed_count} 处 .md 超链接")
            return fixed_count
        
        return 0
        
    except Exception as e:
        relative_path = file_path.relative_to(current_dir)
        print(f"✗ 处理文件 {relative_path} 时出错: {e}")
        return 0

def fix_markdown_links(content):
    """
    修复 Markdown 普通超链接 [text](url)
    只处理以 .md 结尾的链接
    """
    fixed_count = 0
    
    # 匹配 [文本](链接)
    # 但要排除图片语法 ![]()
    pattern = r'(?<!!)\[([^\]]*)\]\(([^)]+)\)'
    
    def replace_markdown_link(match):
        nonlocal fixed_count
        link_text = match.group(1)  # 超链接文本
        link_url = match.group(2).strip()  # 超链接 URL
        
        # 检查是否是 .md 文件且需要修复
        if is_md_file_need_fix(link_url):
            fixed_url = './' + link_url
            fixed_count += 1
            return f'[{link_text}]({fixed_url})'
        
        return match.group(0)
    
    new_content = re.sub(pattern, replace_markdown_link, content)
    return new_content, fixed_count

def is_md_file_need_fix(url):
    """
    判断 URL 是否是需要修复的 .md 文件路径
    """
    if not url:
        return False
    
    # 去除可能的空白字符和 URL 片段（#后面的部分）
    url = url.strip()
    
    # 分离 URL 片段
    base_url = url.split('#')[0]
    
    # 检查是否以 .md 结尾（不区分大小写）
    if not base_url.lower().endswith('.md'):
        return False
    
    # 排除以 . / \ 开头的路径
    if url.startswith('.') or url.startswith('/') or url.startswith('\\'):
        return False
    
    # 排除网络 URL
    if '://' in url:
        return False
    
    # 排除 mailto: 等特殊协议
    if ':' in url and '://' not in url:
        return False
    
    return True

def preview_changes():
    """
    预览模式：只显示将要修改的内容，不实际修改文件
    """
    current_dir = Path.cwd()
    md_files = list(current_dir.rglob('*.md'))
    
    if not md_files:
        print("当前目录下未找到任何 Markdown 文件")
        return
    
    print("预览模式 - 将要修改的内容：")
    print("=" * 60)
    
    total_changes = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找所有需要修改的链接
            pattern = r'(?<!!)\[([^\]]*)\]\(([^)]+)\)'
            matches = re.finditer(pattern, content)
            
            changes = []
            for match in matches:
                link_text = match.group(1)
                link_url = match.group(2).strip()
                
                if is_md_file_need_fix(link_url):
                    fixed_url = './' + link_url
                    changes.append((link_text, link_url, fixed_url))
            
            if changes:
                relative_path = md_file.relative_to(current_dir)
                print(f"\n文件: {relative_path}")
                for i, (text, old_url, new_url) in enumerate(changes, 1):
                    print(f"  {i}. [{text}]({old_url}) -> [{text}]({new_url})")
                    total_changes += 1
        
        except Exception as e:
            relative_path = md_file.relative_to(current_dir)
            print(f"✗ 读取文件 {relative_path} 时出错: {e}")
    
    print("\n" + "=" * 60)
    print(f"预览完成，共发现 {total_changes} 处需要修改的 .md 超链接")
    
    return total_changes

if __name__ == "__main__":
    print("Markdown 文件超链接路径修复工具")
    print("=" * 60)
    print("功能：将不以 . / \\ 开头的 .md 超链接路径前添加 ./")
    print("格式：[文本](链接.md) -> [文本](./链接.md)")
    print("=" * 60)
    
    print("\n请选择操作模式：")
    print("1. 直接修复（修改文件）")
    print("2. 预览模式（查看将要修改的内容）")
    print("3. 取消")
    
    choice = input("\n请输入选项 (1/2/3): ").strip()
    
    if choice == '1':
        confirm = input("\n确认要修改文件吗？(y/n): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            fix_md_links_in_md()
        else:
            print("已取消操作")
    elif choice == '2':
        preview_changes()
        # 询问是否继续修复
        confirm = input("\n是否继续修复这些文件？(y/n): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            fix_md_links_in_md()
        else:
            print("已取消操作")
    else:
        print("已取消操作")