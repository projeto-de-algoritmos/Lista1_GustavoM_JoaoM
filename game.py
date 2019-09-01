import pygame
import math
from pygame.locals import *
from screens import Menu
from screens import Question
from screens import Answer
from screens import Info
from screens import CreateLevel

class Game:
    # Game constants
    WIDTH = 1024
    HEIGHT = 768
    GAME_NAME = 'Jogo dos Grafos'
    INTRO_TEXT = 'Identifique\n os grafos bipartidos'

    #Question state
    CORRECT_ANSWER = 1
    WRONG_ANSWER = 2
    TIMES_UP = 3

    running = True
    current_question = 0
    max_questions = 0

    corrects_ans = 0
    wrong_ans = 0

    current_graph = None
    current_screen = Menu.ID
    state_question = CORRECT_ANSWER
    graphs = []
    num_graph = 0

    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.menu_screen = Menu(self)
        self.question_screen = Question(self)
        self.answer_screen = Answer(self)
        pygame.display.set_caption(self.GAME_NAME)
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        self.screens = []
        self.add_screen(Menu)
        self.add_screen(Question)
        self.add_screen(Answer)
        self.add_screen(Info)
        self.add_screen(CreateLevel)
        self.clock = pygame.time.Clock()

    def add_screen(self, Screen):
        self.screens.append(Screen(self))

    def run(self, graphs):
        pygame.init()
        self.graphs = graphs
        self.max_questions = len(graphs)
        while self.running:
            for screen in self.screens:
                if self.current_screen==screen.ID:
                    screen.run()
    def quit_game(self):
        self.running = False

    def change_screen(self, screen):
        self.current_screen = screen.ID
    
    def answer_question(self, ans):
        if self.current_graph.bipartite() == ans:
            self.corrects_ans+=1
            self.state_question = self.CORRECT_ANSWER
        else:
            self.wrong_ans+=1
            self.state_question = self.WRONG_ANSWER
        self.change_screen(Answer)

    def no_answer_question(self):
        self.current_graph.bipartite()
        self.state_question = self.TIMES_UP
        self.change_screen(Answer)

    def next_question(self):
        self.current_question = (self.current_question+1)%self.max_questions #cicle
        self.change_screen(Question)
