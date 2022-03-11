import pygame


class LaneLine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/lane_line.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        # custom
        self.speed = 5

    def update(self, *args, **kwargs):
        self.move(*args, **kwargs)

    def move(self, up=0):
        if self.rect.top >= 800:
            self.rect.centery -= 1000
        self.rect.centery += self.speed + up


lines = list()

for i in range(5):
    for j in range(4):
        x = 220 + 120 * j
        y = i * 200
        new_line = LaneLine(x, y)
        lines.append(new_line)

