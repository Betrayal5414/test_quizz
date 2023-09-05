import pygame
from button import Button
import constants as C

class Menu:
    # constructeur
    def __init__(self, app):
        # get app's screen to draw on
        self.app = app
        self.screen = app.screen

        self.app.cursor.execute(f"SELECT intitule_diff FROM difficulte WHERE difficulte_id < 4")
        self.diff_names = self.app.cursor.fetchall()
        print(self.diff_names)

        self.background_img = pygame.image.load("img/menu_principal.png")
        self.btn_list = [
            Button(self.screen, 1025, 500, "img/boutons/menu/menu_nopush.png", 'start'),
            Button(self.screen, 1000, 400, "img/boutons/menu/difficulte_1.png", 'easy'),
            Button(self.screen, 1080, 400, "img/boutons/menu/difficulte_2.png", 'medium'),
            Button(self.screen, 1160, 400, "img/boutons/menu/difficulte_3.png", 'hard'),
        ]

    # method update, appelée chaque frame (60fois par sec)
    def update(self):
        for b in self.btn_list:
            b.update()

    # method draw, appelée après l'update
    def draw(self):
        self.screen.blit(self.background_img, (0,0))
        for b in self.btn_list:
            b.draw()
        # start button text
        C.blit_text(self.screen, "Start", C.start_text_pos, 280, C.font_karmatic, '#101010')
        # difficulté text
        C.blit_text(self.screen, f"Difficulté: {self.diff_names[self.app.difficulte-1][0]}", (1015,360), C.WIN_X, C.font_pixelop8, 'white')
