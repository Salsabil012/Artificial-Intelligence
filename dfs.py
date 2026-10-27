
from search_visualizer_helper import GRAPH, show_graph


def dfs(start, goal):
    events = []
    visited = set()
    parent = {start: None}
    stack = [start]

    def record(action, current=None, path=None):
        events.append({
            "action": action,
            "current": current,
            "visited": list(visited),
            "frontier": list(stack),
            "path": path or []
        })

    record("DFS started")

    while stack:
        node = stack.pop()

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

        # Reverse order makes the alphabetically first
        # neighbor get explored first.
        for neighbor in sorted(
            GRAPH.neighbors(node), reverse=True
        ):
            if neighbor not in visited and neighbor not in stack:
                parent[neighbor] = node
                stack.append(neighbor)

        record(f"Updated stack after {node}", node)

    record("Goal not found")
    return events


if __name__ == "__main__":
    show_graph(dfs("A", "G"), "Depth-First Search (DFS)")
