import datetime
import constants as C
from button import Button

class Score:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.cursor = self.app.cursor
        self.conn = self.app.conn

        self.p1_score = 0
        self.p2_score = 0

        self.p1_name = ""
        self.p2_name = ""

        self.best_scores = []
        self.score_names = []

        self.button = Button(self.screen, C.pos_gameover_retour, C.img_menu_start, C.img_menu_start_push, 'menu')


    def update(self):
        self.button.update()

        self.button_events()

    def draw(self):
        self.button.draw()
        C.blit_text(self.screen, "Retour", C.pos_gameover_retour_text, C.WIN_X, C.font_karmatic20, 'black')
        C.blit_text(self.screen, f"PTS         DATE               NOM",
                    (70, 140), C.WIN_X, C.font_karmatic20, 'yellow')
        # affichage best scores
        if len(self.best_scores) > 0:
            for i, s in enumerate(self.best_scores):
                C.blit_text(self.screen, f"{s[1]}       {s[2]}       {s[3]}.",
                            (70, 200 + i*30), C.WIN_X, C.font_karmatic20, 'yellow')

    def button_events(self):
        if self.button.isClicked('menu'):
            self.app.set_state('Menu')

    def set_scores(self, score1=(None, ""), score2=(None, "")):
        self.p1_score = self.p2_score = 0
        if not score1[1] == None:
            self.p1_score += score1[1]
        if not score2[1] == None:
            self.p2_score += score2[1]
        self.p1_name = score1[0]
        self.p2_name = score2[0]

    def get_scores_db(self):
        self.cursor.execute(f"Select * FROM score ORDER BY score_joueur DESC LIMIT 15")
        self.best_scores = self.cursor.fetchall()
        print(self.best_scores)

    def set_scores_db(self):
        today_date = datetime.datetime.today().strftime("%d-%m-%Y")
        # enlève les 2 premiers caractères de l'année ( 2023  ->  23 )
        today_date = today_date[:-4] + today_date[-2:]
        self.cursor.execute('INSERT INTO score (score_joueur, date, nom_joueur) VALUES (?,?,?)', (self.p1_score, today_date, self.p1_name))
        if self.app.game.nbr_players == 2:
            self.cursor.execute('INSERT INTO score (score_joueur, date, nom_joueur) VALUES (?,?,?)', (self.p2_score, today_date, self.p2_name))
        self.conn.commit()
        pass
