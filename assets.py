import pygame
import math
from pygame.locals import *

class Palette:
    # Paleta de cores https://javier.xyz/cohesive-colors/
    # Primeira paleta
    COLOR_1 = (85, 94, 123)
    COLOR_2 = (183, 217, 104)
    COLOR_3 = (181, 118, 173)
    COLOR_4 = (224, 70, 68)
    COLOR_5 = (253, 228, 127)
    COLOR_6 = (67, 91, 198)
    COLOR_7 = (104, 188, 39)
    COLOR_8 = (35, 150, 170)

class Assets:
    LINE_THICKNESS = 7
    NODE_RADIUS = 40
    def get_positions(self, tam):
        # Posições dos nós nos grafos de determinados tamanhos
        if tam==3:
            return [ (150, 150), (300, 450), (450, 150) ]
        elif tam==4:
            return [ (150, 150), (150, 450), (450, 150), (450, 450) ]
        else:
            return [(100, 100)]*tam

    def draw_graph(self, game, graph):
        game.circle_radius = graph.radius
        positions = self.get_positions(self, graph.tam)
        for i in range(graph.tam):
            if graph.color[i]==graph.UNCOLORED:
                self.draw_node(self, game, positions[i])
            elif graph.color[i]==graph.BLUE:
                self.draw_node(self, game, positions[i], color=Palette.COLOR_6)
            elif graph.color[i]==graph.GREEN:
                self.draw_node(self, game, positions[i], color=Palette.COLOR_7)
            elif graph.color[i]==graph.RED:
                self.draw_node(self, game, positions[i], color=Palette.COLOR_4)
            else:
                print(graph.color[i])
                
        for u, v in graph.edges_list:
             self.draw_edge(self, game, positions[u], positions[v])
            
    def draw_node(self, game, position, color=Palette.COLOR_8):
        pygame.draw.circle(game.screen, color, position, game.circle_radius)
        
    def draw_edge(self, game, pos1, pos2, color=Palette.COLOR_1):
        a = pos1[1]-pos2[1]
        b = pos2[0]-pos1[0]
        r = game.circle_radius
        theta = math.atan2(a, b)
        x1 = pos1[0]+math.cos(theta)*r
        y1 = pos1[1]-math.sin(theta)*r
        x2 = pos2[0]-math.cos(theta)*r
        y2 = pos2[1]+math.sin(theta)*r
        pygame.draw.line(game.screen, color, (x1, y1), (x2, y2), self.LINE_THICKNESS)

