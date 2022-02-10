#!/usr/bin/env python3

def Basic():
    def init():
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                # Do action here...
                pass

def one_index():

    def dfs(arr, i, j):
        def foo(arr, i, j, visited):
            if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
                return
            if visited[i][j] == True:
                return
            # Add condiction here...
            visited[i][j] = True
            # Do action here...
            foo(arr, i + 1, j, visited)
            foo(arr, i - 1, j, visited)
            foo(arr, i, j + 1, visited)
            foo(arr, i, j - 1, visited)
        visited = [[False for _ in arr[0]] for _ in arr]
        foo(arr, i, j, visited)

    def bfs(arr, i, j):
        visited = [[False for _ in arr[0]] for _ in arr]
        queue = [(i, j)]
        while len(queue) > 0:
            i, j = queue.pop(0)
            if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
                continue
            if visited[i][j] == True:
                continue
            # Add condiction here...
            visited[i][j] = True
            # Do action here...
            queue.append((i + 1, j))
            queue.append((i - 1, j))
            queue.append((i, j + 1))
            queue.append((i, j - 1))

def all_index():

    def dfs(arr):
        def foo(arr, i, j, visited):
            if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
                return
            if visited[i][j] == True:
                return
            # Add condiction here...
            visited[i][j] = True
            # Do action here...
            foo(arr, i + 1, j, visited)
            foo(arr, i - 1, j, visited)
            foo(arr, i, j + 1, visited)
            foo(arr, i, j - 1, visited)
            visited[i][j] = False
        visited = [[False for _ in arr[0]] for _ in arr]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                foo(arr, 0, 0, visited)

    def bfs(arr):
        visited = [[False for _ in arr[0]] for _ in arr]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                queue = [(i, j)]
                while len(queue) > 0:
                    i, j = queue.pop(0)
                    if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
                        continue
                    if visited[i][j] == True:
                        continue
                    # Add condiction here...
                    visited[i][j] = True
                    # Do action here...
                    queue.append((i + 1, j))
                    queue.append((i - 1, j))
                    queue.append((i, j + 1))
                    queue.append((i, j - 1))
                    visited[i][j] = True
