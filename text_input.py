import pygame
import constants as C
import pygame_textinput

class Text_Input:
    def __init__(self, app, x, y, name=""):
        self.app = app
        self.screen = app.screen
        self.x = x
        self.y = y
        self.name = name
        self.txt = ""

        self.clickedOnce = False
        self.pushed = False

        self.img = C.img_name_input
        self.input = pygame_textinput.TextInputVisualizer(font_object=C.font_kemco)

        self.w = self.img.get_width()
        self.h = self.img.get_height()

    def update(self, events):
        self.isClicked()
        if self.pushed:
            self.input.cursor_blink_interval = 500
            self.input.update(events)
        else:
            self.input.cursor_visible = False

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
        self.screen.blit(self.input.surface, (self.x+12, self.y+20))

    def checkForClick(self):
        x, y = pygame.mouse.get_pos()
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h

    def isClicked(self, name=""):
        if name == "":
            pass
        else:
            if self.name != name:
                return False
        # if pressed, return true once and change clickedOnce to false until not pressed anymore
        if pygame.mouse.get_pressed()[0]:
            if self.checkForClick():
                if not self.clickedOnce:
                    self.clickedOnce = True
                    self.pushed = True
                    return True
                else:
                    return False
            else:
                self.pushed = False
        else:
            self.clickedOnce = False
            return False