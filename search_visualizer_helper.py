
import tkinter as tk
from tkinter import ttk

import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Graph edges and their weights
EDGES = [
    ("A", "B", 1),
    ("A", "C", 4),
    ("B", "D", 2),
    ("B", "E", 5),
    ("C", "F", 1),
    ("C", "G", 3),
    ("D", "G", 6),
    ("E", "G", 1),
    ("F", "G", 2)
]

GRAPH = nx.Graph()

for u, v, weight in EDGES:
    GRAPH.add_edge(u, v, weight=weight)


# Fixed positions so the graph looks organized
POS = {
    "A": (0, 2),
    "B": (-1.2, 1),
    "C": (1.2, 1),
    "D": (-1.8, 0),
    "E": (-0.6, 0),
    "F": (0.6, 0),
    "G": (1.8, 0)
}


def show_graph(events, title):
    root = tk.Tk()
    root.title(title)
    root.geometry("950x700")

    state = {
        "step": 0,
        "playing": False,
        "timer": None
    }

    fig = Figure(figsize=(8, 5), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    info = tk.StringVar()

    ttk.Label(
        root,
        textvariable=info,
        wraplength=900
    ).pack(fill=tk.X, padx=8, pady=5)

    def draw():
        event = events[state["step"]]

        ax.clear()
        ax.set_title(
            f"{title} - Step {state['step'] + 1}/{len(events)}"
        )

        current = event.get("current")
        visited = set(event.get("visited", []))
        frontier = set(event.get("frontier", []))
        path = event.get("path", [])

        colors = []

        for node in GRAPH.nodes:
            if node in path:
                colors.append("#43A047")  # Green: final path
            elif node == current:
                colors.append("#FB8C00")  # Orange: current node
            elif node in frontier:
                colors.append("#64B5F6")  # Blue: waiting to be explored
            elif node in visited:
                colors.append("#BDBDBD")  # Gray: visited
            else:
                colors.append("#E8EAF6")  # Light: not explored yet

        nx.draw_networkx_edges(GRAPH, POS, ax=ax)

        if len(path) > 1:
            path_edges = list(zip(path[:-1], path[1:]))

            nx.draw_networkx_edges(
                GRAPH,
                POS,
                edgelist=path_edges,
                edge_color="green",
                width=4,
                ax=ax
            )

        nx.draw_networkx_nodes(
            GRAPH,
            POS,
            node_color=colors,
            node_size=1400,
            ax=ax
        )

        nx.draw_networkx_labels(GRAPH, POS, ax=ax)

        edge_labels = {
            (u, v): data["weight"]
            for u, v, data in GRAPH.edges(data=True)
        }

        nx.draw_networkx_edge_labels(
            GRAPH,
            POS,
            edge_labels=edge_labels,
            ax=ax
        )

        ax.axis("off")
        fig.tight_layout()
        canvas.draw()

        info.set(
            f"Action: {event['action']} | "
            f"Visited: {event.get('visited', [])} | "
            f"Frontier: {event.get('frontier', [])} | "
            f"Path: {path}"
        )

    def pause():
        state["playing"] = False

        if state["timer"] is not None:
            root.after_cancel(state["timer"])
            state["timer"] = None

    def next_step():
        pause()

        if state["step"] < len(events) - 1:
            state["step"] += 1

        draw()

    def previous_step():
        pause()

        if state["step"] > 0:
            state["step"] -= 1

        draw()

    def animate():
        if not state["playing"]:
            return

        if state["step"] < len(events) - 1:
            state["step"] += 1
            draw()
            state["timer"] = root.after(800, animate)
        else:
            pause()

    def play():
        if state["step"] >= len(events) - 1:
            state["step"] = 0

        state["playing"] = True
        animate()

    def reset():
        pause()
        state["step"] = 0
        draw()

    controls = ttk.Frame(root, padding=8)
    controls.pack()

    ttk.Button(
        controls, text="Previous", command=previous_step
    ).pack(side=tk.LEFT, padx=4)

    ttk.Button(
        controls, text="Next", command=next_step
    ).pack(side=tk.LEFT, padx=4)

    ttk.Button(
        controls, text="Play", command=play
    ).pack(side=tk.LEFT, padx=4)

    ttk.Button(
        controls, text="Pause", command=pause
    ).pack(side=tk.LEFT, padx=4)

    ttk.Button(
        controls, text="Reset", command=reset
    ).pack(side=tk.LEFT, padx=4)

    draw()
    root.mainloop()
