
from collections import deque

from search_visualizer_helper import GRAPH, show_graph


def bfs(start, goal):
    events = []
    visited = set()
    parent = {start: None}
    queue = deque([start])

    def record(action, current=None, path=None):
        events.append({
            "action": action,
            "current": current,
            "visited": list(visited),
            "frontier": list(queue),
            "path": path or []
        })

    record("BFS started")

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        record(f"Exploring {node}", node)

        if node == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            record("Goal found!", node, path)
            return events

        for neighbor in sorted(GRAPH.neighbors(node)):
            if neighbor not in visited and neighbor not in queue:
                parent[neighbor] = node
                queue.append(neighbor)

        record(f"Updated queue after {node}", node)

    record("Goal not found")
    return events


if __name__ == "__main__":
    show_graph(bfs("A", "G"), "Breadth-First Search (BFS)")
