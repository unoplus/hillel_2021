# Create by Bender
"""
Подключение динамического модуля.
"""

# Представим, что есть 2 модуля test.py, tests.py
# Например мы можем по требованиям подключить только один модуль
# Тогда динамически мы можкм создать строку - имя модуля для подключения
# И подключить используя __import__()

TEST = 1
module_name_dyn = "test"

if TEST == 1:
    module_name_dyn += "s"

module = __import__(module_name_dyn)
print(module.x)
input()
