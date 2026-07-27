from collections import deque

begin = input()
end = input()

n = int(input())

words = set()

for _ in range(n):
    words.add(input())

queue = deque([(begin, 1)])

visited = {begin}

while queue:

    word, steps = queue.popleft()

    if word == end:
        print(steps)
        break

    for i in range(len(word)):
        for c in "abcdefghijklmnopqrstuvwxyz":

            new = word[:i] + c + word[i+1:]

            if new in words and new not in visited:
                visited.add(new)
                queue.append((new, steps + 1))
else:
    print(-1)