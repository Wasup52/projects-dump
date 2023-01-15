import pygame
import pickle


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
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), self.radius)


point = circle(0, 0, 0)
clic = False
L = []
lunched = True
while lunched:
    # clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clic = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clic = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_c] == 1:
        window.fill((0, 0, 0))
        point.x = -1
        point.y = -1
        L = []

    if keys[pygame.K_s]:
        with open("Pygame\Drawing\data.txt", "wb") as f:
            pickle.dump(L, f)

    if keys[pygame.K_l]:
        with open("Pygame\Drawing\data.txt", "rb") as f:
            L = pickle.load(f)
            print(L)
        for points in L:
            print(points)
            points.draw(window)

    if clic:
        mx, my = pygame.mouse.get_pos()
        point.x = mx
        point.y = my
        point.radius = 4
        L += [circle(point.x, point.y, point.radius)]

    point.draw(window)

    pygame.display.update()

pygame.quit()
