import pygame
import random


win_width = 940
win_height = 680

img_width = 356
img_height = 220

pygame.init()
pygame.display.set_caption("DVD loading")
screen = pygame.display
window = screen.set_mode((win_width, win_height))

# x = random.randint(0, win_width - img_width)
# y = random.randint(0, win_height - img_height)
x = 100
y = 100
c = random.randint(0, 3)

vel_x = 10
vel_y = 10
# vel_x_sprint = 10
# vel_y_sprint = 10

DVD = [
    pygame.image.load(
        "Pygame\\DVD loading\\DVD sprites\\DVD logo jaune.png"
    ),
    pygame.image.load(
        "Pygame\\DVD loading\\DVD sprites\\DVD logo bleu.png"
    ),
    pygame.image.load(
        "Pygame\\DVD loading\\DVD sprites\\DVD logo rouge.png"
    ),
    pygame.image.load(
        "Pygame\\DVD loading\\DVD sprites\\DVD logo vert.png"
    ),
]


def redraw_game_win(c):
    window.fill((0, 0, 0))
    # pygame.draw.circle(window, (0, 255, 0), (x, y), radius)
    window.blit(DVD[c], (x, y))
    screen.update()


def ran(n):
    rando = random.randint(0, 3)
    if rando != n:
        return rando
    else:
        return ran(n)


lunched = True
while lunched:
    # delays prevent the movement to be super fat
    pygame.time.delay(100)

    keys = pygame.key.get_pressed()

    if x <= 0:
        vel_x = -vel_x
        c = ran(c)

    if x + img_width >= win_width:
        vel_x = -vel_x
        c = ran(c)

    if y <= 0:
        vel_y = -vel_y
        c = ran(c)

    if y + img_height >= win_height:
        vel_y = -vel_y
        c = ran(c)

    x -= vel_x
    y += vel_y

    redraw_game_win(c)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False

pygame.quit()

