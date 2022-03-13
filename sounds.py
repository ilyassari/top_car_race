import pygame
import os

class BackgroundMusic:
    def play(self):
        pygame.mixer.music.load(os.sep.join(("assets","background.mp3")))
        pygame.mixer.music.play(loops=True)

class SoundEffects:
    def __init__(self):
        self.countdown = pygame.mixer.Sound(os.sep.join(("assets", "countdown.wav")))
        self.jumping = pygame.mixer.Sound(os.sep.join(("assets", "jumping.wav")))
        self.passing = pygame.mixer.Sound(os.sep.join(("assets", "passing.wav")))
        self.hit_rival = pygame.mixer.Sound(os.sep.join(("assets", "hit_rival.wav")))
        self.gather_fuel = pygame.mixer.Sound(os.sep.join(("assets", "gather_fuel.wav")))
        self.game_over = pygame.mixer.Sound(os.sep.join(("assets", "game_over.wav")))

