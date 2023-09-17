import constants as C
from button import Button
import time

class GameOver:

    def __init__(self, app):
        self.app = app
        self.screen = app.screen

        self.background_img = C.img_background_gameover

        self.btn_list = [
            Button(self.screen, C.pos_gameover_retour, C.img_gameover_retour_nopush, C.img_gameover_retour_push, 'Retour'),
            Button(self.screen, C.pos_gameover_rejouer, C.img_gameover_rejouer_nopush, C.img_gameover_rejouer_push, 'Rejouer'),
            Button(self.screen, C.pos_gameover_scores, C.img_gameover_scores_nopush, C.img_gameover_scores_push, 'Scores'),
            Button(self.screen, C.pos_gameover_quitter, C.img_gameover_quitter_nopush, C.img_gameover_quitter_push, 'Quitter'),
        ]

    def update(self):
        self.button_events()

    def draw(self):
        self.screen.blit(self.background_img, (0,0))
        for b in self.btn_list:
            b.draw()
        C.blit_text(self.screen, "Retour", C.pos_gameover_retour_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, "Rejouer", C.pos_gameover_rejouer_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, "Scores", C.pos_gameover_scores_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, "Quitter", C.pos_gameover_quitter_text, C.WIN_X, C.font_karmatic20)

    def button_events(self):
        for b in self.btn_list:
            b.update()
            if b.isClicked('Retour'):
                self.app.set_state("Menu")
            elif b.isClicked('Rejouer'):
                self.app.set_state("Game")
                self.app.game.reset()
                time.sleep(0.2)
            elif b.isClicked('Scores'):
                self.app.set_state("Scores")
                self.app.scores.get_scores_db()
            elif b.isClicked('Quitter'):
                self.app.running = False
