#!/usr/bin/env python3

def basic():
    class Graph:
        def __init__(self):
            self.val = None
            self.neighbors = []

def DAG():

    def dfs(n, root):
        def helper(node, visited)
            if visited[node.val] is False:
                visited[node.val] = True
                for next_node in node.neighbors:
                    helper(next_node, visited)
        visited = [False for _ in range(n)]
        dfs(root, visited)

    def bfs(n, root):
        queue, visited[root.val] = [root], True
        while len(queue) > 0:
            node = queue.pop(0)
            for next_node in node.neighbors:
                if visited[next_node.val] is False:
                    visited[next_node.val] = True
                    queue.append(next_node)

    def topological_sort(n, conds):
        # Build graph and indegree.
        graph = {i: [] for i in range(n)}
        indegree = {i: 0 for i in range(n)}
        for cond in conds:
            graph[cond[1]].append(cond[0])
            indegree[cond[0]] += 1
        # Build queue for arrangement.
        path = []
        queue = [key for key in indegree if key == 0]
        while len(queue) > 0:
            n = queue.pop(0)
            path.append(n)
            for next_n in graph[n]:
                indegree[next_n] -= 1
                if indegree[next_n] == 0:
                    path.append(next_n)
        for val in indegree.values():
            if val > 0:
                return []
        return path
