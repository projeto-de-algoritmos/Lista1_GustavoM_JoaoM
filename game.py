import pygame
import math
from pygame.locals import *
from assets import Palette
from assets import draw_text
from assets import draw_graph
from assets import draw_button




class Game:
    WIDTH = 800
    HEIGHT = 600
    GAME_NAME = 'Bipartite graph game'
    INTRO_TEXT = 'Jogo de perguntas e respostas\n para identificação de grafos bipartidos'
    running = True
    MENU = 1
    GAME = 2
    state = MENU
    circle_radius = 40
    graphs = []
    def build_screen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(Palette.COLOR_5)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.GAME_NAME)
    
    def print_graph(self, graph):
        self.clock.tick(15)
        #graph.bipartite()
        self.screen.fill(Palette.COLOR_5)
        draw_graph(game=self, graph=graph)

    def print_menu(self, mouse_pos=(0, 0), click=False):
        h_middle = self.WIDTH/2
        button_height = 50
        button_width = 200
        play_pos = ((h_middle),(400))
        quit_pos = ((h_middle),(500))
        quit_color = Palette.COLOR_4
        play_color = Palette.COLOR_6
        if is_inside_square(play_pos, button_height, button_width, mouse_pos):
            if click:
                play_color = Palette.COLOR_5
                self.state = self.GAME
            else:
                play_color = Palette.COLOR_8
        if is_inside_square(quit_pos, button_height, button_width, mouse_pos):
            if click:
                quit_color = Palette.COLOR_5
                self.running = False
            else:
                quit_color = Palette.COLOR_8
        #self.clock.tick(15)
        self.screen.fill(Palette.COLOR_1)
        draw_text(game=self, text=self.GAME_NAME, position=((h_middle),(100)), font_size=60)
        lines = self.INTRO_TEXT.split('\n')
        for i in range(len(lines)):
            draw_text(game=self, text=lines[i], position=((h_middle),(180+30*i)), font_size=24, color=Palette.COLOR_5)
        draw_button(game=self, position=play_pos,  width=button_width, height=button_height, text='Jogar', color=play_color)
        draw_button(game=self, position=quit_pos,  width=button_width, height=button_height, text='Sair', color=quit_color)

    def run_menu(self):
        self.print_menu()
        while self.running and self.state==self.MENU:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.print_menu(mouse_pos=pos, click=True)
                    #print('click', pos)
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    self.print_menu(mouse_pos=pos, click=False)
                    #print('motion', pos)
                if event.type == QUIT:
                    pygame.quit()
            
            pygame.display.update()
    
    def run_game(self):
        while self.running and self.state==self.GAME:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            self.print_graph(self.graphs[0])
            pygame.display.update()

    def run(self, graphs):
        pygame.init()
        self.graphs = graphs
        self.build_screen()
        while self.running:
            if self.state==self.MENU:
                self.run_menu()
            elif self.state==self.GAME:
                self.run_game()
            else:
                print(self.state)
        
        

def is_inside_square(center, height, width, pos):
    x1 = center[0]-width/2
    y1 = center[1]-height/2
    x2 = center[0]+width/2
    y2 = center[1]+height/2

    if pos[0]>=x1 and pos[0]<=x2 and pos[1]>=y1 and pos[1]<=y2:
        return True
    return False