def dls(graph, node, goal, limit, depth=0):
    print(node, end=" ")

    if node == goal:
        return True

    if depth == limit:
        return False

    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, limit, depth + 1):
            return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

limit = 1

if dls(graph, 'A', 'G', limit):
    print("\nGoal found!")
else:
    print("\nGoal not found within depth limit.")