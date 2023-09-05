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


class App:
    def __init__(self):
        # connexion à la DB
        self.conn = sqlite3.connect('db/quizz.db')
        self.cursor = self.conn.cursor()

        diff = 2

        # pygame initialisation
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720)) # taille de la fenêtre

        # titre de la fenêtre
        pygame.display.set_caption('Le quizz des gamerzz')

        self.running = True

        self.clock = pygame.time.Clock()
        self.fps = 60
        #

        self.menu = Menu(self.screen)
        self.game = Game(self.screen, self.cursor, diff)

        self.statedict = {
            1: 'Menu',
            2: 'Game'
        }
        self.state = 'Menu'
        # start game loop
        self.loop()




    def loop(self):
        # game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.state == 'Game':
                        if self.game.back_button.checkForClick(event):
                            self.state = 'Menu'
                        for i, b in enumerate(self.game.answers_buttons):
                            if b.checkForClick(event):
                                self.game.answer_index = i+1
                    if self.state == 'Menu':
                        if self.menu.button.checkForClick(event):
                            time.sleep(0.1)
                            self.state = 'Game'
                            self.game.timer.reset()


                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        sys.exit()

            if self.state == 'Menu':
                self.menu.update()
            if self.state == 'Game':
                self.game.update()
            # method draw
            self.draw()
            self.clock.tick(self.fps)


    def draw(self):
        self.screen.fill('#0a0a0a')
        # projettage de l'image sur l'écran
        if self.state == 'Menu':
            self.menu.draw()
        if self.state == 'Game':
            self.game.draw()
        pygame.display.flip()
