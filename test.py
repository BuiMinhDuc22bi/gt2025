28/12/2024

import networkx as nx

# Create the graph
edges = [
    (1, 2), (2, 3), (2, 6), (1, 4), (6, 3), (6, 4),
    (5, 4), (5, 5), (5, 9), (7, 6), (7, 3), (7, 5),
    (7, 8), (8, 3), (8, 9)
]
G = nx.Graph()
G.add_edges_from(edges)

# 4. PathExistence(G, s, v)
def path_existence(graph, source, target):
    return nx.has_path(graph, source, target)

# 5. Find the sequence of vertices in a path
def find_path(graph, source, target):
    if nx.has_path(graph, source, target):
        return nx.shortest_path(graph, source, target)
    return None

# 6. Check if the path is unique
def is_unique_path(graph, source, target):
    if nx.has_path(graph, source, target):
        all_paths = list(nx.all_simple_paths(graph, source, target))
        return len(all_paths) == 1
    return False

# Example usage
source, target = 1, 6
print(f"Path exists: {path_existence(G, source, target)}")
print(f"Path: {find_path(G, source, target)}")
print(f"Is the path unique? {is_unique_path(G, source, target)}")

