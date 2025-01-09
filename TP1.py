import networkx as nx
import matplotlib.pyplot as plt

# Recreate the graph based on the description
G = nx.Graph()
edges = [(1, 2), (2, 5), (6, 3), (4, 6), (4, 7), (6, 7)]
G.add_edges_from(edges)

def path_existence(graph, node1, node2):
    """
    Check if a path exists between two nodes in the graph.
    Args:
        graph (nx.Graph): The graph to check.
        node1 (int): The first node.
        node2 (int): The second node.
    Returns:
        bool: True if a path exists, False otherwise.
    """
    try:
        # Use NetworkX's has_path function to check for a path
        return nx.has_path(graph, node1, node2)
    except nx.NetworkXError:
        # If nodes do not exist in the graph, return False
        return False

def draw_graph_with_path(graph, node1, node2):
    """
    Draws the graph and highlights the path between two nodes if it exists.
    """
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph, seed=42)
    
    # Draw the graph
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=12)
    
    if nx.has_path(graph, node1, node2):
        # Find the shortest path and highlight it
        path = nx.shortest_path(graph, source=node1, target=node2)
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, edge_color='red', width=2)
        print(f"Path exists: {' -> '.join(map(str, path))}")
    else:
        print(f"No path exists between node {node1} and node {node2}.")
    
    plt.title(f"Graph Visualization with Path from {node1} to {node2}")
    plt.show()

# User inputs
node1 = int(input("Enter the first node (1-7): "))
node2 = int(input("Enter the second node (1-7): "))

# Check if path exists and visualize the result
exists = path_existence(G, node1, node2)
draw_graph_with_path(G, node1, node2)
