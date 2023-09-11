import pygame
import constants as C
from button import Button

class Score:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen

        self.p1_score = 0
        self.p2_score = 0

        self.p1_name = ""
        self.p2_name = ""

        self.button = Button(self.screen, (15, 15), C.img_menu_start, C.img_menu_start_push, 'menu')


    def update(self):
        self.button.update()

        self.button_events()

    def draw(self):
        self.button.draw()

        C.blit_text(self.screen, f"Score de {self.p1_name}: {self.p1_score} !",
                    (C.WIN_X/2, 300), C.WIN_X, C.font_karmatic20, 'white')
        C.blit_text(self.screen, f"Score de {self.p2_name}: {self.p2_score} !",
                    (C.WIN_X / 2, 420), C.WIN_X, C.font_karmatic20, 'white')


    def button_events(self):
        if self.button.isClicked('menu'):
            self.app.set_state('Menu')

    def set_scores(self, score1=(None, ""), score2=(None, "")):
        if not score1[1] == None:
            self.p1_score += score1[1]
        if not score2[1] == None:
            self.p2_score += score2[1]
        self.p1_name = score1[0]
        self.p2_name = score2[0]

