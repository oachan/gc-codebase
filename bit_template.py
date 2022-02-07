#!/usr/bin/env python3

MAX_INT = 0x7FFFFFFF
MIN_INT = 0x80000000
MASK = 0x100000000

def bitarray(arr):
    bitarray = 1 << len(arr)
    bitarray = bitarray | (1 << bit)  # on
    bitarray = bitarray & ~(1 << bit)  # off
    flag = bitarray & (1 << bit)
    
