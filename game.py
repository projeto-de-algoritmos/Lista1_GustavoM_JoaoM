import pygame
import math
from pygame.locals import *
from screens import Menu
from screens import Question
from screens import Answer
from assets import Palette
from assets import Button
from assets import draw_text 
from assets import draw_graph 
from assets import draw_button 
from assets import draw_graph_result 

class Game:
    WIDTH = 800
    HEIGHT = 600
    GAME_NAME = 'Jogo dos Grafos'
    INTRO_TEXT = 'Identifique\n os grafos bipartidos'
    MENU = 1
    QUESTION = 2
    ANSWER = 3
    CORRECT_ANSWER = 4
    WRONG_ANSWER = 5
    
    running = True
    current_question = 0
    max_questions = 0
    current_graph = None
    state = MENU
    state_question = CORRECT_ANSWER
    circle_radius = 40
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
        
        self.clock = pygame.time.Clock()

    def run(self, graphs):
        pygame.init()
        self.graphs = graphs
        self.max_questions = len(graphs)
        while self.running:
            if self.state==self.MENU:
                self.menu_screen.run()
            elif self.state==self.QUESTION:
                self.question_screen.run()
            elif self.state==self.ANSWER:
                 self.answer_screen.run()

    def quit_game(self):
        self.running = False

    def start_game(self):
        self.state = self.QUESTION
    
    def answer_question(self, ans):
        self.state = self.ANSWER
        if self.current_graph.bipartite() == ans:
            self.state_question = self.CORRECT_ANSWER
        else:
            self.state_question = self.WRONG_ANSWER

    def next_question(self):
        self.current_question = (self.current_question+1)%self.max_questions #cicle
        self.state = self.QUESTION
