# Импортируем
import pygame
import random


def main() -> None:
    # Подготовка к работе
    pygame.init()

    # Настройка фпс
    FPS = 60
    clock = pygame.time.Clock()

    # Создание переменных
    screen_width = 674
    screen_height = 1024
    DISPLAYSURFACE = pygame.display.set_mode((674, 1024))
    xpos = 50
    ypos = 50
    speedx = 5
    speedy = 5
    score = 0

    # Создание цветов
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Загрузка и настройка картинок 
    background = pygame.image.load("back.png")
    image = pygame.image.load("bl.png")
    image.set_colorkey((255, 255, 255))
    image.set_alpha(200)

    # Создание экрана и его название
    DISPLAYSURFACE = pygame.display.set_mode((674, 1024))
    pygame.display.set_caption("FootBall Game")

    # Добавление шрифтов
    font = pygame.font.SysFont("Chilanka", 100)
    font_small = pygame.font.SysFont("Chilanka", 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False
        if xpos > screen_width-64:
            speedx = (-5 * random.random())-1
        if xpos < 0:
            speedx = (5 * random.random())+1
        if ypos > screen_height-64:
            speedy = (-5 * random.random())-1
        if ypos < 0:
            speedy = (5 * random.random())+1
        xpos += speedx
        ypos += speedy
        DISPLAYSURFACE.blit(background, (0, 0))
        DISPLAYSURFACE.blit(image, (xpos, ypos))
        scores = font_small.render(str(score), True, BLACK)
        DISPLAYSURFACE.blit(scores, (10, 10))
        DISPLAYSURFACE.blit(scores, (10, 930))
        pygame.display.flip()
        clock.tick(150)


if __name__ == "__main__":
    main()





