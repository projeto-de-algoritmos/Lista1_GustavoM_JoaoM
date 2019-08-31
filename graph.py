import queue 
#Grafo não direcionado 
class Graph:
    def __init__(self, tam=0):
        self.tam=tam
        self.adj_list = []
        self.edges_list = set()
        self.position = []
        for _ in range(self.tam):
            self.adj_list.append(set())
            self.position.append((0, 0))

    def add_node(self):
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
        UNCOLORED = -1
        BLUE = 0
        RED = 1
        color = [UNCOLORED]*self.tam
        q = queue.Queue(maxsize=self.tam)
        for i in range(self.tam):
            if color[i]!=UNCOLORED:
                continue
            q.put(i)
            color[i]=BLUE
            while not q.empty():
                u = q.get()
                for v in self.adj_list[u]:
                    if color[v] == UNCOLORED:
                        color[v] = (color[u]+1)%2
                        q.put(v)
                    elif color[v] == color[u]:
                        return False
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