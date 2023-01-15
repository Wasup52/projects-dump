import pygame
import pickle
import tkinter as tk
from tkinter import filedialog


class wall(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, rect_width, rect_height))


def load_map():
    root = tk.Tk()
    load_path = tk.filedialog.askopenfilename(
        initialdir="Pygame\\PacMan\\saved maps"
    )
    root.destroy()
    with open(load_path, "rb") as f:
        walls = pickle.load(f)

    for wall1 in walls:
        for wall2 in walls:
            if wall1.x == wall2.x and wall1.id != wall2.id:
                if wall1.y == wall2.y:
                    walls.pop(walls.index(wall2))

    for wall1 in walls:
        for wall2 in walls:
            if wall1.x == wall2.x and wall1.y == wall2.y:
                if wall1.id != wall2.id:
                    walls.pop(walls.index(wall2))

    return walls


# walls = load_map()

# print(len(walls))

# pygame.init()

# rect_width = 25
# rect_height = 25

# win_width = rect_width * 30
# win_height = rect_height * 30

# window = pygame.display.set_mode((win_width, win_height))


# lunched = True
# while lunched:
#     window.fill((0, 255, 0))
#     for wall in walls:
#         wall.draw(window)

#     pygame.display.update()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             lunched = False

# pygame.quit()
