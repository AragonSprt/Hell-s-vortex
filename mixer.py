import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'assets/sounds/'
        self.shotgun = pg.mixer.Sound(self.path + 'shoot.mp3')
        self.npc_pain = pg.mixer.Sound(self.path + 'mob_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'mob_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'mob_attack.wav')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.music.load(self.path + 'ULTRAKILL.mp3')
        pg.mixer.music.set_volume(0.3)