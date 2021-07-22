# Escape-symbols table
""" Написать программу, которая выводит в консоль таблицу Escape-последовательностей:
Escape sequences
\a    -  Bell (alert)
\b    -  Backspace
\n    -  New line
\t     - Horizontal tab
\\     -  Backslash \
\"     - Double quotation mark "
\'     - Single quotation mark ' """

esc_table = {"bell": "\\a\t-\tBell (alert)", "backspace": "\\b\t-\tBackspace",
             "new_line": "\\n\t-\tNew Line", "tab": "\\t\t-\tHorizontal tab",
             "backslash": "\\\\\t-\tBackslash \\", "double_mark": "\\\"\t-\tDouble quotation mark \"",
             "single_mark": "\\\'\t-\tSingle quotation mark \'"}
for key in esc_table:
    print(esc_table[key])
