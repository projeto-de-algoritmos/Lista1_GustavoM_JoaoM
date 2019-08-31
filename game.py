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
    def build_screen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(Palette.COLOR_5)
        pygame.display.set_caption(self.GAME_NAME)
        self.drawEdge((100, 100), self.circle_radius)
        self.drawEdge((200, 200), self.circle_radius)
        self.drawConnection((100, 100), (200, 200))
    def drawEdge(self, pos, radius):
        pygame.draw.circle(self.screen, Palette.COLOR_1, pos, radius)
    def drawConnection(self, pos1, pos2):
        a = pos1[1]-pos2[1]
        b = pos2[0]-pos1[0]
        theta = math.atan(a/b)
        x1 = pos1[0]+math.cos(theta)*self.circle_radius
        y1 = pos1[1]-math.sin(theta)*self.circle_radius
        x2 = pos2[0]-math.cos(theta)*self.circle_radius
        y2 = pos2[1]+math.sin(theta)*self.circle_radius
        pygame.draw.line(self.screen,Palette.COLOR_4, (x1, y1), (x2, y2), 7)
    
    def run(self):
        pygame.init()
        self.build_screen()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            pygame.display.update()

