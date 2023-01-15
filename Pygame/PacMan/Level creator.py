import pygame
import pickle
import tkinter as tk
from tkinter import filedialog
from load_map import load_map


rect_width = 25
rect_height = 25

win_width = rect_width * 30
win_height = rect_height * 30

col_num = 30
row_num = 30

clock = pygame.time.Clock()

pygame.init()


class wall(object):
    def __init__(self, x, y, color, id):
        self.x = x
        self.y = y
        self.color = color
        self.id = id

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, rect_width, rect_height))


def redraw_game_win():
    window.fill((0, 0, 0))
    for bloc in walls:
        bloc.draw(window)
    moving.draw(window)
    window.blit(text, text.get_rect())
    pygame.display.update()


def save_file():
    root = tk.Tk()
    save_path = tk.filedialog.asksaveasfilename(
        initialdir="Pygame\\PacMan\\saved maps"
    )
    root.destroy()
    return save_path


window = pygame.display.set_mode((win_width, win_height))

div_w = win_width // (col_num)
div_h = win_height // (row_num)

walls = []
moving = wall(0, 0, (0, 0, 255), 0)
w_id = 1

font = pygame.font.Font("freesansbold.ttf", 15)

cooldown = 0
mode = "wall"
erase = False
x_border = False
y_border = False
lunched = True
while lunched:
    clock.tick(15)
    text = font.render(f"Mode : {mode}", True, (255, 255, 255))

    # cooldown to prevent the spam of "r"
    if cooldown > 0:
        cooldown += 1
    if cooldown > 4:
        cooldown = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] == 1 and x_border is False:
        moving.x += div_w
    if keys[pygame.K_LEFT] == 1:
        moving.x -= div_w
    if keys[pygame.K_UP] == 1:
        moving.y -= div_h
    if keys[pygame.K_DOWN] == 1 and y_border is False:
        moving.y += div_h
    if keys[pygame.K_SPACE] == 1:
        if erase:
            for wall1 in walls:
                if wall1.y == moving.y and wall1.x == moving.x:
                    walls.pop(walls.index(wall1))
        else:
            walls += [wall(moving.x, moving.y, moving.color, w_id)]
            w_id += 1
    if keys[pygame.K_r] == 1 and erase is False and cooldown == 0:
        moving.color = (255, 0, 0)
        cooldown = 1
        erase = True
        mode = "erase"
    if keys[pygame.K_r] == 1 and erase is True and cooldown == 0:
        moving.color = (0, 0, 255)
        cooldown = 1
        erase = False
        mode = "wall"
    if keys[pygame.K_s] == 1:
        save_path = save_file()
        with open(save_path, "wb") as f:
            pickle.dump(walls, f)
    if keys[pygame.K_l] == 1:
        walls = load_map()

    # --------Borders-----------
    if moving.x + rect_width >= win_width:
        x_border = True
    elif moving.x <= 0:
        moving.x = 0
    else:
        x_border = False
    if moving.y + rect_height >= win_height:
        y_border = True
    elif moving.y <= 0:
        moving.y = 0
    else:
        y_border = False
    # --------------------------

    redraw_game_win()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False

pygame.quit()

