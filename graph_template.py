#!/usr/bin/env python3

def basic():
    class Graph:
        def __init__(self):
            self.val = None
            self.neighbors = []

def dfs(node, visited):
    if node is None:
        return
    visited[node.val] = True
    for next_node in node.neighbors:
        dfs(next_node, visited)

def bfd():
    pass

def topological_sort():
    pass
