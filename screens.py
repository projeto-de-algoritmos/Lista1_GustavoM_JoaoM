import pygame 
from pygame.locals import *
from assets import Button
from assets import Palette
from assets import draw_text
from assets import draw_graph
from assets import draw_graph_result

class Menu:
    def __init__(self, game):
        self.game = game
        self.x_middle = game.WIDTH/2
        self.y_middle = game.HEIGHT/2
        self.play_button = Button(screen=game.screen, position=((self.x_middle), (game.HEIGHT-200)),  on_press=game.start_game, text='Jogar')
        self.quit_button = Button(screen=game.screen, position=((self.x_middle), (game.HEIGHT-100)),  on_press=game.quit_game, text='Sair', color=Palette.RED)

    def draw(self):
        self.game.screen.fill(Palette.COLOR_1)
        draw_text(screen=self.game.screen, text=self.game.GAME_NAME, position=((self.x_middle),(100)), font_size=60)
        lines = self.game.INTRO_TEXT.split('\n')
        for i in range(len(lines)):
            draw_text(screen=self.game.screen, text=lines[i], position=((self.x_middle),(180+30*i)), font_size=24, color=Palette.COLOR_5)
        self.play_button.draw()
        self.quit_button.draw()

    def run(self):
        while self.game.running and self.game.state==self.game.MENU:
            for event in pygame.event.get():
                self.play_button.get_event(event, pygame.mouse.get_pos())
                self.quit_button.get_event(event, pygame.mouse.get_pos())              
                if event.type == QUIT:
                    self.game.quit_game()
            self.draw()
            pygame.display.update()

class Question:
    def __init__(self, game):
        self.game = game
        self.x_middle = game.WIDTH/2
        self.y_middle = game.HEIGHT/2
        self.yes_button = Button(screen=self.game.screen, position=((self.x_middle-120), (self.game.HEIGHT-80)), on_press=lambda:self.game.answer_question(True), text='Sim', color=Palette.BLUE)
        self.no_button = Button(screen=self.game.screen, position=((self.x_middle+120), (self.game.HEIGHT-80)), on_press=lambda:self.game.answer_question(False), text='Não', color=Palette.RED)

    def draw(self):
        self.game.screen.fill(Palette.COLOR_9)
        draw_text(screen=self.game.screen, text='Esse grafo é bipartido?', position=((self.x_middle),(40)), font_size=30, color=Palette.COLOR_10)
        draw_graph(game=self.game, graph=self.game.current_graph)
        self.yes_button.draw()
        self.no_button.draw()

    def run(self):
        self.game.current_graph = self.game.graphs[self.game.current_question]
        while self.game.running and self.game.state==self.game.QUESTION:
            for event in pygame.event.get():
                self.yes_button.get_event(event, pygame.mouse.get_pos())
                self.no_button.get_event(event, pygame.mouse.get_pos())              
                if event.type == QUIT:
                    self.game.quit_game()
            self.draw()
            pygame.display.update()

class Answer:
    def __init__(self, game):
        self.game = game
        self.x_middle = game.WIDTH/2
        self.y_middle = game.HEIGHT/2
        self.quit_button = Button(screen=self.game.screen, position=((self.x_middle-120), (self.game.HEIGHT-80)), on_press=self.game.quit_game, text='Sair', color=Palette.RED)
        self.next_button = Button(screen=self.game.screen, position=((self.x_middle+120), (self.game.HEIGHT-80)), on_press=self.game.next_question, text='Próxima pergunta', color=Palette.BLUE)

    def draw(self):
        self.game.screen.fill(Palette.COLOR_9)
        if self.game.state_question == self.game.CORRECT_ANSWER:
            draw_text(screen=self.game.screen, text='Resposta Correta!', position=((self.x_middle),(40)), font_size=30, color=Palette.COLOR_7)
        else:
            draw_text(screen=self.game.screen, text='Resposta Errada', position=((self.x_middle),(40)), font_size=30, color=Palette.RED)

        draw_graph_result(game=self.game, graph=self.game.current_graph)
        self.quit_button.draw()
        self.next_button.draw()

    def run(self):
        while self.game.running and self.game.state==self.game.ANSWER:
            for event in pygame.event.get():
                self.next_button.get_event(event, pygame.mouse.get_pos())
                self.quit_button.get_event(event, pygame.mouse.get_pos())              
                if event.type == QUIT:
                    self.game.quit_game()
            self.draw()
            pygame.display.update()
