import pygame
import pickle


win_width = 940
win_height = 680
clock = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((win_width, win_height))


class blocs(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        # pygame.draw.rect(window, (0, 0, 255), self.hitbox, 1)
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height))


bloc = blocs(0, 0, 0, 0)
clic = 0
L = []
lunched = True
while lunched:
    # clock.tick(30)
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            L += [blocs(bloc.x, bloc.y, bloc.width, bloc.height)]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_c] == 1:
        window.fill((0, 0, 0))
        bloc.x = 0
        bloc.y = 0
        clic = 0
        L = []

    if keys[pygame.K_DOWN] == 1:
        bloc.width -= 1
        bloc.height -= 1

    if keys[pygame.K_UP] == 1:
        bloc.width += 1
        bloc.height += 1

    if keys[pygame.K_LEFT]:
        pass

    if keys[pygame.K_s]:
        with open("Pygame\Drawing\data.txt", "wb") as f:
            pickle.dump(L, f)

    if keys[pygame.K_l]:
        with open("Pygame\Drawing\data.txt", "rb") as f:
            L = pickle.load(f)
        for lines in L:
            lines.draw(window)

    mx, my = pygame.mouse.get_pos()
    bloc.x = mx - bloc.width // 2
    bloc.y = my - bloc.height // 2
    bloc.draw(window)

    for pist in L:
        pist.draw(window)

    pygame.display.update()

pygame.quit()
