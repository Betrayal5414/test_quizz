import pygame
import constants as C
from button import Button

class Score:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen

        self.p1_score = 0
        self.p2_score = 0

        self.button = Button(self.screen, 15, 15, "img/boutons/menu/menu_nopush.png", 'menu')


    def update(self):
        self.button.update()

        self.button_events()

    def draw(self):
        #C.blit_text(self.screen, 'les scores!', (C.WIN_X/2,C.WIN_Y/2), C.WIN_X, C.font_karmatic, 'white')
        self.button.draw()

        C.blit_text(self.screen, f"Score du joueur 1...   {self.p1_score} !",
                    (C.WIN_X/2, 300), C.WIN_X, C.font_karmatic, 'white')
        C.blit_text(self.screen, f"Score du joueur 1: {self.p1_score} !",
                    (C.WIN_X/2, 400), C.WIN_X, C.font_kemco, 'white')
        C.blit_text(self.screen, f"Score du joueur 1: {self.p1_score} !",
                    (C.WIN_X/2, 500), C.WIN_X, C.font_symtext, 'white')
        C.blit_text(self.screen, f"Score du joueur 1: {self.p1_score} !",
                    (C.WIN_X/2, 600), C.WIN_X, C.font_pixelop, 'white')

    def button_events(self):
        if self.button.isClicked('menu'):
            self.app.state = 'Menu'

    def set_scores(self, score1=None, score2=None):
        if not score1 == None:
            self.p1_score += score1
        if not score2 == None:
            self.p2_score += score2
