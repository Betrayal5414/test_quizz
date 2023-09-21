import pygame
import time
import constants as C

class Timer_Bar:
    def __init__(self, screen, x, y, sec, color=C.colors['Red']):
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
        self.delay = 3
        self.sec = sec + self.delay
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
        # après 20s, il faut que toute la largeur du rectangle soit réduite
        # donc que self.t = self.w
        # 1. le nombre de pixels à enlever chaque seconde
        # 2. le temps écoulé (en secondes)
        self.chrono = self.sec - (time.time() - self.cZero)
        if self.chrono < 0:
            self.chrono = 0

        # on réduit la taille de la barre en fonction du temps écoulé
        # en prenant en compte le délai laissé à l'utilisateur pour lire la question
        if self.sec - self.chrono > self.delay:
            self.t = (self.sec - self.chrono - self.delay) * ((self.w - self.margin*2) / self.sec+self.delay)
            if self.t > self.w - self.margin*2:
                self.t = self.w - self.margin*2



    def draw(self):
        # draw du rect exterieur (bordure)
        pygame.draw.rect(self.screen, self.border_color, pygame.Rect(self.x, self.y, self.w, self.h), 0, self.corners)
        # draw du rect intérieur (la barre se réduisant selon le temps passé)
        pygame.draw.rect(self.screen, self.main_color, pygame.Rect(
            self.x+self.margin, self.y+self.margin, self.w-self.t-self.margin*2, self.h-self.margin*2), 0, self.corners)

        # affichage du chrono (nbr de secondes restantes en texte)
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
