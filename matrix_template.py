#!/usr/bin/env python3

def Basic():
    
    def init():
        visited = [[False for _ in arr[0]] for _ in arr]

    def dfs(arr):
        def helper(arr, i, j, visited):
            if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
                return
            if visited[i][j] == True:
                return
            visited[i][j] = True
            # Do action here...
            dfs(arr, i + 1, j, visited)
            dfs(arr, i - 1, j, visited)
            dfs(arr, i, j + 1, visited)
            dfs(arr, i, j - 1, visited)
        visited = [[False for _ in arr[0]] for _ in arr]
        helper(arr, 0, 0, visited)

    def bfs(arr):
        visited = [[False for _ in arr[0]] for _ in arr]
        queue = [(0, 0)]
        while len(queue) > 0:
            i, j = queue.pop(0)
            if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
                continue
            if visited[i][j] == True:
                continue
            visited[i][j] = True
            # Do action here...
            queue.append((i + 1, j))
            queue.append((i - 1, j))
            queue.append((i, j + 1))
            queue.append((i, j - 1))
