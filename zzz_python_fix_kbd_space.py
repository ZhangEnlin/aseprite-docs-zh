'''
    `<kbd>⌘⇧⌥S</kbd>` 等元素，经过VuePress之后，生成的HTML文件中，使用 `JetBrains Mono NL` 字体会显得特别拥挤，用这个脚本来给中间添加空格。
'''
import os
import re
from pathlib import Path

def fix_kbd_formatting_in_md():
    """
    递归检查当前文件夹内所有 .md 文件，
    修复 <kbd> 标签内的快捷键格式：
    1. 加号前后添加空格
    2. 特殊符号间添加空格
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
    print(f"处理完成！共修改 {files_modified} 个文件，修复 {total_fixed} 处 <kbd> 标签格式")
    
    return total_fixed

def process_md_file(file_path, current_dir):
    """
    处理单个 Markdown 文件，修复 <kbd> 标签格式
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 查找所有 <kbd> 标签并修复格式
        content, fixed_count = fix_kbd_tags(content)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            relative_path = file_path.relative_to(current_dir)
            print(f"✓ {relative_path} - 修复了 {fixed_count} 处 <kbd> 标签")
            return fixed_count
        
        return 0
        
    except Exception as e:
        relative_path = file_path.relative_to(current_dir)
        print(f"✗ 处理文件 {relative_path} 时出错: {e}")
        return 0

def fix_kbd_tags(content):
    """
    修复所有 <kbd> 标签内的格式
    """
    fixed_count = 0
    
    # 匹配 <kbd>...</kbd> 标签及其内容
    # 使用非贪婪匹配，支持多行
    pattern = r'<kbd>(.*?)</kbd>'
    
    def replace_kbd_content(match):
        nonlocal fixed_count
        original_content = match.group(1)
        
        # 修复快捷键格式
        fixed_content = fix_keyboard_shortcut(original_content)
        
        # 如果内容有变化
        if fixed_content != original_content:
            fixed_count += 1
            return f'<kbd>{fixed_content}</kbd>'
        
        return match.group(0)
    
    new_content = re.sub(pattern, replace_kbd_content, content, flags=re.DOTALL)
    return new_content, fixed_count

def fix_keyboard_shortcut(text):
    """
    修复键盘快捷键的格式
    1. 如果有加号，在加号前后添加空格
    2. 如果没有加号，检查特殊符号并添加空格
    """
    if not text or not text.strip():
        return text
    
    # 去除首尾空白
    text = text.strip()
    
    # 检查是否包含加号
    if '+' in text:
        # 处理加号：在加号前后添加空格
        return fix_plus_formatting(text)
    else:
        # 处理特殊符号间的空格
        return fix_special_keys_formatting(text)

def fix_plus_formatting(text):
    """
    处理包含加号的快捷键格式
    例如：Ctrl+Shift+F -> Ctrl + Shift + F
    """
    # 先移除加号周围已有的多余空格
    text = re.sub(r'\s*\+\s*', '+', text)
    
    # 在加号前后添加一个空格
    text = text.replace('+', ' + ')
    
    # 清理可能产生的多余空格
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def fix_special_keys_formatting(text):
    """
    处理特殊符号间的格式
    特殊符号：⌘ (Command), ⇧ (Shift), ⌥ (Option/Alt), ⌃ (Control)
    在这些符号之间添加空格
    """
    # 定义特殊符号集合
    special_keys = '⌘⇧⌥⌃'
    
    # 检查文本中是否包含这些特殊符号
    has_special = any(char in text for char in special_keys)
    
    if not has_special:
        return text
    
    # 方法1：使用正则表达式在特殊符号之间添加空格
    # 匹配连续的特殊符号
    pattern = f'([{re.escape(special_keys)}])([{re.escape(special_keys)}])'
    
    # 重复替换直到没有连续的符号
    prev_text = text
    while True:
        new_text = re.sub(pattern, r'\1 \2', prev_text)
        if new_text == prev_text:
            break
        prev_text = new_text
    
    text = new_text
    
    # 方法2：如果特殊符号与其他文本连在一起，也在前后添加空格
    for char in special_keys:
        if char in text:
            # 确保符号前后有空格（除非在开头或结尾）
            # 符号前不是空格且在开头或前面是字母数字
            text = re.sub(f'([a-zA-Z0-9])([{re.escape(char)}])', r'\1 \2', text)
            # 符号后不是空格且在结尾或后面是字母数字
            text = re.sub(f'([{re.escape(char)}])([a-zA-Z0-9])', r'\1 \2', text)
    
    # 清理多余空格
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def preview_changes():
    """
    预览模式：只显示将要修改的内容
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
            
            # 查找所有 <kbd> 标签
            pattern = r'<kbd>(.*?)</kbd>'
            matches = re.finditer(pattern, content, re.DOTALL)
            
            changes = []
            for match in matches:
                original_content = match.group(1)
                fixed_content = fix_keyboard_shortcut(original_content)
                
                if fixed_content != original_content:
                    changes.append((original_content, fixed_content))
            
            if changes:
                relative_path = md_file.relative_to(current_dir)
                print(f"\n文件: {relative_path}")
                for i, (old, new) in enumerate(changes, 1):
                    print(f"  {i}. <kbd>{old}</kbd> -> <kbd>{new}</kbd>")
                    total_changes += 1
        
        except Exception as e:
            relative_path = md_file.relative_to(current_dir)
            print(f"✗ 读取文件 {relative_path} 时出错: {e}")
    
    print("\n" + "=" * 60)
    print(f"预览完成，共发现 {total_changes} 处需要修复的 <kbd> 标签")
    
    return total_changes

# 测试函数
def test_fix_keyboard_shortcut():
    """
    测试快捷键修复功能
    """
    test_cases = [
        # 加号相关测试
        ("Ctrl+Shift+F", "Ctrl + Shift + F"),
        ("Ctrl + Shift + F", "Ctrl + Shift + F"),  # 已有空格
        ("Ctrl+  Shift+F", "Ctrl + Shift + F"),    # 不规则空格
        ("A+B+C", "A + B + C"),
        ("Ctrl+Alt+Delete", "Ctrl + Alt + Delete"),
        
        # 特殊符号测试
        ("⌘⇧⌥", "⌘ ⇧ ⌥"),
        ("⌘⇧", "⌘ ⇧"),
        ("⌘⌥", "⌘ ⌥"),
        ("⇧⌥", "⇧ ⌥"),
        ("⌘", "⌘"),  # 单个符号不变
        ("⌘⇧⌥⌃", "⌘ ⇧ ⌥ ⌃"),
        
        # 混合测试
        ("Ctrl⌘", "Ctrl ⌘"),  # 文本和符号间添加空格
        ("⌘F", "⌘ F"),
        
        # 普通文本
        ("Enter", "Enter"),
        ("Space", "Space"),
        ("Ctrl", "Ctrl"),
    ]
    
    print("测试修复功能：")
    print("-" * 40)
    all_passed = True
    
    for input_text, expected in test_cases:
        result = fix_keyboard_shortcut(input_text)
        if result == expected:
            print(f"✓ <kbd>{input_text}</kbd> -> <kbd>{result}</kbd>")
        else:
            print(f"✗ <kbd>{input_text}</kbd> -> <kbd>{result}</kbd> (期望: <kbd>{expected}</kbd>)")
            all_passed = False
    
    print("-" * 40)
    if all_passed:
        print("所有测试通过！")
    else:
        print("部分测试失败！")
    
    return all_passed

if __name__ == "__main__":
    print("KBD 标签格式修复工具")
    print("=" * 60)
    print("功能：修复 Markdown 文件中 <kbd> 标签的快捷键格式")
    print("规则：")
    print("  1. 包含加号：在加号前后添加空格")
    print("     例如：Ctrl+Shift+F -> Ctrl + Shift + F")
    print("  2. 包含特殊符号(⌘⇧⌥⌃)：在符号间添加空格")
    print("     例如：⌘⇧⌥ -> ⌘ ⇧ ⌥")
    print("=" * 60)
    
    print("\n请选择操作：")
    print("1. 运行测试")
    print("2. 预览模式（查看将要修改的内容）")
    print("3. 直接修复（修改文件）")
    print("4. 取消")
    
    choice = input("\n请输入选项 (1/2/3/4): ").strip()
    
    if choice == '1':
        test_fix_keyboard_shortcut()
    elif choice == '2':
        preview_changes()
        confirm = input("\n是否继续修复这些文件？(y/n): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            fix_kbd_formatting_in_md()
        else:
            print("已取消操作")
    elif choice == '3':
        confirm = input("\n确认要修改文件吗？(y/n): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            fix_kbd_formatting_in_md()
        else:
            print("已取消操作")
    else:
        print("已取消操作")