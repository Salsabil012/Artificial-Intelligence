
from search_visualizer_helper import GRAPH, show_graph

DEPTH_LIMIT = 2  #maximum depth search can reach


def dls(start, goal, depth_limit):
    events = []
    visited = set()
    path = []  #storing current path from start

    def record(action, current=None): #storing the steps here
        events.append({
            "action": action,
            "current": current,
            "visited": list(visited),
            "frontier": list(path),
            "path": path.copy() if action == "Goal found!" else []
        })

    def search(node, depth):
        path.append(node)
        visited.add(node)  #tracking visited nodes
        record(f"Exploring {node} at depth {depth}", node)

        if node == goal:  #if goal node found, search stops
            record("Goal found!", node)
            path.pop()
            return True

        if depth == depth_limit:  #if goal limit reached stop exploring
            record(f"Depth limit reached at {node}", node)
            path.pop()
            return False

        for neighbor in sorted(GRAPH.neighbors(node)):
            if neighbor not in path:
                if search(neighbor, depth + 1):
                    path.pop()
                    return True

        record(f"Backtracking from {node}", node)
        path.pop()  #remove current node
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
