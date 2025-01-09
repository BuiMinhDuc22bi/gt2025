from collections import defaultdict

# Adjusted adjacency matrix without node 0
G = [
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0]
]

# Helper function to perform DFS
def dfs(graph, v, visited, result=None):
    visited[v] = True
    if result is not None:
        result.append(v + 1)  # Add 1 to the node index for 1-based indexing
    for i in range(len(graph)):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited, result)

# Step 1: Find SCCs using Kosaraju's algorithm
def kosaraju_scc(graph):
    n = len(graph)
    visited = [False] * n
    stack = []
    
    # Step 1.1: Perform DFS and push finished nodes to stack
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)
    
    # Step 1.2: Transpose the graph
    transpose = [[graph[j][i] for j in range(n)] for i in range(n)]
    
    # Step 1.3: Perform DFS on the transposed graph in reverse order of stack
    visited = [False] * n
    sccs = []
    
    while stack:
        node = stack.pop()
        if not visited[node - 1]:  # Adjust for 1-based indexing
            scc = []
            dfs(transpose, node - 1, visited, scc)  # Adjust for 1-based indexing
            sccs.append(scc)
    
    return sccs

# Step 2: Find WCCs using DFS
def find_wccs(graph):
    n = len(graph)
    visited = [False] * n
    wccs = []
    
    for i in range(n):
        if not visited[i]:
            wcc = []
            dfs(graph, i, visited, wcc)
            wccs.append(wcc)
    
    return wccs

# Find SCCs and WCCs
sccs = kosaraju_scc(G)
wccs = find_wccs(G)

# Output the results with 1-based indexing
print("Strongly Connected Components (SCCs):")
for idx, scc in enumerate(sccs):
    print(f"SCC {idx + 1}: {scc}")

print("\nWeakly Connected Components (WCCs):")
for idx, wcc in enumerate(wccs):
    print(f"WCC {idx + 1}: {wcc}")
