# Create by Bender
"""
Демонстрация работы с импортированными пакетами и модулями.
Скрипт сортирует сгенерированный список, в сортированном списке устанавливает диапазон из которго
будет, случайным образом, выбираться число, которое будет являтся высотой фигуры, которые, затем
будут выведены на экран.
"""
import random
from my_package import drawing as draw
import my_sorter_module as sort

help(draw)
help(sort)

list_gen = [random.randint(1, 25) for i in range(10)]
print(f"This is unsorted list: {list_gen}")

bubble_list = sort.bubble_sort(list_gen)
print(f"This is bubble_sort list: {bubble_list}")

quick_list = sort.quick_sort(list_gen)
print(f"This is quick_sort list: {quick_list}")

figure_height = random.choice(quick_list[1:5])
draw.triangle(figure_height)
print()
draw.empty_triangle(figure_height)
print()
draw.rhombus(figure_height)
print()
draw.rhombus_line(figure_height)
