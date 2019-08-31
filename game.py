import pygame
import math
from pygame.locals import *
from assets import Palette
from assets import Assets

class Game:
    WIDTH = 600
    HEIGHT = 600
    GAME_NAME = 'Bipartite graph game'
    running = True
    circle_radius = 40
    graphs = []
    def build_screen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(Palette.COLOR_5)
        pygame.display.set_caption(self.GAME_NAME)
        Assets.draw_graph(Assets, game=self, graph=self.graphs[0])
    
    def run(self, graphs):
        self.graphs = graphs
        pygame.init()
        self.build_screen()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            pygame.display.update()

