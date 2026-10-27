def dfs(graph, node, goal, visited):
    visited.add(node)
    print(node, end=" ")

    if node == goal:
        return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
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

if dfs(graph, 'A', 'G', set()):
    print("\nGoal found!")
else:
    print("\nGoal not found.")