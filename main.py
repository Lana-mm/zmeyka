import pygame
import time
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 128, 0)  # Темно-зеленый
blue = (50, 153, 213)
pink = (255, 192, 203)

# Массив цветов для змеи
snake_colors = [
    (255, 0, 0),   # Красный
    (0, 255, 0),   # Зеленый
    (0, 0, 255),   # Синий
    (255, 255, 0), # Желтый
    (255, 0, 255), # Фиолетовый
    (0, 255, 255)  # Голубой
]

# Установка размеров окна
width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

snake_block = 20  # Увеличиваем размер блока в 2 раза
snake_speed = 2

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для отображения змеи
def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        color = snake_colors[i % len(snake_colors)]  # Разные цвета для сегментов
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])

# Функция для отображения сообщения
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(width / 2, height / 2))
    screen.blit(mesg, mesg_rect)

# Основная функция игры
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Генерация еды
    def generate_food():
        return round(random.randrange(0, width - snake_block) / 20.0) * 20.0, \
               round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    foodx, foody = generate_food()

    while not game_over:
        while game_close:
            screen.fill(pink)
            message("Вы проиграли! Нажмите C для новой игры или Q для выхода", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(green)
        pygame.draw.rect(screen, black, [foodx, foody, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            Length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
