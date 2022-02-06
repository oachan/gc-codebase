#!/usr/bin/env python3

def Basic():
    
    def init():
        visited = [[False for _ in arr[0]] for _ in arr]

    def dfs(arr, i, j, visited):
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

    def bfs():
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                print(matrix[i][j])
