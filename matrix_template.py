def Basic():
    
    def dfs():
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                print(matrix[i][j])

    def bfs():
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                print(matrix[i][j])
