import pygame
import time
import constants as C

class Timer_Bar:
    def __init__(self, screen, x, y, sec=15, color=C.colors['Red']):
        self.screen = screen
        # positions for drawing
        self.x = x
        self.y = y
        self.w = 500
        self.h = 65
        self.margin = 6
        self.corners = 5   # determines how much the rect's corners are rounded
        # timer-related variables
        self.t = 0
        self.sec = sec
        self.cZero = time.time()
        self.chrono = self.sec - (time.time() - self.cZero)
        # surface to write time left
        self.txt_surface = None
        # colors
        self.border_color = color['Dark']
        self.main_color = color['Mid']

    def update(self):
        # self.t représente le nbr de pixel a retirer de la barre (0 au début, self.w-self.margin*2 au max)
        # self.sec - self.chrono    -> temps écoulé (secondes)
        # (self.w-self.margin*2)/self.sec   -> nbr de pixels à retirer chaque seconde
        self.t = (self.sec - self.chrono) * ((self.w-self.margin*2)/self.sec)
        # s'assure que t ne devient pas négatif, peut etre remplacé par max(0,self.t)
        if self.t >= self.w-self.margin*2:
            self.t = self.w-self.margin*2

        # timer texte, minnuteur qui va de self.sec à 0
        self.chrono = self.sec - (time.time() - self.cZero)
        if self.chrono < 0:
            self.chrono = 0

    def draw(self):
        # draw outside rect
        pygame.draw.rect(self.screen, self.border_color, pygame.Rect(self.x, self.y, self.w, self.h), 0, self.corners)
        # draw inside rect (celui qui réduit jusqu'à 'disparaitre' en utilisant self.t)
        pygame.draw.rect(self.screen, self.main_color, pygame.Rect(
            self.x+self.margin, self.y+self.margin, self.w-self.t-self.margin*2, self.h-self.margin*2), 0, self.corners)

        # draw chrono text to screen
        self.txt_surface = C.font_karmatic30.render(f"{round(self.chrono, 1)}", False, (0,0,0))
        self.screen.blit(self.txt_surface, (self.x+self.w/2 - self.txt_surface.get_width()/2,
                                            self.y+self.txt_surface.get_height()/2))

    # reset method, resets chrono and t
    def reset(self):
        self.t = 0
        self.cZero = time.time()
        self.chrono = self.sec - (time.time() - self.cZero)

    def change_color(self, color: str):
        color = color.capitalize()
        self.main_color = C.colors[color]['Mid']
        self.border_color = C.colors[color]['Dark']