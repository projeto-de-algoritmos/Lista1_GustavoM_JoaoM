import pygame 
import math
from pygame.locals import *
import graph
from assets import Button
from assets import Text
from assets import Graph
from assets import Palette
from assets import Timer
from assets import Line

class Screen:
    # Screen codes
    ID = 0
    def __init__(self, game, background_color):
        self.game = game
        self.background_color = background_color
        self.x_middle = self.game.WIDTH/2
        self.y_middle = self.game.HEIGHT/2
        self.assets = []
    def build_function(self):
        pass
    def update_function(self):
        pass
    def put_asset(self, asset):
        self.assets.append(asset)
        self.game.screen.fill(Palette.COLOR_1)
    def draw(self):
        self.game.screen.fill(self.background_color)
        self.update_function()
        for asset in self.assets:
            asset.draw()
    def run(self):
        self.build_function()
        while self.game.running and self.game.current_screen==self.ID:
            for event in pygame.event.get():
                for asset in self.assets:
                    asset.get_event(event, pygame.mouse.get_pos())
                if event.type == QUIT:
                    self.game.quit_game()
            self.draw()
            pygame.display.update()

class Menu(Screen):
    ID = 1
    def __init__(self, game):
        super().__init__(game=game, background_color=Palette.COLOR_1)
        #Assets
        info_icon = pygame.image.load('info.png')
        play_button = Button(screen=game.screen, position=((self.x_middle), (game.HEIGHT-200)),  on_press=self.game.start_game , text='Níveis padrões', width=300)
        info_button = Button(screen=game.screen, position=((70), (40)),  on_press=lambda:game.change_screen(Info), icon=info_icon, text='Info', width=120, color=Palette.COLOR_1)
        create_button = Button(screen=game.screen, position=((self.x_middle), (game.HEIGHT-100)),  on_press=lambda:game.change_screen(SelectTam), text='Níveis customizados', width=300, color=Palette.GREEN)
        title = Text(screen=self.game.screen, position=((self.x_middle),(100)), text=self.game.GAME_NAME, font_size=60)
        sub_title = Text(screen=self.game.screen, position=((self.x_middle),(180)), text=self.game.INTRO_TEXT, font_size=34, font_color=Palette.COLOR_5)
        self.put_asset(play_button)
        self.put_asset(info_button)
        self.put_asset(create_button)
        self.put_asset(title)
        self.put_asset(sub_title)



class Info(Screen):
    ID = 3
    def __init__(self, game):
        super().__init__(game=game, background_color=Palette.COLOR_9)
        # Assets
        back_button = Button(screen=self.game.screen, position=((79), (40)), on_press=lambda:game.change_screen(Menu), text='Voltar', width=120)
        title = Text(screen=self.game.screen, position=((self.x_middle),(40)), text='O que é um grafo bipartido?', font_size=38, font_color=Palette.BLACK)
        definition_text = open('definition.txt').read()
        definition = Text(screen=self.game.screen, position=((self.x_middle),(self.y_middle)), text=definition_text, font_size=24, font_type='robotoslab', font_color=Palette.BLACK)
        self.put_asset(back_button)
        self.put_asset(title)
        self.put_asset(definition)

    

class Question(Screen):
    ID = 4
    def __init__(self, game):
        super().__init__(game=game, background_color=Palette.COLOR_9)
        # Assets
        self.timer = Timer(surface=self.game.screen, color=Palette.GREEN , rect=(20, 20, 60, 60) , start_angle=0 , stop_angle=2*math.pi, width=30, on_finished=lambda:self.game.no_answer_question())
        yes_button = Button(screen=self.game.screen, position=((self.x_middle-120), (self.game.HEIGHT-80)), on_press=lambda:self.game.answer_question(True), text='Sim', color=Palette.BLUE)
        no_button = Button(screen=self.game.screen, position=((self.x_middle+120), (self.game.HEIGHT-80)), on_press=lambda:self.game.answer_question(False), text='Não', color=Palette.RED)
        question = Text(screen=self.game.screen, text='Esse grafo é bipartido?' ,position=((self.x_middle),(60)), font_size=30, font_color=Palette.COLOR_10)
        self.question_number = Text(screen=self.game.screen, position=((self.x_middle),(30)), font_size=30, font_color=Palette.COLOR_10)
        self.correct_ans = Text(screen=self.game.screen, position=((220),(40)), font_size=28, font_color=Palette.GREEN)
        self.wrong_ans = Text(screen=self.game.screen, position=((220),(60)), font_size=28, font_color=Palette.RED)
        self.graph = Graph(game=self.game, reveal=False)
        self.put_asset(self.timer)
        self.put_asset(yes_button)
        self.put_asset(no_button)
        self.put_asset(question)
        self.put_asset(self.question_number)
        self.put_asset(self.correct_ans)
        self.put_asset(self.wrong_ans)
        self.put_asset(self.graph)

    def update_function(self):
        self.timer.seconds=(pygame.time.get_ticks()-self.timer.start_timer)/1000
        self.graph.set_graph(self.game.current_graph)
        q_number = '( {}/{} )'.format(self.game.current_question+1, self.game.max_questions)
        c_ans = 'Respostas certas: {}'.format(self.game.corrects_ans)
        w_ans = 'Respostas erradas: {}'.format(self.game.wrong_ans)
        self.question_number.text = q_number
        self.wrong_ans.text = w_ans
        self.correct_ans.text = c_ans

    def build_function(self):
        self.game.current_graph = self.game.graphs[self.game.current_question]
        self.timer.start_timer=pygame.time.get_ticks()

class Answer(Screen):
    ID = 5
    def __init__(self, game):
        super().__init__(game=game, background_color=Palette.COLOR_9)

        #Assets
        quit_button = Button(screen=self.game.screen, position=((self.game.WIDTH-120), (50)), on_press=lambda:game.change_screen(Menu), text='Voltar para o menu', color=Palette.RED)
        next_button = Button(screen=self.game.screen, position=((self.x_middle), (self.game.HEIGHT-80)), on_press=self.game.next_question, text='Próxima pergunta', color=Palette.BLUE)
        self.correct_ans = Text(screen=self.game.screen, position=((220),(40)), font_size=28, font_color=Palette.GREEN)
        self.wrong_ans = Text(screen=self.game.screen, position=((220),(60)), font_size=28, font_color=Palette.RED)
        self.answer = Text(screen=self.game.screen, position=((self.x_middle),(60)), font_size=42)
        self.graph = Graph(game=self.game, reveal=True)

        self.put_asset(quit_button)
        self.put_asset(next_button)
        self.put_asset(self.correct_ans)
        self.put_asset(self.wrong_ans)
        self.put_asset(self.answer)
        self.put_asset(self.graph)
    
    def update_function(self):
        self.graph.set_graph(self.game.current_graph)
        c_ans = 'Respostas certas: {}'.format(self.game.corrects_ans)
        w_ans = 'Respostas erradas: {}'.format(self.game.wrong_ans)
        self.wrong_ans.text = w_ans
        self.correct_ans.text = c_ans
        if self.game.state_question == self.game.CORRECT_ANSWER:
            self.answer.text = 'Resposta Correta!'
            self.answer.font_color = Palette.GREEN
        elif self.game.state_question == self.game.WRONG_ANSWER:
            self.answer.text = 'Resposta Errada'
            self.answer.font_color = Palette.RED
        elif self.game.state_question == self.game.TIMES_UP:
            self.answer.text = 'O tempo acabou'
            self.answer.font_color = Palette.RED

class Finish(Screen):
    ID = 6
    def __init__(self, game):
        super().__init__(game=game, background_color=Palette.COLOR_9)
        title = Text(screen=self.game.screen, position=((self.x_middle),(100)), text='O jogo acabou', font_size=60, font_color=Palette.BLACK)
        sub_title = Text(screen=self.game.screen, position=((self.x_middle),(180)), text='Sua pontuação foi: ', font_size=42, font_color=Palette.BLACK)
        back_button = Button(screen=self.game.screen, position=((self.x_middle), (self.game.HEIGHT-80)), on_press=lambda:self.game.change_screen(Menu), text='Voltar para o menu', color=Palette.BLUE)
        self.correct_ans = Text(screen=self.game.screen, position=((self.x_middle),(self.y_middle-30)), font_size=42, font_color=Palette.GREEN)
        self.wrong_ans = Text(screen=self.game.screen, position=((self.x_middle),(self.y_middle+30)), font_size=42, font_color=Palette.RED)
        self.put_asset(title)
        self.put_asset(back_button)
        self.put_asset(sub_title)
        self.put_asset(self.correct_ans)
        self.put_asset(self.wrong_ans)
    def update_function(self):
        c_ans = 'Respostas certas: {}'.format(self.game.corrects_ans)
        w_ans = 'Respostas erradas: {}'.format(self.game.wrong_ans)
        self.wrong_ans.text = w_ans
        self.correct_ans.text = c_ans

class SelectTam(Screen):
    def __init__(self, game):
        super().__init__(game=game, background_color=Palette.COLOR_9)
        title = Text(screen=self.game.screen, position=((self.x_middle),(40)), text='Selecione o tamanho do grafo', font_size=38, font_color=Palette.BLACK)
        back_button = Button(screen=self.game.screen, position=((self.game.WIDTH-120), (50)), on_press=lambda:game.change_screen(Menu), text='Voltar para o menu', color=Palette.RED)
        b_1 = Button(screen=self.game.screen, position=((self.x_middle-150), (200)), on_press=lambda:self.select(1), text='1', color=Palette.BLUE)
        b_2 = Button(screen=self.game.screen, position=((self.x_middle-150), (300)), on_press=lambda:self.select(2), text='2', color=Palette.BLUE)
        b_3 = Button(screen=self.game.screen, position=((self.x_middle-150), (400)), on_press=lambda:self.select(3), text='3', color=Palette.BLUE)
        b_4 = Button(screen=self.game.screen, position=((self.x_middle-150), (500)), on_press=lambda:self.select(4), text='4', color=Palette.BLUE)
        b_5 = Button(screen=self.game.screen, position=((self.x_middle-150), (600)), on_press=lambda:self.select(5), text='5', color=Palette.BLUE)
        b_6 = Button(screen=self.game.screen, position=((self.x_middle+150), (200)), on_press=lambda:self.select(6), text='6', color=Palette.BLUE)
        b_7 = Button(screen=self.game.screen, position=((self.x_middle+150), (300)), on_press=lambda:self.select(7), text='7', color=Palette.BLUE)
        b_8 = Button(screen=self.game.screen, position=((self.x_middle+150), (400)), on_press=lambda:self.select(8), text='8', color=Palette.BLUE)
        b_9 = Button(screen=self.game.screen, position=((self.x_middle+150), (500)), on_press=lambda:self.select(9), text='9', color=Palette.BLUE)
        b_10 = Button(screen=self.game.screen, position=((self.x_middle+150), (600)), on_press=lambda:self.select(10), text='10', color=Palette.BLUE)
        self.put_asset(title)
        self.put_asset(back_button)
        self.put_asset(b_1)
        self.put_asset(b_2)
        self.put_asset(b_3)
        self.put_asset(b_4)
        self.put_asset(b_5)
        self.put_asset(b_6)
        self.put_asset(b_7)
        self.put_asset(b_8)
        self.put_asset(b_9)
        self.put_asset(b_10)
    def select(self, number):
        self.game.select_tam(number)

class CreateLevel(Screen):
    ID = 7
    graph_tam = 5
    node_selected = -1
    def __init__(self, game):
        super().__init__(game=game, background_color=Palette.COLOR_9)
        title = Text(screen=self.game.screen, position=((self.x_middle),(40)), text='Criação do grafo', font_size=38, font_color=Palette.BLACK)
        back_button = Button(screen=self.game.screen, position=((self.game.WIDTH-120), (50)), on_press=lambda:game.change_screen(Menu), text='Voltar para o menu', color=Palette.RED)
        new_graph = Button(screen=self.game.screen, position=((self.x_middle-120), (self.game.HEIGHT-80)), on_press=self.create_new, text='Inserir novo grafo', color=Palette.BLUE)
        continue_button = Button(screen=self.game.screen, position=((self.x_middle+120), (self.game.HEIGHT-80)), on_press=self.play, text='Jogar Nível', color=Palette.RED)
        self.graph = Graph(game=self.game, graph=graph.Graph(self.graph_tam), editable=True, on_press=self.select_node)    
        self.line = Line(screen=self.game.screen, mouse_guide=True, visible=False)
        self.put_asset(title)
        self.put_asset(self.line)
        self.put_asset(back_button)
        self.put_asset(self.graph)
        self.put_asset(new_graph)
        self.put_asset(continue_button)

    def create_graph(self):
        graph = self.graph.graph
        self.game.custom_graphs.append(graph)
    
    def create_new(self):
        self.create_graph()
        self.set_tam(5)
        self.game.change_screen(SelectTam)

    def play(self):
        self.create_graph()
        self.game.start_game(self.game.CUSTOM)

    def update_function(self):
        if self.node_selected!=-1:
            self.line.visible = True
            self.line.pos1 = self.graph.positions[self.node_selected]
        else:
            self.line.visible = False
    def select_node(self):
        if(self.node_selected!=-1 and self.graph.node_select!=-1 and self.node_selected!=self.graph.node_select):
            self.graph.graph.connect(self.node_selected+1, self.graph.node_select+1)
            self.node_selected = -1
            self.graph.node_select = -1
        else:
            self.node_selected = self.graph.node_select
    def set_tam(self, tam):
        self.graph_tam = tam
        self.graph.set_graph(graph.Graph(tam))