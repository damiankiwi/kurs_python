def find_islands(matrix):
    def dfs(i, j):
        if i < 0 or i >= 10 or j < 0 or j >= 10 or matrix[i][j] == 0:
            return
        matrix[i][j] = 0
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    islands = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                islands += 1
                dfs(i, j)

    return islands

# Input data
matrix = [
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 0]
]


result = find_islands(matrix)
print(f"Liczba wysp: {result}")