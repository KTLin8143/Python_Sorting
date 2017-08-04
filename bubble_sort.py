# -*- coding: utf-8 -*-

"""Bubble Sort"""


def bubble_sort(n):
    for i in range(0, len(n) - 1):  # 總共有n-1回 (n為數字個數)
        for j in range(0, len(n) - 1 - i):  # 每回所需檢查的個數
            if n[j] > n[j + 1]:
                temp = n[j]
                n[j] = n[j + 1]
                n[j + 1] = temp
        print('Round', i + 1, n)


mylist = [20, 9, 100, 0, 55, 3, 11]
print ('Bubble_Sort')
bubble_sort(mylist)
