from button import Button
from text_input import Text_Input
import constants as C
import time

class Options:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.cursor = self.app.cursor
        self.conn = self.app.conn

        # récupération des noms difficulté dans la BDD
        self.app.cursor.execute(f"SELECT intitule_diff FROM difficulte WHERE difficulte_id < 4")
        self.diff_names = self.app.cursor.fetchall()

        self.j1 = 0
        self.j2 = 1

        self.btn_list = [
            Button(self.screen, C.pos_options_start, C.img_menu_start, C.img_menu_start_push, 'start'),
            Button(self.screen, C.pos_options_easy, C.img_facile, C.img_facile_push, 'easy', True),
            Button(self.screen, C.pos_options_medium, C.img_moyen, C.img_moyen_push, 'medium', True),
            Button(self.screen, C.pos_options_hard, C.img_difficile, C.img_difficile_push, 'hard', True),
            Button(self.screen, C.pos_options_retour, C.img_menu_start, C.img_menu_start_push, 'quit'),
            Button(self.screen, C.pos_options_1joueur, C.img_moyen, C.img_moyen_push, '1-player', True),
            Button(self.screen, C.pos_options_2joueur, C.img_moyen, C.img_moyen_push, '2-player', True),
            Button(self.screen, C.pos_options_icon1, C.img_options_icones[0], C.img_options_icones[0], 'icone_j1'),
            Button(self.screen, C.pos_options_icon2, C.img_options_icones[1], C.img_options_icones[1], 'icone_j2')
        ]

        self.text_inputs = [
            Text_Input(self.app, C.pos_options_nom_1),
            Text_Input(self.app, C.pos_options_nom_2, visible=False)
        ]

        # on appuie sur les boutons réglages par ddéfaut (1 joueur et difficulté récupérée dans l'app - par défaut 1)
        self.btn_list[self.app.difficulte].pushed = True
        self.btn_list[5].pushed = True
        self.btn_list[8].visible = False

    def update(self, events):
        # updates and check events of button
        self.button_events()
        for t in self.text_inputs:
            t.update(events)

    def draw(self):
        self.screen.fill("#03010d")
        for b in self.btn_list:
            b.draw()
        for t in self.text_inputs:
            t.draw()
        self.draw_text()

    def button_events(self):
        for b in self.btn_list:
            b.update()
            if b.isClicked('start'):
                # si le/les joueurs ont bien rentré un nom :
                if self.app.game.nbr_players == 2 and self.text_inputs[1].input.value != "" \
                        and self.text_inputs[0].input.value != "" \
                        or self.app.game.nbr_players == 1 and self.text_inputs[0].input.value != "":
                    # passe à l'écran de jeu et le réinitialise
                    self.app.set_state('Game')
                    self.app.game.reset()
                    time.sleep(0.2)
                    # envoie les noms rentrés à la variable du jeu
                    self.app.game.nom_joueurs = [self.text_inputs[0].input.value,
                                                 self.text_inputs[1].input.value]
                    # envoie les icones des joueurs au jeu
                    self.app.game.icone_j1 = C.img_options_icones[self.j1]
                    self.app.game.icone_j2 = C.img_options_icones[self.j2]

            elif b.isClicked('easy'):
                self.app.difficulte = 1
                self.btn_list[2].pushed = False
                self.btn_list[3].pushed = False

            elif b.isClicked('medium'):
                self.app.difficulte = 2
                self.btn_list[1].pushed = False
                self.btn_list[3].pushed = False

            elif b.isClicked('hard'):
                self.app.difficulte = 3
                self.btn_list[1].pushed = False
                self.btn_list[2].pushed = False

            elif b.isClicked('1-player'):
                self.text_inputs[1].visible = False
                self.btn_list[8].visible = False
                self.btn_list[6].pushed = False
                self.app.game.nbr_players = 1

            elif b.isClicked('2-player'):
                self.text_inputs[1].visible = True
                self.btn_list[8].visible = True
                self.btn_list[5].pushed = False
                self.app.game.nbr_players = 2

            elif b.isClicked('quit'):
                self.app.set_state('Menu')

            elif b.isClicked('icone_j1'):
                self.j1 += 1
                if self.j1 > len(C.img_options_icones) - 1:
                    self.j1 = 0
                if self.j1 == self.j2:
                    self.j1 += 1
                b.change_image(C.img_options_icones[self.j1], C.img_options_icones[self.j1])

            elif b.isClicked('icone_j2'):
                self.j2 += 1
                if self.j2 > len(C.img_options_icones) - 1:
                    self.j2 = 0
                if self.j2 == self.j1:
                    self.j2 += 1
                b.change_image(C.img_options_icones[self.j2], C.img_options_icones[self.j2])


    def draw_text(self):
        C.blit_text(self.screen, 'Start', C.pos_options_start_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, 'Retour', C.pos_options_retour_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, f'{self.diff_names[0][0]}', C.pos_options_easy_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, f'{self.diff_names[1][0]}', C.pos_options_medium_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, f'{self.diff_names[2][0]}', C.pos_options_hard_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, '1 Joueur', C.pos_options_1joueur_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, '2 Joueurs', C.pos_options_2joueur_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, 'Choisir le nombre de joueurs', C.pos_options_bg_text_1, C.WIN_X+50, C.font_karmatic50, 'white')
        C.blit_text(self.screen, 'Choisir la difficulte', C.pos_options_bg_text_2, C.WIN_X, C.font_karmatic50, 'white')
