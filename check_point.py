import pygame

class CheckPoint(pygame.sprite.Sprite):
    def __init__(self, x=700, y=-400):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        # custom
        self.speed = 5
        self.count = 0

    def update(self, *args, **kwargs):
        self.move(*args, **kwargs)

    def move(self, up=0):
        if self.rect.top >= 800:
            self.rect.centery -= 1000
            self.count += 1
        self.rect.centery += self.speed + up