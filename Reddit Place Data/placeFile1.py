import csv
import gzip
import random
import pygame


class Pixel(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 1
        self.height = 1

    def draw(self, window):
        # pygame.draw.rect(window, (0, 0, 255), self.hitbox, 1)
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


WIN_WIDTH = 2000
WIN_HEIGHT = 2000

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT) )
clock = pygame.time.Clock()


with gzip.open("/root/Documents/Reddit Place Data/2022_place_canvas_history-000000000001.csv.gz", "rt", encoding="utf8") as csvFile:
    lines = csv.reader(csvFile)

    pixels = []
    lunched = True
    while lunched:
        # clock.tick(30)
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lunched = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                # color = (r,g,b)
                color = pygame.Color("#7EED56")
                pixel = Pixel(event.pos[0], event.pos[1], color)
                pixels.append(pixel)
        
        # for pixel in pixels:
        #     pixel.draw(window)

        for i, line in enumerate(lines):
            if 0 != i:
                x = int(line[3].split(",")[0])
                y = int(line[3].split(",")[1])
                color = pygame.Color(line[2])
                Pixel(x, y, color).draw(window)
        
                pygame.display.update()


pygame.quit()

