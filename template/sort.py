#!/usr/bin/env python3

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

def merge_sort():
    pass

def quick_sort():
    pass

def bucket_sort():
    pass
