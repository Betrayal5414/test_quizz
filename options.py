from button import Button
from text_input import Text_Input
import constants as C

class Options:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen

        self.btn_list = [
            Button(self.screen, 1025, 500, C.img_menu_start, 'start'),
            Button(self.screen, 1000, 400, C.img_menu_start, 'easy'),
            Button(self.screen, 1080, 400, C.img_menu_start, 'medium'),
            Button(self.screen, 1160, 400, C.img_menu_start, 'hard'),
            Button(self.screen, 1160, 400, C.img_menu_start, 'quit'),
            Button(self.screen, 1160, 400, C.img_menu_start, '1-player'),
            Button(self.screen, 1160, 400, C.img_menu_start, '2-player'),
        ]

        self.text_inputs = [
            #Text_Input(self.screen, )
        ]