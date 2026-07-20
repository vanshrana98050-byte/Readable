rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()