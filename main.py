import sys
import pygame
import random
import time

from car import PlayerCar, RivalCar
from lane import lines
from check_point import CheckPoint
from fuel import FuelBar, Fuel

pygame.init()

# Ekran Objesini oluştur
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#arka plan görüntüsü
background = pygame.image.load("assets/background.png")
screen.blit(background, (0, 0))

# Bütün spriteler
sprites = pygame.sprite.Group()

# Cars
# all_cars = pygame.sprite.Group()
rivals = pygame.sprite.Group()
for i in range(10):
    x = random.choice((160, 280, 400, 520, 640))
    y = -i * 250
    new_rival = RivalCar(x, y)
    # all_cars.add(new_rival)
    rivals.add(new_rival)
    sprites.add(new_rival)

# player
player = PlayerCar(WIDTH / 2, HEIGHT - 20)
# all_cars.add(player)
sprites.add(player)

# Şerit Çizgileri
all_lines = pygame.sprite.Group()
for line in lines:
    all_lines.add(line)

# FuelBar
fuel_bar = FuelBar()
sprites.add(fuel_bar)
# Fuel
fuels = pygame.sprite.Group()
x = random.choice((160, 280, 400, 520, 640))
y = random.randint(-1000, -500)
fuel = Fuel(x, y)
sprites.add(fuel)
fuels.add(fuel)

# Sayac
check = CheckPoint()
# all_lines.add(check)
sprites.add(check)

# FPS - Saniye de gösterilecek kare sayısını belirten obje
clock = pygame.time.Clock()

def game_over():
    game_over_font = pygame.font.SysFont('Helvetica', 50)
    game_over_txt = game_over_font.render("Game Over", True, (250, 50, 50))
    game_over_pos = (WIDTH - game_over_txt.get_width()) // 2, (HEIGHT - game_over_txt.get_height()) // 2
    screen.blit(game_over_txt, game_over_pos)
    point_font = pygame.font.SysFont('Helvetica', 20)
    point_txt = point_font.render(f"Total Point: {check.count}", True, (250, 50, 50))
    point_txt_pos = (WIDTH - point_txt.get_width()) // 2, (
                HEIGHT - point_txt.get_height()) // 2 + game_over_txt.get_height()
    screen.blit(game_over_txt, game_over_pos)
    screen.blit(point_txt, point_txt_pos)
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()

while True:
    # fps belirle
    clock.tick(60)

    # Penceredeki X butonuna basınca oyunu kapatsın
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.switch_right()
            if event.key == pygame.K_LEFT:
                player.switch_left()
            if event.key == pygame.K_SPACE:
                if time.time() - player.jump_time > player.jump_wait_duration:
                    fuel_bar.amount -= 60
                player.jump()

    if time.time() - player.jump_time > player.jump_duration:
        x = player.rect.centerx
        y = player.rect.bottom
        player.image = pygame.image.load("assets/red_car.png")
        player.rect = player.image.get_rect()
        player.rect.centerx = x
        player.rect.bottom = y

    # basılı tuttukça çalışan tuşlar
    keys = pygame.key.get_pressed()
    up, = (keys[pygame.K_UP],)
    if up:
        rivals.update(up=5)
        fuels.update(up=5)
        all_lines.update(up=5)
        check.update(up=5)

    # Ekran arka planı
    screen.blit(background, (0, 0))

    # Topu hareket ettir
    all_lines.update()
    # all_cars.update()
    sprites.update()

    # Spriteları ekrana yerleştir
    all_lines.draw(screen)
    # all_cars.draw(screen)
    sprites.draw(screen)

    # Çarpışma Kontrolü
    if time.time() - player.jump_time > player.jump_duration:
        if pygame.sprite.spritecollide(player, rivals, False):
            game_over()

    # Benzin Toplama
    if pygame.sprite.spritecollide(player, fuels, False):
        fuel.gathered()
        fuel_bar.amount += fuel.amount


    # Benzin bitişi kontrolü
    if fuel_bar.amount <= 0:
        game_over()


    # ekranda tut
    pygame.display.update()

