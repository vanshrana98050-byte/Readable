rows = int(input())
cols = int(input())

grid = []

for _ in range(rows):
    grid.append(list(input()))

def dfs(r, c):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return

    if grid[r][c] == '0':
        return

    grid[r][c] = '0'

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)

count = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '1':
            dfs(i, j)
            count += 1

print(count)