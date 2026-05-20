from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        cc = [v]
        for i in self.graph[v]:
            if not visited[i]:
                cc += self.DFS(i, visited)
        return cc

    def connected_components(self):
        visited = [False] * self.V
        cc = []
        for v in range(self.V):
            if not visited[v]:
                cc.append(self.DFS(v, visited))
        return cc

# Create a sample graph representing the social network
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 4)

connected_components = g.connected_components()
print("Connected Components:", connected_components)
