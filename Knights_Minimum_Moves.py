from collections import deque

n = int(input())

sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

moves = [
    (2,1),(2,-1),(-2,1),(-2,-1),
    (1,2),(1,-2),(-1,2),(-1,-2)
]

queue = deque([(sx, sy, 0)])
visited = {(sx, sy)}

while queue:

    x, y, d = queue.popleft()

    if (x, y) == (tx, ty):
        print(d)
        break

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
            visited.add((nx, ny))
            queue.append((nx, ny, d + 1))