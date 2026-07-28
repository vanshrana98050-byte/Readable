import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start = int(input())

dist = [float("inf")] * n
dist[start] = 0

pq = [(0, start)]

while pq:

    d, node = heapq.heappop(pq)

    if d > dist[node]:
        continue

    for nxt, wt in graph[node]:

        nd = d + wt

        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

print(dist)