import pygame
from pygame.locals import *

class Palette:
    # Paleta de cores https://javier.xyz/cohesive-colors/
    # Primeira paleta
    COLOR_1 = (85, 94, 123)
    COLOR_2 = (183, 217, 104)
    COLOR_3 = (181, 118, 173)
    COLOR_4 = (224, 70, 68)
    COLOR_5 = (253, 228, 127)
    COLOR_6 = (124, 204, 229)

class Assets:
    def draw_node(self, game, position, color=Palette.COLOR_1):
        pygame.draw.circle(game.screen, Palette.COLOR_1, position, game.node_radius)

