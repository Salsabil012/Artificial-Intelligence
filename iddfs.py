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


def iddfs(graph, start, goal):
    limit = 0

    while True:
        print(f"\nDepth limit {limit}: ", end="")

        if dls(graph, start, goal, limit):
            print("\nGoal found!")
            return

        limit += 1


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

iddfs(graph, 'A', 'G')