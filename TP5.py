import sys

def dijkstra(graph, source, target):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    previous = [-1] * n

    distance[source] = 0

    for _ in range(n):
        # Find the unvisited node with the smallest distance
        min_dist = sys.maxsize
        min_node = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_node = i

        if min_node == -1:  # No reachable nodes left
            break

        visited[min_node] = True

        # Update distances for neighbors of the current node
        for neighbor in range(n):
            if graph[min_node][neighbor] != float('inf') and not visited[neighbor]:
                new_dist = distance[min_node] + graph[min_node][neighbor]
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    previous[neighbor] = min_node

    # Reconstruct the shortest path
    path = []
    current = target
    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distance[target]

# Graph adjacency matrix representation
graph = [
    [0, 4, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [4, 0, float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf'), float('inf')],
    [1, float('inf'), 0, 8, float('inf'), 7, float('inf'), float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 8, 0, float('inf'), float('inf'), float('inf'), 5, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0, 1, float('inf'), 2, 2, float('inf')],
    [float('inf'), 3, 7, float('inf'), 1, 0, float('inf'), 1, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0, 3, 4, 4],
    [float('inf'), float('inf'), float('inf'), 5, 2, 1, 3, 0, 6, 7],
    [float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 4, 6, 0, 1],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 4, 7, 1, 0]
]

# Node labels
nodes = "ABCDEFGHLM"

# Input source and target
source_label = input("Enter source node (e.g., A): ").strip().upper()
target_label = input("Enter target node (e.g., M): ").strip().upper()

source = nodes.index(source_label)
target = nodes.index(target_label)

# Run Dijkstra's algorithm
path, total_weight = dijkstra(graph, source, target)

# Convert path indices back to labels
path_labels = [nodes[i] for i in path]

# Output results
print("Shortest path (in reverse):", path_labels[::-1])
print("Total weight of shortest path:", total_weight)
