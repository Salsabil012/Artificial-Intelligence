
import heapq

from search_visualizer_helper import GRAPH, show_graph


def ucs(start, goal):
    events = []
    visited = set()
    parent = {start: None}
    distances = {start: 0}
    priority_queue = [(0, start)]  #using priority queue to explore the node with loweest cost first

    def record(action, current=None, path=None):
        events.append({
            "action": action,
            "current": current,
            "visited": list(visited),
            "frontier": [  #displaying nodes in order of their priority
                node for cost, node in sorted(priority_queue)
            ],
            "path": path or []
        })

    record("UCS started")

    while priority_queue:  #searching if priority queue not empty
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue   #skipping nodes if already finished

        visited.add(node)  #marking node as visited
        record(f"Exploring {node}, total cost = {cost}", node)

        if node == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            record(
                f"Goal found! Total cost = {cost}",
                node,
                path
            )
            return events

        for neighbor in GRAPH.neighbors(node):
            if neighbor in visited:
                continue

            edge_cost = GRAPH[node][neighbor]["weight"]  #storing edge cost
            new_cost = cost + edge_cost

            if new_cost < distances.get(neighbor, float("inf")):  #if cheap path found update neighbour 
                distances[neighbor] = new_cost
                parent[neighbor] = node

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor)
                )

        record(f"Updated priority queue after {node}", node)  #recording final path and total cost

    record("Goal not found")
    return events


if __name__ == "__main__":
    show_graph(ucs("A", "G"), "Uniform-Cost Search (UCS)")
