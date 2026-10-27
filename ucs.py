import heapq

def ucs(graph, start, goal):
    priority_queue = [(0, start)]
    distances = {start: 0}
    parent = {start: None}

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if cost != distances[node]:
            continue

        print(f"{node}(cost={cost})", end=" ")

        if node == goal:
            print(f"\nMinimum cost: {cost}")

            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            print("Path:", " -> ".join(path))
            return

        for neighbor, edge_cost in graph[node]:
            new_cost = cost + edge_cost

            if new_cost < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_cost
                parent[neighbor] = node

                heapq.heappush(
                    priority_queue, (new_cost, neighbor)
                )

    print("\nGoal not found.")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1), ('G', 3)],
    'D': [('G', 6)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

ucs(graph, 'A', 'G')