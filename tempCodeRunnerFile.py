from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Adjacency list representation

    # Add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u-1].append(v-1)  # Adjust for 1-based indexing

    # BFS utility for SCC and WCC
    def BFSUtil(self, start, visited, scc=None):
        queue = deque([start])  # Queue for BFS
        visited[start] = True
        if scc is not None:  # For SCC
            scc.append(start+1)  # Convert back to 1-based indexing
        while queue:
            node = queue.popleft()  # Dequeue the node
            for i in self.graph[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    if scc is not None:  # For SCC
                        scc.append(i+1)  # Convert back to 1-based indexing

    # Transpose the graph (reverse the directions of all edges)
    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j+1, i+1)  # Adjust for 1-based indexing
        return g

    # Find SCCs using BFS (Kosaraju's algorithm with BFS)
    def findSCCs(self):
        visited = [False] * self.V
        stack = []

        # First BFS loop to fill the stack
        for i in range(self.V):
            if not visited[i]:
                self.BFSUtil(i, visited, scc=None)
                stack.append(i)

        # Transpose the graph
        gr = self.getTranspose()

        # Second BFS loop to get SCCs
        visited = [False] * self.V
        sccs = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                scc = []
                gr.BFSUtil(node, visited, scc=scc)
                sccs.append(scc)
        return sccs

    # Find WCCs by ignoring direction (treating as undirected)
    def findWCCs(self):
        visited = [False] * self.V
        wccs = []

        # Create an undirected version of the graph
        undirected_graph = defaultdict(list)
        for i in self.graph:
            for j in self.graph[i]:
                undirected_graph[i].append(j)
                undirected_graph[j].append(i)

        # BFS for weakly connected components
        for i in range(self.V):
            if not visited[i]:
                wcc = []
                self.BFSUtil(i, visited, scc=wcc)
                wccs.append(wcc)
        return wccs

# Driver code
if __name__ == "__main__":
    # Create the graph with 9 vertices (1-based indexing)
    g = Graph(9)

    # Add the edges (converted to 1-based indexing)
    edges = [
        (1, 2), (1, 4), (2, 3), (2, 6), (6, 4), (6, 3),
        (7, 3), (5, 4), (5, 5), (5, 9), (7, 6), (7, 8),
        (7, 5), (8, 3), (8, 9)
    ]
    for u, v in edges:
        g.addEdge(u, v)

    # Find SCCs
    sccs = g.findSCCs()
    print("Number of Strongly Connected Components:", len(sccs))
    print("Strongly Connected Components:")
    for i, scc in enumerate(sccs, start=1):
        print(f"SCC {i}: {scc}")

    # Find WCCs
    wccs = g.findWCCs()
    print("Number of Weakly Connected Components:", len(wccs))
    print("Weakly Connected Components:", wccs)
