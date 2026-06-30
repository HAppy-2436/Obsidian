"""
markdown → 邮件正文 / 在线表单正文 转换器
规则：
- # 标题     → 【标题】
- ## 标题    → 【标题】
- ### 标题   → —— 标题 ——
- **粗体**    → 【粗体】
- *斜体*     → "斜体"
- [文字](url) → 文字（url）
- ![alt](url) → [图片：alt]
- | 表格 |   → "   |   "  保留列结构但不用管道
- ---       → ——————
- 引用 > xxx → 【引用】xxx
- 多余空行合并为一个空行

用法：
  python md2mail.py input.md               # 打印结果
  python md2mail.py input.md output.txt    # 写入文件
  python md2mail.py in1.md in2.md ...     # 多个文件逐一打印
"""

import sys
import re


def md_to_mail(md_text: str) -> str:
    lines = md_text.split('\n')
    out = []
    in_table = False

    for line in lines:
        raw = line.rstrip()

        # 分隔线
        if raw.strip() == '---':
            out.append('——————')
            continue

        # 标题
        if raw.startswith('# '):
            out.append('')
            out.append(f'【{raw[2:].strip()}】')
            out.append('')
            continue
        if raw.startswith('## '):
            out.append('')
            out.append(f'【{raw[3:].strip()}】')
            continue
        if raw.startswith('### '):
            out.append('')
            out.append(f'—— {raw[4:].strip()} ——')
            continue

        # 表格分割行（|---|---|
        if re.match(r'^\s*\|[\s\-:|]+\|\s*$', raw):
            in_table = True
            continue

        # 普通表格行：把 | 分隔的单元格改为 " | " 显示，并把整行转为 "列1: xxxxx" 风格
        if raw.lstrip().startswith('|'):
            cells = [c.strip() for c in raw.strip().strip('|').split('|')]
            cells = [c for c in cells if c]
            if cells:
                # 用 全角空格 和 全角竖线 让中文阅读舒服
                out.append('  ｜  '.join(cells))
            in_table = True
            continue
        elif in_table and not raw.lstrip().startswith('|') and raw.strip() != '':
            in_table = False
            out.append('')
            out.append(raw)
            continue
        elif in_table and raw.strip() == '':
            in_table = False
            continue

        # 引用
        if raw.startswith('> '):
            content = raw[2:].strip()
            # 嵌套引用 > >
            content = re.sub(r'^>\s*', '', content)
            out.append(f'  › {content}')
            continue
        if raw.startswith('>'):
            content = raw.lstrip('>').strip()
            out.append(f'  › {content}')
            continue

        # 有序列表（保留）
        if re.match(r'^\s*\d+\.\s+', raw):
            out.append(raw)
            continue

        # 无序列表（保留）
        if re.match(r'^\s*[-*]\s+', raw):
            out.append(raw)
            continue

        # 空行
        if raw.strip() == '':
            out.append('')
            continue

        # 加粗
        line = re.sub(r'\*\*(.+?)\*\*', r'【\1】', raw)

        # 斜体
        line = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'"\1"', line)

        # 行内代码
        line = re.sub(r'`([^`]+)`', r'（\1）', line)

        # 链接 [文字](url)
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1（\2）', line)

        # 图片 ![alt](url)
        line = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'[图片：\1]', line)

        out.append(line)

    # 合并多余空行
    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'


def main():
    args = sys.argv[1:]
    if not args:
        print('用法：python md2mail.py <input.md> [output.txt]')
        print('  python md2mail.py 02_举报渠道汇总.md output.txt')
        print('  python md2mail.py *.md                # 多个文件逐一处理')
        sys.exit(1)

    # 支持通配符
    import glob
    files = []
    for a in args:
        if '*' in a or '?' in a:
            files.extend(glob.glob(a))
        else:
            files.append(a)

    if len(files) == 1:
        inp = files[0]
        with open(inp, 'r', encoding='utf-8') as f:
            md = f.read()
        result = md_to_mail(md)
        out = inp.rsplit('.', 1)[0] + '_邮件版.txt' if '.' in inp else inp + '_邮件版.txt'
        with open(out, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f'已写入：{out}（{len(result)} 字符）')
    else:
        for inp in files:
            try:
                with open(inp, 'r', encoding='utf-8') as f:
                    md = f.read()
                result = md_to_mail(md)
                out = inp.rsplit('.', 1)[0] + '_邮件版.txt' if '.' in inp else inp + '_邮件版.txt'
                with open(out, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f'已转换：{inp} -> {out}（{len(result)} 字符）')
            except Exception as e:
                print(f'跳过 {inp}: {e}')


if __name__ == '__main__':
    main()
