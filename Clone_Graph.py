class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def clone(node, visited={}):
    if node is None:
        return None

    if node in visited:
        return visited[node]

    copy = Node(node.val)
    visited[node] = copy

    for nei in node.neighbors:
        copy.neighbors.append(clone(nei, visited))

    return copy