#!/usr/bin/env python3

def heap(arr):
    import heapq
    heap = arr
    heapq.heapify(heap)
    heapq.heappop(heap)
    heapq.heappush(heap, val)
    heapq.heappushpop(heap, val)
    heap[0]
