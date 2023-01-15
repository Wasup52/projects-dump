import pygame
import random


win_width = 940
win_height = 680
clock = pygame.time.Clock()

xa = random.randint(0, win_width)
ya = random.randint(0, win_height)

pygame.init()
pygame.display.set_caption("Snake")
window = pygame.display.set_mode((win_width, win_height))


class Snake(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = True
        self.up = False
        self.down = False

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height))


class food(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.hitbox = (
            self.x - self.radius - 1,
            self.y - self.radius - 1,
            self.radius * 2 + 1,
            self.radius * 2 + 1,
        )

    def draw(self, window):
        self.hitbox = (
            self.x - self.radius - 1,
            self.y - self.radius - 1,
            self.radius * 2 + 1,
            self.radius * 2 + 1,
        )
        # pygame.draw.rect(window, (0, 0, 255), self.hitbox, 1)
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), self.radius)


# def game_over():
#     global game_over
#     global restart
#     global exit_
#     if game_over:
#         while


def redraw_game_win():
    window.fill((0, 0, 0))
    for part in body:
        part.draw(window)
    apple.draw(window)
    pygame.display.update()


game_over = False
lunched = True
snake = Snake(win_width // 2, win_height // 2, 15, 15)
apple = food(xa, ya, 4)
body = [snake, Snake(snake.x - 16, snake.y, snake.width, snake.height)]
while lunched:
    clock.tick(20)

    ### -------Border------- ###
    if body[0].x < 0:
        body[0].x = win_width
    if body[0].x > win_width:
        body[0].x = 0
    if body[0].y < 0:
        body[0].y = win_height
    if body[0].y > win_height:
        body[0].y = 0
    ### -------------------- ###

    ### ------Movements----- ###
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] == 1 and not snake.right:
        snake.left = True
        snake.right = False
        snake.up = False
        snake.down = False
    if keys[pygame.K_RIGHT] == 1 and not snake.left:
        snake.left = False
        snake.right = True
        snake.up = False
        snake.down = False
    if keys[pygame.K_UP] == 1 and not snake.down:
        snake.left = False
        snake.right = False
        snake.up = True
        snake.down = False
    if keys[pygame.K_DOWN] == 1 and not snake.up:
        snake.left = False
        snake.right = False
        snake.up = False
        snake.down = True

    if snake.left:
        body.insert(
            0,
            Snake(
                body[0].x - snake.width - 1, body[0].y, body[0].width, body[0].height
            ),
        )
        body.pop(len(body) - 1)
    if snake.right:
        body.insert(
            0,
            Snake(
                body[0].x + snake.width + 1, body[0].y, body[0].width, body[0].height
            ),
        )
        body.pop(len(body) - 1)
    if snake.up:
        body.insert(
            0,
            Snake(
                body[0].x, body[0].y - snake.height - 1, body[0].width, body[0].height
            ),
        )
        body.pop(len(body) - 1)
    if snake.down:
        body.insert(
            0,
            Snake(
                body[0].x, body[0].y + snake.height + 1, body[0].width, body[0].height
            ),
        )
        body.pop(len(body) - 1)
    ### -------------------- ###

    ### ----Aplle eating---- ###
    if (
        body[0].x <= apple.hitbox[0] <= body[0].x + snake.width
        and body[0].y <= apple.hitbox[1] <= body[0].y + snake.height
        or body[0].x <= apple.hitbox[0] + apple.hitbox[2] <= body[0].x + snake.width
        and body[0].y <= apple.hitbox[1] + apple.hitbox[3] <= body[0].y + snake.height
    ):
        apple.x = random.randint(0, win_width)
        apple.y = random.randint(0, win_height)
        body += [Snake(body[1].x, body[1].y, body[1].width, body[1].height)]
    ### -------------------- ###

    for part in body[1:]:
        if (
            part.x <= body[0].x <= part.x + snake.width
            and part.y <= body[0].y <= part.y + snake.height
        ):
            game_over = True

    if game_over:
        lunched = False
    # if game_over:
    #     restart = False
    #     exit_ = False
    #     while not restart or not exit_:
    #         window.fill((0,0,0))
    #         keys = pygame.key.get_pressed()

    # print(game_over)

    redraw_game_win()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False

pygame.quit()
