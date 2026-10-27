
from search_visualizer_helper import GRAPH, show_graph

DEPTH_LIMIT = 2


def dls(start, goal, depth_limit):
    events = []
    visited = set()
    path = []

    def record(action, current=None):
        events.append({
            "action": action,
            "current": current,
            "visited": list(visited),
            "frontier": list(path),
            "path": path.copy() if action == "Goal found!" else []
        })

    def search(node, depth):
        path.append(node)
        visited.add(node)
        record(f"Exploring {node} at depth {depth}", node)

        if node == goal:
            record("Goal found!", node)
            path.pop()
            return True

        if depth == depth_limit:
            record(f"Depth limit reached at {node}", node)
            path.pop()
            return False

        for neighbor in sorted(GRAPH.neighbors(node)):
            if neighbor not in path:
                if search(neighbor, depth + 1):
                    path.pop()
                    return True

        record(f"Backtracking from {node}", node)
        path.pop()
        return False

    record("DLS started")

    found = search(start, 0)

    if not found:
        record("Goal not found within depth limit")

    return events


if __name__ == "__main__":
    show_graph(
        dls("A", "G", DEPTH_LIMIT),
        "Depth-Limited Search (DLS)"
    )
