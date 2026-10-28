
from collections import deque
from platform import node

from matplotlib.pylab import record

from search_visualizer_helper import GRAPH, show_graph


def bfs(start, goal):
    events = []   #I am storing the steps of bfs here
    visited = set()  #keeping track of nodes that i visited
    visited_order = []  # Store nodes in the order they are visited
    parent = {start: None} #storing parent of each node
    queue = deque([start])

    def record(action, current=None, path=None):
        events.append({
            "action": action,
            "current": current,
            "visited": visited_order.copy(),
            "frontier": list(queue),
            "path": path or []
        })

    record("BFS started")  #recording iniital state

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        visited_order.append(node)  #thsi node has been visited
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

    record("Goal not found")  #if goal can't be found
    return events


if __name__ == "__main__":
    show_graph(bfs("A", "G"), "Breadth-First Search (BFS)")
