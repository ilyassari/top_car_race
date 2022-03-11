import pygame
import random


class FuelBar(pygame.sprite.Sprite):
    def __init__(self, x=50, y=580):
        super().__init__()
        self.max_amount = 500
        self.amount = self.max_amount
        self.image = pygame.Surface((10, self.amount))
        self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        #
        self.consumption = .1

    def update(self, *args, **kwargs):
        if self.amount > self.max_amount:
            self.amount = self.max_amount
        self.decrease(*args, **kwargs)

    def decrease(self, up=0):
        self.amount -= self.consumption
        x = self.rect.centerx
        y = self.rect.bottom
        if self.amount > 200:
            self.image = pygame.Surface((10, int(self.amount)))
            self.image.fill((250, 250, 250))
        elif self.amount > 0:
            self.image = pygame.Surface((10, int(self.amount)))
            self.image.fill((250, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x



class Fuel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/fuel.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        #
        self.speed = 5
        self.amount = random.randint(50, 100)

    def update(self, *args, **kwargs):
        self.move(*args, **kwargs)

    def move(self, up=0):
        if self.rect.top >= 800:
            x = random.choice((160, 280, 400, 520, 640))
            y = random.randint(-3000, -1000)
            self.rect.centerx = x
            self.rect.centery = y
        self.rect.centery += self.speed + up

    def gathered(self):
        x = random.choice((160, 280, 400, 520, 640))
        y = random.randint(-4000, -2000)
        self.rect.centerx = x
        self.rect.centery = y
        self.amount = random.randint(50, 100)



