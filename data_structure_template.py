#!/usr/bin/env python3

def char_dictionary():
    lower_dict = {chr(i): i - 96 for i in range(97, 123)}
    upper_dict = {chr(i): i - 64 for i in range(65, 91)}

def heap(arr):
    import heapq
    heap = arr
    heapq.heapify(heap)
    heapq.heappop(heap)
    heapq.heappush(heap, val)
    heapq.heappushpop(heap, val)
    heap[0]
