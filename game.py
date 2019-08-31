import pygame
import math
from pygame.locals import *
from assets import Palette
from assets import draw_text
from assets import draw_graph




class Game:
    WIDTH = 800
    HEIGHT = 600
    GAME_NAME = 'Bipartite graph game'
    running = True
    circle_radius = 40
    graphs = []
    def build_screen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(Palette.COLOR_5)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.GAME_NAME)
    
    def print_graph(self, graph):
        self.clock.tick(15)
        graph.bipartite()
        draw_graph(game=self, graph=graph)

    def print_menu(self):
        self.clock.tick(15)
        self.screen.fill(Palette.COLOR_1)
        draw_text(game=self, text='Bipartite graph game', position=((self.WIDTH/2),(100)), font_size=60)

        pygame.draw.rect(self.screen, Palette.COLOR_6,(150,450,100,50))
        pygame.draw.rect(self.screen, Palette.COLOR_8,(550,450,100,50))
        
    def run(self, graphs):
        self.graphs = graphs
        pygame.init()
        self.build_screen()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            self.print_menu()
            pygame.display.update()

