import pygame
import random
import time

class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/red_car.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.jump_time = time.time()
        self.jump_duration = 1
        self.jump_wait_duration = 0

    def switch_right(self):
        if self.rect.centerx < 600:
            self.rect.centerx += 120

    def switch_left(self):
        if self.rect.centerx > 200:
            self.rect.centerx -= 120

    def jump(self):
        if time.time() - self.jump_time > self.jump_wait_duration:
            self.jump_time = time.time()
            x = self.rect.centerx
            y = self.rect.bottom
            self.image = pygame.image.load("assets/red_car_jump.png")
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.bottom = y
            self.jump_wait_duration += 3

class RivalCar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/white_car.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        #
        self.speed = 1

    def update(self, *args, **kwargs):
        self.move(*args, **kwargs)

    def move(self, up=0):
        if self.rect.top >= 1500:
            self.rect.centery -= 2000
            self.rect.centerx = random.choice((160, 280, 400, 520, 640))
        self.rect.centery += self.speed + up

