import pygame, math

from pygame.locals import *
from assets import Palette, draw_text, draw_graph, draw_button, draw_graph_result


class Game:
    WIDTH = 800
    HEIGHT = 600
    
    GAME_NAME = 'Jogo dos Grafos'
    INTRO_TEXT = 'Identifique\n os grafos bipartidos'
    
    running = True
    
    MENU = 1
    QUESTION = 2
    ANSWER = 3
    state = MENU

    CORRECT_ANSWER = 4
    WRONG_ANSWER = 5
    state_question = CORRECT_ANSWER
    
    graphs = []
    num_graph = 0

    def build_screen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.GAME_NAME)
        
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        
        self.clock = pygame.time.Clock()

    def print_menu(self, mouse_pos=(0, 0), click=False):
        self.screen.fill(Palette.COLOR_1)
        
        h_middle = self.WIDTH/2
        button_width = 200
        button_height = 50
        play_pos = ((h_middle),(400))
        quit_pos = ((h_middle),(500))
        play_color = Palette.COLOR_6
        quit_color = Palette.COLOR_4

        if is_inside_square(play_pos, button_height, button_width, mouse_pos):
            if click:
                play_color = Palette.COLOR_5
                self.state = self.QUESTION
            else:
                play_color = Palette.COLOR_8
        
        if is_inside_square(quit_pos, button_height, button_width, mouse_pos):
            if click:
                quit_color = Palette.COLOR_5
                self.running = False
            else:
                quit_color = Palette.COLOR_8
        
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
                
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    self.print_menu(mouse_pos=pos, click=False)
                
                if event.type == QUIT:
                    pygame.quit()
            
            pygame.display.update()
    
    def print_question(self, mouse_pos=(0, 0), click=False):
        self.screen.fill(Palette.COLOR_9)

        h_middle = self.WIDTH/2
        button_width = 200
        button_height = 50
        yes_pos = ((h_middle-120),(550))
        no_pos = ((h_middle+120),(550))
        yes_color = Palette.COLOR_6
        no_color = Palette.COLOR_4

        draw_text(game=self, text='Esse grafo é bipartido?', position=((h_middle),(40)), font_size=30, color=Palette.COLOR_10)
        draw_graph(game=self, graph=self.graphs[0])

        if is_inside_square(yes_pos, button_height, button_width, mouse_pos):
            if click:
                yes_color = Palette.COLOR_5
                self.state = self.ANSWER
                print(self.graphs[0].bipartite())
                if self.graphs[0].bipartite():
                    self.state_question = self.CORRECT_ANSWER
                else:
                    self.state_question = self.WRONG_ANSWER
            else:
                yes_color = Palette.COLOR_8
        
        if is_inside_square(no_pos, button_height, button_width, mouse_pos):
            if click:
                no_color = Palette.COLOR_5
                self.state = self.ANSWER
                if self.graphs[0].bipartite():
                    self.state_question = self.WRONG_ANSWER
                else:
                    self.state_question = self.CORRECT_ANSWER
            else:
                no_color = Palette.COLOR_8

        draw_button(game=self, position=yes_pos,  width=button_width, height=button_height, text='Sim', color=yes_color)
        draw_button(game=self, position=no_pos,  width=button_width, height=button_height, text='Não', color=no_color)

    def run_question(self):
        self.print_question()

        while self.running and self.state==self.QUESTION:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.print_question(mouse_pos=pos, click=True)
                
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    self.print_question(mouse_pos=pos, click=False)
                
                if event.type == QUIT:
                    pygame.quit()
            
            pygame.display.update()

    def print_answer(self, mouse_pos=(0, 0), click=False):
        self.screen.fill(Palette.COLOR_9)

        h_middle = self.WIDTH/2
        button_width = 200
        button_height = 50
        quit_pos = ((h_middle-120),(550))
        next_pos = ((h_middle+120),(550))
        quit_color = Palette.COLOR_4
        next_color = Palette.COLOR_6

        if self.state_question == self.CORRECT_ANSWER:
            draw_text(game=self, text='Resposta Correta!', position=((h_middle),(40)), font_size=30, color=Palette.COLOR_7)
        else:
            draw_text(game=self, text='Resposta Errada', position=((h_middle),(40)), font_size=30, color=Palette.COLOR_4)

        draw_graph_result(game=self, graph=self.graphs[0])
        
        if is_inside_square(quit_pos, button_height, button_width, mouse_pos):
            if click:
                self.quit_color = Palette.COLOR_5
                pygame.quit()
            else:
                quit_color = Palette.COLOR_8
            
        if is_inside_square(next_pos, button_height, button_width, mouse_pos):
            if click:
                self.next_color = Palette.COLOR_5
                self.state = self.QUESTION
                ## IR PARA PROXIMO GRAFO
            else:
                next_color = Palette.COLOR_8

        draw_button(game=self, position=quit_pos,  width=button_width, height=button_height, text='Sair', color=quit_color)
        draw_button(game=self, position=next_pos,  width=button_width, height=button_height, text='Próxima', color=next_color)

    def run_answer(self):
        self.print_answer()

        while self.running and self.state==self.ANSWER:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.print_answer(mouse_pos=pos, click=True)
                
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    self.print_answer(mouse_pos=pos, click=False)

                if event.type == QUIT:
                    pygame.quit()
            
            pygame.display.update()

    def run(self, graphs):
        pygame.init()
        self.build_screen()
        self.graphs = graphs
        
        while self.running:
            if self.state==self.MENU:
                self.run_menu()
            elif self.state==self.QUESTION:
                self.run_question()
            elif self.state==self.ANSWER:
                 self.run_answer()
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
