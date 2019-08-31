from graph import Graph

a = Graph(5)
a.connect(1, 2)
a.connect(2, 3)
a.connect(1, 4)
print(a.bipartite())
print(a.adj_list)
