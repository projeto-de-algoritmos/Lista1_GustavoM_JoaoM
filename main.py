from game import Game
from graph import Graph
from graph import read_graphs

graphs = read_graphs('graphs.txt')
for graph in graphs:
    print(graph.adj_list)

g = Game()
g.run()
