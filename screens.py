import pygame 
from pygame.locals import *
from assets import Button
from assets import Text
from assets import Graph
from assets import Palette

class Menu:
    def __init__(self, game):
        self.game = game
        self.x_middle = game.WIDTH/2
        self.y_middle = game.HEIGHT/2
        #Assets
        self.play_button = Button(screen=game.screen, position=((self.x_middle), (game.HEIGHT-200)),  on_press=lambda:game.change_screen(self.game.QUESTION), text='Jogar')
        self.quit_button = Button(screen=game.screen, position=((self.x_middle), (game.HEIGHT-100)),  on_press=game.quit_game, text='Sair', color=Palette.RED)
        self.title = Text(screen=self.game.screen, position=((self.x_middle),(100)), text=self.game.GAME_NAME, font_size=60)
        self.sub_title = Text(screen=self.game.screen, position=((self.x_middle),(180)), text=self.game.INTRO_TEXT, font_size=24, font_color=Palette.COLOR_5)

    def draw(self):
        self.game.screen.fill(Palette.COLOR_1)
        self.title.draw()
        self.sub_title.draw()
        self.play_button.draw()
        self.quit_button.draw()

    def run(self):
        while self.game.running and self.game.current_screen==self.game.MENU:
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
        #Assets
        self.yes_button = Button(screen=self.game.screen, position=((self.x_middle-120), (self.game.HEIGHT-80)), on_press=lambda:self.game.answer_question(True), text='Sim', color=Palette.BLUE)
        self.no_button = Button(screen=self.game.screen, position=((self.x_middle+120), (self.game.HEIGHT-80)), on_press=lambda:self.game.answer_question(False), text='Não', color=Palette.RED)
        self.question = Text(screen=self.game.screen, text='Esse grafo é bipartido?' ,position=((self.x_middle),(60)), font_size=30, font_color=Palette.COLOR_10)
        self.question_number = Text(screen=self.game.screen, text='( 1/2 )', position=((self.x_middle),(30)), font_size=20, font_color=Palette.COLOR_10)
        self.graph = Graph(game=self.game, reveal=False)

    def update_question(self):
        self.graph.set_graph(self.game.current_graph)
        text = '( {}/{} )'.format(self.game.current_question+1, self.game.max_questions)
        self.question_number.text = text

    def draw(self):        
        self.game.screen.fill(Palette.COLOR_9)
        self.update_question()
        self.question_number.draw()
        self.question.draw()
        self.graph.draw()
        self.yes_button.draw()
        self.no_button.draw()

    def run(self):
        self.game.current_graph = self.game.graphs[self.game.current_question]
        while self.game.running and self.game.current_screen==self.game.QUESTION:
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
        #Assets
        self.quit_button = Button(screen=self.game.screen, position=((self.x_middle-120), (self.game.HEIGHT-80)), on_press=lambda:game.change_screen(self.game.MENU), text='Voltar para o menu', color=Palette.RED)
        self.next_button = Button(screen=self.game.screen, position=((self.x_middle+120), (self.game.HEIGHT-80)), on_press=self.game.next_question, text='Próxima pergunta', color=Palette.BLUE)
        self.answer = Text(screen=self.game.screen, position=((self.x_middle),(60)), font_size=30)
        self.graph = Graph(game=self.game, reveal=True)
    
    def update_ans(self):
        self.graph.set_graph(self.game.current_graph)
        if self.game.state_question == self.game.CORRECT_ANSWER:
            self.answer.text = 'Resposta Correta!'
            self.answer.font_color = Palette.GREEN
        else:
            self.answer.text = 'Resposta Errada'
            self.answer.font_color = Palette.RED
            
    def draw(self):
        self.game.screen.fill(Palette.COLOR_9)
        self.update_ans()
        self.answer.draw()
        self.graph.draw()
        self.quit_button.draw()
        self.next_button.draw()

    def run(self):
        while self.game.running and self.game.current_screen==self.game.ANSWER:
            for event in pygame.event.get():
                self.next_button.get_event(event, pygame.mouse.get_pos())
                self.quit_button.get_event(event, pygame.mouse.get_pos())              
                if event.type == QUIT:
                    self.game.quit_game()
            self.draw()
            pygame.display.update()
