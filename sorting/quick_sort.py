# -*- coding: utf-8 -*-
"""
	Quick sort

	Quick sort is based on the divide-and-conquer approach based on the idea of choosing one element as a pivot element 
	and partitioning the array around it such that: Left side of pivot contains all the elements that are less than the pivot
	element Right side contains all elements greater than the pivot.

quick sort chọn 1 giá trị làm chốt, chuyển số lớn hơn chốt sang trái, nhỏ hơn chốt sang phải
chuyển xong thì đưa chốt vào giữa, tai được 2 list bên phải và bên trái chốt,lúc này chốt cố
định vị trí
tiếp tục chọn chốt và làm tiếp đến khi nào 2 list chỉ còn 1 phần tử là xong
"""
def partition(alist, left, right):
    pivot = alist[right]

    left_p = left
    right_p = right - 1

    while True:
        while left_p <= right_p and alist[left_p] <= pivot:
            left_p = left_p + 1

        while right_p >= left_p and alist[right_p] >= pivot:
            right_p = right_p - 1

        if left_p >= right_p:
            break
        else:
            alist[left_p], alist[right_p] = alist[right_p], alist[left_p]

    alist[left_p], alist[right] = alist[right], alist[left_p]

    return left_p
    

def quick_sort_helper(alist, left, right):
    if left >= right:
        return

    split_point = partition(alist, left, right)

    quick_sort_helper(alist, left, split_point - 1)
    quick_sort_helper(alist, split_point + 1, right)


def quickSort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)

alist = [3, 4, 2, 1, 8, 6, 9, 0, 5, 7]

quickSort(alist)
print(alist)

