import queue 


# Grafo não direcionado 
class Graph:
    UNCOLORED = -1
    BLUE = 0
    GREEN = 1
    RED = -2
    def __init__(self, tam=0):
        self.tam=tam
        self.edges_list = set()
        self.color = [self.UNCOLORED]*self.tam
        self.visited = [False]*self.tam
        self.adj_list = []
        for _ in range(self.tam):
            self.adj_list.append(set())

    def connect(self, i, j):
        if i>self.tam or i<=0:
            raise Exception('O valor {} é inválido'.format(i))
        if j>self.tam or j<=0:
            raise Exception('O valor {} é inválido'.format(j))
        self.edges_list.add((j-1, i-1))
        self.adj_list[j-1].add(i-1)
        self.adj_list[i-1].add(j-1)
    
    def unconnect(self, i, j):
        if i>self.tam or i<=0:
            raise Exception('O valor {} é inválido'.format(i))
        if j>self.tam or j<=0:
            raise Exception('O valor {} é inválido'.format(j))
        self.edges_list.remove((j-1, i-1))
        self.adj_list[j-1].remove(i-1)
        self.adj_list[i-1].remove(j-1)

    def bipartite(self):
        self.reset_graph()
        q = queue.Queue(maxsize=self.tam)
        ans = True
        for i in range(self.tam):
            if self.color[i]!=self.UNCOLORED:
                continue
            q.put(i)
            self.color[i]=self.BLUE
            while not q.empty():
                u = q.get()
                self.visited[u] = True
                for v in self.adj_list[u]:
                    self.tint_node(u, v)
                    if self.color[v] == self.color[u]:
                        ans = False
                    if not self.visited[v]:
                        q.put(v)
        return ans

    def reset_graph(self):
        self.color = [self.UNCOLORED]*self.tam
        self.visited = [False]*self.tam

    def tint_node(self, u, v):
        if self.color[v] == self.UNCOLORED:
            self.color[v] = (self.color[u]+1)%2
        elif self.color[v] == self.color[u]:
            self.color[v] = self.RED
            self.color[u] = self.RED

        return True

def read_graphs(path):
    file = open(path)
    contents  = file.read().split('$')[1:-1]
    graphs = []

    for content in contents:
        lines = content.split('\n')[1:-1]
        tam, n = map(int, lines[0].split())
        graph = Graph(tam)
        for i in range(n):
            u, v = map(int, lines[i+1].split())
            graph.connect(u, v)
        graphs.append(graph)
    return graphs