import pygame
import math
from pygame.locals import *
from screens import Menu
from screens import Question
from screens import Answer
from screens import Info
from screens import CreateLevel
from screens import Finish

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

    # Game mods
    STANDARD = 1
    CUSTOM = 2

    running = True
    current_question = 0
    max_questions = 0
    game_mode = STANDARD
    corrects_ans = 0
    wrong_ans = 0

    current_graph = None
    current_screen = CreateLevel.ID
    state_question = CORRECT_ANSWER
    graphs = []
    standard_graphs = []
    custom_graphs = []

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
        self.add_screen(Finish)
        self.clock = pygame.time.Clock()

    def add_screen(self, Screen):
        self.screens.append(Screen(self))

    def run(self, graphs=[]):
        pygame.init()
        self.standard_graphs = graphs
        self.max_questions = len(graphs)
        while self.running:
            for screen in self.screens:
                if self.current_screen==screen.ID:
                    screen.run()
    def start_game(self, game_mode=STANDARD):
        self.current_question = 0
        self.wrong_ans = 0
        self.corrects_ans = 0
        if game_mode == self.CUSTOM:
            self.graphs = self.custom_graphs
        else:
            self.graphs = self.standard_graphs
        self.max_questions = len(self.graphs)
        self.change_screen(Question)

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
        self.current_question = self.current_question+1 
        if self.current_question>=self.max_questions:
            self.current_question = 0
            self.change_screen(Finish)
        else:
            self.change_screen(Question)
