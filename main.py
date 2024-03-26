import pygame
import random
pygame.init()

#Создание окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My Game is TIR")
icon = pygame.image.load("image/Mick-Thomson-Jackson-Guitars-promo.jpg")
pygame.display.set_icon(icon)

#Создание объекта игры

target_image = pygame.image.load("image/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)





#Игровой цикл
running = True
while running:
    pass

pygame.quit()
