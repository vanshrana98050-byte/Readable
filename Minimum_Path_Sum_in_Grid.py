rows = int(input())
cols = int(input())

grid = [list(map(int, input().split())) for _ in range(rows)]

for i in range(rows):
    for j in range(cols):

        if i == 0 and j == 0:
            continue

        if i == 0:
            grid[i][j] += grid[i][j-1]

        elif j == 0:
            grid[i][j] += grid[i-1][j]

        else:
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

print(grid[-1][-1])