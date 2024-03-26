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

# Добавление переменной для подсчета очков
score = 0

# Добавление шрифта для текста
font = pygame.font.Font(None, 36)

# Функция для отображения счета
def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))


#Игровой цикл
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            score += 1  # Увеличиваем счет на 1

        # Обновляем положение мишени для ее движения (можно добавить условия для изменения направления движения)
    target_x += random.randint(-5, 5)
    target_y += random.randint(-5, 5)

        # Проверка выхода мишени за пределы экрана и корректировка положения
    if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
    if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x, target_y))
# Отображаем счет
    show_score(10, 10)


    #Обновление экрана
    pygame.display.update()

pygame.quit()
