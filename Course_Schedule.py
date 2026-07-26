from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque()

    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    count = 0

    while queue:
        node = queue.popleft()
        count += 1

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return count == numCourses

print(canFinish(2, [[1, 0]]))