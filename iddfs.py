
from search_visualizer_helper import GRAPH, show_graph

MAX_DEPTH = 5


def iddfs(start, goal, max_depth):
    events = []

    def record(action, current=None, visited=None, path=None):
        events.append({
            "action": action,
            "current": current,
            "visited": list(visited or []),
            "frontier": [],
            "path": path or []
        })

    for limit in range(max_depth + 1):
        visited = set()
        path = []

        record(f"Starting DLS with depth limit {limit}")

        def search(node, depth):
            path.append(node)
            visited.add(node)

            record(
                f"Exploring {node} at depth {depth} "
                f"(limit {limit})",
                node,
                visited,
                path if node == goal else []
            )

            if node == goal:
                record("Goal found!", node, visited, path.copy())
                path.pop()
                return True

            if depth == limit:
                record(
                    f"Depth limit reached at {node}",
                    node,
                    visited
                )
                path.pop()
                return False

            for neighbor in sorted(GRAPH.neighbors(node)):
                if neighbor not in path:
                    if search(neighbor, depth + 1):
                        path.pop()
                        return True

            path.pop()
            return False

        if search(start, 0):
            return events

    record("Goal not found within maximum depth")
    return events


if __name__ == "__main__":
    show_graph(
        iddfs("A", "G", MAX_DEPTH),
        "Iterative Deepening DFS (IDDFS)"
    )
