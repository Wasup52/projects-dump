import pygame
from pylab import *


win_width = 940
win_height = 680
clock = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((win_width, win_height))


class circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, window):
        pygame.draw.circle(window, (0, 255, 0), (self.x, self.y), self.radius)


class line(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, window):
        pygame.draw.line(window, (0, 255, 0), (self.x1, self.y1), (self.x2, self.y2))


def f(x):
    return x ** 2


X = [i + win_width // 2 for i in range(-100, 100 + 1)]
points = []
lines = []
lunched = True
drawn = False
while lunched:

    for x in X:
        y = win_height - f(x - win_width // 2)
        points += [circle(x, y, 2)]
    for point in points:
        point.draw(window)

    for k in range(-100, 100 + 1):
        x1 = X[k - 1]
        y1 = win_height - f(x1 - win_width // 2)
        x2 = X[k]
        y2 = win_height - f(x2 - win_width // 2)
        lines += [line(x1, y1, x2, y2)]
    for joint in lines:
        joint.draw(window)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False


pygame.quit()
