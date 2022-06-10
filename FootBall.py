# Импортируем
import pygame
import random


# Подготовка к работе
pygame.init()

# Настройка фпс
FPS = 150
clock = pygame.time.Clock()

# Создание переменных
screen_width = 674
screen_height = 1024
xpos = 338
ypos = 513
xpos1 = 420
ypos2 = 940
xpos2 = 250
ypos3 = 10
speedx = 5
speedy = 5
score1 = 0
score2 = 0
speed1 = 5
speed2 = 5

# Создание цветов
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Загрузка и настройка картинок
background = pygame.image.load("back.png")
pl1 = pygame.image.load("vr.png")
pl2 = pygame.image.load("vrl.png")
icon = pygame.image.load("fb.png")
pygame.display.set_icon(icon)
ball = pygame.image.load("bl.png")
ball.set_colorkey((255, 255, 255))
ball.set_alpha(200)

# Создание экрана и его название
DISPLAYSURFACE = pygame.display.set_mode((674, 1024))
pygame.display.set_caption("Ball Game")

# Добавление шрифтов
font = pygame.font.SysFont("Chilanka", 100)
font_small = pygame.font.SysFont("Chilanka", 100)
game_over = font.render("Game Over", True, BLACK)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                xpos = event.pos[0] - 75
                ypos = event.pos[1] - 75
                print(event.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        speed1 -= 3
    elif keys[pygame.K_RIGHT]:
        speed1 += 3
    if keys[pygame.K_a]:
        speed2 -= 3
    elif keys[pygame.K_d]:
        speed2 += 3
    if xpos > screen_width-64:
        speedx = (-5 * random.random())-1
    if xpos < 0:
        speedx = (5 * random.random())+1
    if ypos > screen_height-64:
        speedy = (-5 * random.random())-1
        score2 += 1
    if ypos < 0:
        speedy = (5 * random.random())+1
        score1 += 1
    xpos1 = speed1
    xpos2 = speed2
    xpos += speedx
    ypos += speedy
    DISPLAYSURFACE.blit(background, (0, 0))
    DISPLAYSURFACE.blit(ball, (xpos, ypos))
    DISPLAYSURFACE.blit(pl1, (xpos1, ypos2))
    DISPLAYSURFACE.blit(pl2, (xpos2, ypos3))
    scores1 = font_small.render(str(score1), True, BLACK)
    scores2 = font_small.render(str(score2), True, BLACK)
    DISPLAYSURFACE.blit(scores1, (10, 10))
    DISPLAYSURFACE.blit(scores2, (10, 930))
    pygame.display.flip()
    clock.tick(FPS)
