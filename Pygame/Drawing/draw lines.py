import pygame
import pickle


win_width = 940
win_height = 680
clock = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((win_width, win_height))


class line(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, window):
        pygame.draw.line(window, (0, 255, 0), (self.x1, self.y1), (self.x2, self.y2))


limit = line(0, 0, 0, 0)
clic = 0
L = []
lunched = True
while lunched:
    # clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clic == 0:
                mx, my = pygame.mouse.get_pos()
                limit.x1 = mx
                limit.y1 = my
                clic += 1
            elif clic == 1:
                mx, my = pygame.mouse.get_pos()
                limit.x2 = mx
                limit.y2 = my
                limit.draw(window)
                clic += 1
                L += [line(limit.x1, limit.y1, limit.x2, limit.y2)]
            else:
                mx, my = pygame.mouse.get_pos()
                limit.x1 = limit.x2
                limit.y1 = limit.y2
                limit.x2 = mx
                limit.y2 = my
                limit.draw(window)
                L += [line(limit.x1, limit.y1, limit.x2, limit.y2)]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_c] == 1:
        window.fill((0, 0, 0))
        limit.x1 = 0
        limit.y1 = 0
        clic = 0
        L = []

    if keys[pygame.K_DOWN] == 1:
        clic = 0

    if keys[pygame.K_s]:
        with open("Pygame\Drawing\data.txt", "wb") as f:
            pickle.dump(L, f)

    if keys[pygame.K_l]:
        with open("Pygame\Drawing\data.txt", "rb") as f:
            L = pickle.load(f)
        for lines in L:
            lines.draw(window)

    pygame.display.update()

pygame.quit()
