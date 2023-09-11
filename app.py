import pygame
import sqlite3
import sys
import constants as C
from menu import Menu
from options import Options
from game import Game
from scores import Score
from gameover import GameOver


class App:
    def __init__(self):
        # connexion à la DB
        self.conn = sqlite3.connect('db/quizz.db')
        self.cursor = self.conn.cursor()

        # difficulté (temporaire)
        self.difficulte = 1

        # pygame initialisation
        pygame.init()
        pygame.key.set_repeat(500, 64)
        self.screen = pygame.display.set_mode(C.WIN_SIZE) # taille de la fenêtre

        # titre de la fenêtre
        pygame.display.set_caption('Le quizz des gamerzz')

        self.running = True

        self.clock = pygame.time.Clock()
        self.fps = 60

        # double check for quit
        self.quit = False

        self.menu = Menu(self)
        self.options = Options(self)
        self.scores = Score(self)
        self.game = Game(self)
        self.game_over = GameOver(self)

        # to-do state machine
        self.statedict = {
            1: 'Menu',
            2: 'Options',
            3: 'Game',
            4: 'Scores',
            5: 'GameOver',
        }
        self.state = 'Menu'
        # start game loop
        self.loop()




    def loop(self):
        # game loop
        while self.running:

            dt = self.clock.tick(self.fps)

            # check pygame events (user inputs)
            events = pygame.event.get()
            for event in events:
                # quit program ('normalement' avec la croix ou alt-f4)
                if event.type == pygame.QUIT:
                    self.running = False


                # keyboard inputs
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    # quit program (Esc key)
                    if keys[pygame.K_ESCAPE]:
                        sys.exit()

            # switch states
            if self.state == 'Menu':
                self.menu.update()
            elif self.state == 'Options':
                self.options.update(events)
            elif self.state == 'Game':
                self.game.update()
            elif self.state == 'Scores':
                self.scores.update()
            elif self.state == 'GameOver':
                self.game_over.update()

            self.button_events()
            # after updates go to draw
            self.draw()



    def draw(self):
        self.screen.fill('#0a0a0a') # background of the window, overriden by background images
        # switch states
        if self.state == 'Menu':
            self.menu.draw()
        elif self.state == 'Options':
            self.options.draw()
        elif self.state == 'Game':
            self.game.draw()
        elif self.state == 'Scores':
            self.scores.draw()
        elif self.state == 'GameOver':
            self.game_over.draw()
        # update changes
        pygame.display.flip()

    def button_events(self):

        if self.state == 'Game':
            if self.game.back_button.isClicked():
                self.state = 'Options'
            for i, b in enumerate(self.game.answers_buttons):
                if b.isClicked():
                    self.game.answer_index = i+1


    def set_state(self, state):
        for k,v in self.statedict.items():
            if state == v:
                self.state = state