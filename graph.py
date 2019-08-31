import queue 

#Grafo não direcionado 
class Graph:
    def __init__(self, tam=0):
        self.tam=tam
        self.adj_list = []
        for _ in range(self.tam):
            self.adj_list.append(set())

    def add_edge(self):
        self.adj_list.append(set())

    def connect(self, i, j):
        if i>self.tam or i<=0:
            raise Exception('O valor {} é inválido'.format(i))
        if j>self.tam or j<=0:
            raise Exception('O valor {} é inválido'.format(j))
        self.adj_list[j-1].add(i-1)
        self.adj_list[i-1].add(j-1)
    
    def unconnect(self, i, j):
        if i>self.tam or i<=0:
            raise Exception('O valor {} é inválido'.format(i))
        if j>self.tam or j<=0:
            raise Exception('O valor {} é inválido'.format(j))
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



            