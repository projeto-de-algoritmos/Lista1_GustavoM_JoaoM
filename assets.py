import pygame 
import random
import math
import graph
from pygame.locals import *

class Palette:
    # Paleta de cores https://javier.xyz/cohesive-colors/
    # Primeira paleta
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (224, 70, 68)
    BLUE = (67, 91, 198)
    GREEN = (104, 188, 39)
    COLOR_1 = (85, 94, 123)
    COLOR_2 = (183, 217, 104)
    COLOR_3 = (181, 118, 173) 
    COLOR_5 = (253, 228, 127)
    COLOR_8 = (35, 150, 170)

    # Cores Adicionais
    COLOR_9 = (238, 238, 238)
    COLOR_10 = (38, 50, 56)
    COLOR_11 = (117, 117, 117)
    COLOR_12 = (66, 66, 66)


class Timer:
    def __init__(self, surface, color, rect, start_angle, stop_angle, width, on_finished=lambda:None):
        self.screen = surface
        self.color = color
        self.rect = rect
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.width = width
        self.on_finished = on_finished

    def timer_run(self, seconds):
        to_timer = 5 - seconds
        if to_timer < 0:
            self.on_finished()
        pygame.draw.arc(self.screen, self.color, self.rect, self.start_angle, self.stop_angle - 1.256*seconds, self.width)

class Button:
    def __init__(self, screen, position, on_press=lambda:None, 
        on_focus=lambda:None, text='', font_size=30, 
        width=200, height=50, color=Palette.BLUE, font_color=Palette.WHITE, 
        focused_color=Palette.COLOR_8, press_color=Palette.COLOR_5,
        icon=None):
        self.icon = icon
        self.screen = screen
        self.center = position
        self.on_press = on_press
        self.on_focus = on_focus
        self.width = width
        self.height = height
        self.color = color
        self.focused_color = focused_color
        self.press_color = press_color
        self.pressed = False
        self.focused = False
        self.text = Text(screen=self.screen, text=text, position=self.center, font_size=font_size, font_color=font_color)

    def get_event(self, event, mouse_pos):
        mouse_pos = mouse_pos
        x1 = self.center[0]-self.width/2
        y1 = self.center[1]-self.height/2
        x2 = self.center[0]+self.width/2
        y2 = self.center[1]+self.height/2
        if mouse_pos[0]>=x1 and mouse_pos[0]<=x2 and mouse_pos[1]>=y1 and mouse_pos[1]<=y2:
            self.focused = True
        else:
            self.focused = False
            return    
        if self.focused and event.type == pygame.MOUSEBUTTONUP:
            self.pressed = True
            self.on_press()
        else:
            self.pressed = False
            if self.focused:
                self.on_focus()

    def draw(self, event=None):
        b_color = self.color
        if self.focused and self.pressed:
            b_color = self.press_color
        elif self.focused:
            b_color = self.focused_color            
        x1 = self.center[0]-self.width/2
        y1 = self.center[1]-self.height/2
        pygame.draw.rect(self.screen, b_color, (x1,y1, self.width, self.height))
        if self.icon:
            self.icon = pygame.transform.scale(self.icon, (30, 30))
            rect = self.icon.get_rect()
            rect.center = (x1+20, self.center[1])
            self.screen.blit(self.icon, rect)
            self.text.center = (self.center[0]+20, self.center[1])
        self.text.draw()

class Text:
    def __init__(self, screen, position, text='', font_size=30, font_color=Palette.WHITE, font_type='freesansbold.ttf', padding=5):
        self.screen = screen
        self.text = text
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.padding = padding
        self.center = (position)

    def draw(self):
        lines = self.text.split('\n')
        n = len(lines)
        y_pos = self.center[1]-( max(0, n//2-1)*self.padding + max(0, n//2-1)*self.font_size )
        if n!=1 and n%2==1:
            y_pos -= int(self.padding/2+self.font_size/2)
        x_pos = self.center[0]
        self.style = pygame.font.SysFont(self.font_type, self.font_size)
        for line in lines:
            text_surf = self.style.render(line, True, self.font_color)
            text_rect = text_surf.get_rect()
            text_rect.center = (x_pos, y_pos)
            self.screen.blit(text_surf, text_rect)
            y_pos+=self.font_size+self.padding


class Graph:
    def __init__(self, game, graph=graph.Graph(), reveal=False, circle_radius=40, line_thickness=7):
        self.graph = graph
        self.game = game
        self.circle_radius = circle_radius
        self.line_thickness = line_thickness
        self.reveal = reveal
        self.positions = get_positions(self.graph.tam, self.game.WIDTH, self.game.HEIGHT)
    
    def set_graph(self, graph):
        self.graph = graph
        self.positions = get_positions(self.graph.tam, self.game.WIDTH, self.game.HEIGHT)

    def draw_node(self, i, color=Palette.COLOR_11):
        pygame.draw.circle(self.game.screen, color, self.positions[i], self.circle_radius)
    
    def draw_edge(self, u, v, color=Palette.COLOR_12):
        pos1 = self.positions[u]
        pos2 = self.positions[v]
        a = pos1[1]-pos2[1]
        b = pos2[0]-pos1[0]
        theta = math.atan2(a, b)
        x1 = pos1[0]+math.cos(theta)*self.circle_radius
        y1 = pos1[1]-math.sin(theta)*self.circle_radius
        x2 = pos2[0]-math.cos(theta)*self.circle_radius
        y2 = pos2[1]+math.sin(theta)*self.circle_radius
        pygame.draw.line(self.game.screen, color, (x1, y1), (x2, y2), self.line_thickness)

    def draw(self):
        for i in range(self.graph.tam):
            if not self.reveal:
                self.draw_node(i=i)
            elif self.graph.color[i]==self.graph.BLUE:
                self.draw_node(i=i, color=Palette.BLUE)
            elif self.graph.color[i]==self.graph.GREEN:
                self.draw_node(i=i, color=Palette.GREEN)
            elif self.graph.color[i]==self.graph.RED:
                self.draw_node(i=i, color=Palette.RED)
        for u, v in self.graph.edges_list:
            self.draw_edge(u, v)


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

#
#
# Funções descontinuadas 
#
#
# LINE_THICKNESS = 7
# def draw_graph_result(game, graph):
#     positions = get_positions(graph.tam, game.WIDTH, game.HEIGHT)    
#     for i in range(graph.tam):
#         if graph.color[i]==graph.UNCOLORED:
#             draw_node(game, positions[i])
#         elif graph.color[i]==graph.BLUE:
#             draw_node(game, positions[i], color=Palette.BLUE)
#         elif graph.color[i]==graph.GREEN:
#             draw_node(game, positions[i], color=Palette.GREEN)
#         elif graph.color[i]==graph.RED:
#             draw_node(game, positions[i], color=Palette.RED)
#         else:
#             print(graph.color[i])
            
#     for u, v in graph.edges_list:
#         draw_edge(game, positions[u], positions[v])
        
# def draw_graph(game, graph):
#     positions = get_positions(graph.tam, game.WIDTH, game.HEIGHT)
#     for i in range(graph.tam):
#         draw_node(game, positions[i], color=Palette.COLOR_11)

#     for u, v in graph.edges_list:
#         draw_edge(game, positions[u], positions[v])

# def draw_node(game, position, color=Palette.COLOR_8):
#     pygame.draw.circle(game.screen, color, position, game.circle_radius)
    
# def draw_edge(game, pos1, pos2, color=Palette.COLOR_12):
#     a = pos1[1]-pos2[1]
#     b = pos2[0]-pos1[0]
#     r = game.circle_radius
#     theta = math.atan2(a, b)
#     x1 = pos1[0]+math.cos(theta)*r
#     y1 = pos1[1]-math.sin(theta)*r
#     x2 = pos2[0]-math.cos(theta)*r
#     y2 = pos2[1]+math.sin(theta)*r
#     pygame.draw.line(game.screen, color, (x1, y1), (x2, y2), LINE_THICKNESS)

# def draw_text(screen, text, position, font_size=12, color=Palette.WHITE ):
#     txt = pygame.font.Font('freesansbold.ttf',font_size)
#     TextSurf = txt.render(text, True, color)
#     TextRect = TextSurf.get_rect()
#     TextRect.center = (position)
#     screen.blit(TextSurf, TextRect)

# def draw_button(game, position, text='', font_size=20, width=200, height=50, color=Palette.BLUE, font_color=Palette.WHITE):
#     x1 = position[0]-width/2
#     y1 = position[1]-height/2
#     x2 = width
#     y2 = height
#     pygame.draw.rect(game.screen, color,(x1,y1,x2,y2))
#     draw_text(game.screen, text, position, font_size, font_color)