import pygame
from button import Button
import constants as C
from text_input import Text_Input

class Menu:
    # constructeur
    def __init__(self, app):
        # get app's screen to draw on
        self.app = app
        self.screen = app.screen

        self.app.cursor.execute(f"SELECT intitule_diff FROM difficulte WHERE difficulte_id < 4")
        self.diff_names = self.app.cursor.fetchall()

        self.background_img = C.img_menu_background
        self.btn_list = [
            Button(self.screen, C.pos_menu_start, C.img_menu_start, 'start'),
            Button(self.screen, C.pos_menu_regle, C.img_menu_start, 'regles'),
            Button(self.screen, C.pos_menu_score, C.img_menu_start, 'scores'),
            Button(self.screen, C.pos_menu_quit, C.img_menu_start, 'quit'),
        ]
        self.text_input = Text_Input(self.app, 50, 480)
        self.text_input2 = Text_Input(self.app, 50, 565)

    # method update, appelée chaque frame (60fois par sec)
    def update(self, events):
        # à faire
        pass



    # method draw, appelée après l'update
    def draw(self):
        self.screen.blit(self.background_img, (0,0))
        for b in self.btn_list:
            b.draw()
        # start button text
        C.blit_text(self.screen, "Start", C.pos_start_text, 280, C.font_karmatic, '#101010')
        # difficulté text
        C.blit_text(self.screen, f"Difficulté: {self.diff_names[self.app.difficulte-1][0]}", (1015,360), C.WIN_X, C.font_pixelop8, 'white')
        self.text_input.draw()
        self.text_input2.draw()
