import random
import time
import pygame
import sqlite3
import sys
from timer_bar import Timer_Bar
from button import Button
import constants as C
from menu import Menu
from game import Game
from scores import Score


class App:
    def __init__(self):
        # connexion à la DB
        self.conn = sqlite3.connect('db/quizz.db')
        self.cursor = self.conn.cursor()

        # difficulté (temporaire)
        self.difficulte = 1

        # pygame initialisation
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720)) # taille de la fenêtre

        # titre de la fenêtre
        pygame.display.set_caption('Le quizz des gamerzz')

        self.running = True

        self.clock = pygame.time.Clock()
        self.fps = 60
        #

        self.menu = Menu(self)
        self.game = Game(self, self.cursor)
        self.scores = Score(self)

        # to-do state machine
        self.statedict = {
            1: 'Menu',
            2: 'Game',
            3: 'Scores'
        }
        self.state = 'Game'
        # start game loop
        self.loop()




    def loop(self):
        # game loop
        while self.running:

            dt = self.clock.tick(self.fps)

            # check pygame events (user inputs)
            for event in pygame.event.get():
                # quit program ('normalement' avec la croix ou alt-f4)
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    pass


                # keyboard inputs
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    # quit program (Esc key)
                    if keys[pygame.K_ESCAPE]:
                        sys.exit()

            # switch states
            if self.state == 'Menu':
                self.menu.update()
            elif self.state == 'Game':
                self.game.update()
            elif self.state == 'Scores':
                self.scores.update()

            self.button_events()
            # after updates go to draw
            self.draw()


    def draw(self):
        self.screen.fill('#0a0a0a') # background of the window, overriden by background images
        # switch states
        if self.state == 'Menu':
            self.menu.draw()
        elif self.state == 'Game':
            self.game.draw()
        elif self.state == 'Scores':
            self.scores.draw()
        # update changes
        pygame.display.flip()

    def button_events(self):
        if self.state == 'Menu':
            for i, b in enumerate(self.menu.btn_list):
                if b.isClicked('start'):
                    time.sleep(0.1)
                    self.state = 'Game'
                    self.game.reset()
                elif b.isClicked('easy'):
                    self.difficulte = 1
                elif b.isClicked('medium'):
                    self.difficulte = 2
                elif b.isClicked('hard'):
                    self.difficulte = 3

        elif self.state == 'Game':
            if self.game.back_button.isClicked():
                self.state = 'Menu'
            for i, b in enumerate(self.game.answers_buttons):
                if b.isClicked():
                    self.game.answer_index = i+1
