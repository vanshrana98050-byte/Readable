from collections import defaultdict, deque

def alienOrder(words):
    graph = defaultdict(set)
    indegree = {}

    for word in words:
        for ch in word:
            indegree[ch] = 0

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]

        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break

    queue = deque([c for c in indegree if indegree[c] == 0])
    ans = []

    while queue:
        ch = queue.popleft()
        ans.append(ch)

        for nei in graph[ch]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return "".join(ans)

print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))