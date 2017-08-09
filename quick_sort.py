# -*- coding: utf-8 -*-

"""Qucik  Sort"""


def divide(list):
    return quick_sort(list, 0, len(list) - 1)


def quick_sort(list, left, right):
    if right <= left:
        return list
    # 在此挑選最左邊的元素作為pivot
    pivot = list[left]
    left_pivot = left
    right_pivot = right
    while left_pivot < right_pivot:
        # 由右邊至左邊，遇到比pivot"小"的才停下來
        while left_pivot < right_pivot and list[right_pivot] >= pivot:
            right_pivot -= 1
        # 由左邊至右邊，遇到比pivot"大"的才停下來
        while left_pivot < right_pivot and list[left_pivot] <= pivot:
            left_pivot += 1
        if left_pivot < right_pivot:
            list[left_pivot], list[right_pivot] = list[right_pivot], list[left_pivot]
    list[left], list[left_pivot] = list[left_pivot], list[left]  # 跟key值交換
    quick_sort(list, left, left_pivot - 1)
    quick_sort(list, right_pivot + 1, right)
    return list


mylist = [13, 20, 27, 97, 3, 32, 42, 26, 60, 66]
print (divide(mylist))
