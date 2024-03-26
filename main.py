import pygame
pygame.init()

#Создание окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My Game is TIR")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Игровой цикл
running = True
while running:
    pass

pygame.quit()
