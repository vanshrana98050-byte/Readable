INF = 10**9

n = int(input())
m = int(input())

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):

    u, v, w = map(int, input().split())

    dist[u][v] = w

for k in range(n):

    for i in range(n):

        for j in range(n):

            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )

for row in dist:
    print(*row)