import pygame, random
import math

from pygame.locals import *


class Palette:
    # Paleta de cores https://javier.xyz/cohesive-colors/
    # Primeira paleta
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    COLOR_1 = (85, 94, 123)
    COLOR_2 = (183, 217, 104)
    COLOR_3 = (181, 118, 173)
    COLOR_4 = (224, 70, 68)
    COLOR_5 = (253, 228, 127)
    COLOR_6 = (67, 91, 198)
    COLOR_7 = (104, 188, 39)
    COLOR_8 = (35, 150, 170)

    # Cores Adicionais
    COLOR_9 = (238, 238, 238)
    COLOR_10 = (38, 50, 56)
    COLOR_11 = (117, 117, 117)
    COLOR_12 = (66, 66, 66)


LINE_THICKNESS = 7
NODE_RADIUS = 40


def get_positions(tam, screen_width, screen_heigth):
    # Posições dos nós de acordo com o tamanho dos grafos

    x_mid = screen_width//2 
    y_mid = screen_heigth//2

    if tam==1:
        return [(x_mid, y_mid)]
    elif tam==2:
        return [(x_mid-100, y_mid), (x_mid+100, y_mid)]
    elif tam==3:
        return [(x_mid, y_mid+50), (x_mid-100, y_mid-50), (x_mid+100, y_mid-50)]
    elif tam==4:
        return [(x_mid, y_mid+100), (x_mid-100, y_mid), (x_mid, y_mid-100), (x_mid+100, y_mid)]
    elif tam==5:
        return [(x_mid, y_mid-150), (x_mid-150, y_mid-50), (x_mid-150, y_mid+150), (x_mid+150, y_mid+150), (x_mid+150, y_mid-50)]
    elif tam==6:
        return [(x_mid-100, y_mid-150), (x_mid-200, y_mid), (x_mid-100, y_mid+150), (x_mid+100, y_mid+150), (x_mid+200, y_mid), (x_mid+100, y_mid-150)]
    elif tam==7:
        return [(x_mid, y_mid-180), (x_mid-100, y_mid-90), (x_mid-200, y_mid), (x_mid-100, y_mid+120), (x_mid+100, y_mid+120), (x_mid+200, y_mid), (x_mid+100, y_mid-90)]
    elif tam==8:
        return [(x_mid, y_mid-180), (x_mid-150, y_mid-90), (x_mid-250, y_mid), (x_mid-150, y_mid+90), (x_mid, y_mid+180), (x_mid+150, y_mid+90), (x_mid+250, y_mid), (x_mid+150, y_mid-90)]



def draw_text(game, text, position, font_size=12, color=Palette.WHITE ):
    txt = pygame.font.Font('freesansbold.ttf',font_size)
    TextSurf = txt.render(text, True, color)
    TextRect = TextSurf.get_rect()
    TextRect.center = (position)
    game.screen.blit(TextSurf, TextRect)

def draw_button(game, position, text='', font_size=20, width=200, height=50, color=Palette.COLOR_6, font_color=Palette.WHITE):
    x1 = position[0]-width/2
    y1 = position[1]-height/2
    x2 = width
    y2 = height
    pygame.draw.rect(game.screen, color,(x1,y1,x2,y2))
    draw_text(game, text, position, font_size, font_color)

def draw_graph_result(game, graph):
    game.circle_radius = graph.radius
    positions = get_positions(graph.tam, game.WIDTH, game.HEIGHT)    
    for i in range(graph.tam):
        if graph.color[i]==graph.UNCOLORED:
            draw_node(game, positions[i])
        elif graph.color[i]==graph.BLUE:
            draw_node(game, positions[i], color=Palette.COLOR_6)
        elif graph.color[i]==graph.GREEN:
            draw_node(game, positions[i], color=Palette.COLOR_7)
        elif graph.color[i]==graph.RED:
            draw_node(game, positions[i], color=Palette.COLOR_4)
        else:
            print(graph.color[i])
            
    for u, v in graph.edges_list:
            draw_edge(game, positions[u], positions[v])
        
def draw_graph(game, graph):
    game.circle_radius = graph.radius
    positions = get_positions(graph.tam, game.WIDTH, game.HEIGHT)
    for i in range(graph.tam):
        draw_node(game, positions[i], color=Palette.COLOR_11)

    for u, v in graph.edges_list:
        draw_edge(game, positions[u], positions[v])

def draw_node(game, position, color=Palette.COLOR_8):
    pygame.draw.circle(game.screen, color, position, game.circle_radius)
    
def draw_edge(game, pos1, pos2, color=Palette.COLOR_12):
    a = pos1[1]-pos2[1]
    b = pos2[0]-pos1[0]
    r = game.circle_radius
    theta = math.atan2(a, b)
    x1 = pos1[0]+math.cos(theta)*r
    y1 = pos1[1]-math.sin(theta)*r
    x2 = pos2[0]-math.cos(theta)*r
    y2 = pos2[1]+math.sin(theta)*r
    pygame.draw.line(game.screen, color, (x1, y1), (x2, y2), LINE_THICKNESS)
