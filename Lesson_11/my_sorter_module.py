# Create by Bender
"""
Данный модуль выполняет сортировку последовательностей (список)
при помощи двух разных алгоритмов.
Пузырьковая сортировка - список сортируется методом пузырька.
Быстрая сортировка - список сортируется методом быстрой сортировки.
"""

__all__ = ["bubble_sort", "quick_sort"]


def bubble_sort(nums: list) -> list:
    """
    Функция осуществляет сортировку переданного массива методом пузырька
    :param nums: Принимает несортированный список
    :return:     Возвращает отсортированный список
    """

    size_list = len(nums)
    for i in range(size_list - 1):
        for j in range(size_list - 2, i - 1, -1):
            if nums[j + 1] < nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def partition(nums, low, high):
    """
    Функция определения среднего элемента последовательности,
    в качестве опорного.
    :param nums: Принимает несортированный список
    :param low:  Принимает нижний граничный элемент
    :param high: Принимает верхний граничный элемент
    :return:     Возвращает средний элемент
    """
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums: list) -> list:
    """
    Функция быстрой сортировки
    :param nums: Принимает несортированный список
    :return:     Возвращает сортированный список
    """
    def _quick_sort(items: list, low: int, high: int) -> None:
        """
        Вспомогательная функция, которая вызывается рекурсивно,
        служит для получения опорного элемента
        относительно которого разделяется последовательность.
        :param items: Принимает несортированный список
        :param low:   Принимает нижний граничный элемент
        :param high:  Принимает верхний граничный элемент
        :return:      Ничего не возвращает
        """
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums)-1)
    return nums
