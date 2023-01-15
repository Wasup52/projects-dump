import pygame


col_num = 7
row_num = 6

win_width = 358
win_height = 338
clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Connect 4")
window = pygame.display.set_mode((win_width, win_height))

# jetons = [
#     pygame.image.load("Pygame\Puissance 4\sprits\jetons jaune.png"),
#     pygame.image.load("Pygame\Puissance 4\sprits\jetons rouge.png"),
# ]
# board_sprit = pygame.image.load("Pygame\\Puissance 4\\sprits\\board.png")


class piont(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), 15)


def check_win():
    # Vertical win
    for r in range(row_num):
        for c in range(col_num - 3):
            if (
                pionts[r][c] != 0
                and pionts[r][c + 1] != 0
                and pionts[r][c + 2] != 0
                and pionts[r][c + 3] != 0
            ):
                if (
                    pionts[r][c].color == pionts[r][c + 1].color
                    and pionts[r][c + 1].color == pionts[r][c + 2].color
                    and pionts[r][c + 2].color == pionts[r][c + 3].color
                ):
                    return True
    # Horizontal win
    for c in range(col_num):
        for r in range(row_num - 3):
            if (
                pionts[r][c] != 0
                and pionts[r + 1][c] != 0
                and pionts[r + 2][c] != 0
                and pionts[r + 3][c] != 0
            ):
                if (
                    pionts[r][c].color == pionts[r + 1][c].color
                    and pionts[r + 1][c].color == pionts[r + 2][c].color
                    and pionts[r + 2][c].color == pionts[r + 3][c].color
                ):
                    return True
    # Diagonal win (left to right)
    for r in range(row_num - 3):
        for c in range(col_num - 3):
            if (
                pionts[r][c] != 0
                and pionts[r + 1][c + 1] != 0
                and pionts[r + 2][c + 2] != 0
                and pionts[r + 3][c + 3] != 0
            ):
                if (
                    pionts[r][c].color == pionts[r + 1][c + 1].color
                    and pionts[r + 1][c + 1].color == pionts[r + 2][c + 2].color
                    and pionts[r + 2][c + 2].color == pionts[r + 3][c + 3].color
                ):
                    return True
    # Diagonal win (right to left)
    for r in range(row_num - 3):
        for c in range(col_num - 3):
            if (
                pionts[r][col_num - c - 1] != 0
                and pionts[r + 1][col_num - (c + 1) - 1] != 0
                and pionts[r + 2][col_num - (c + 2) - 1] != 0
                and pionts[r + 3][col_num - (c + 3) - 1] != 0
            ):
                if (
                    pionts[r][col_num - c - 1].color
                    == pionts[r + 1][col_num - (c + 1) - 1].color
                    and pionts[r + 1][col_num - (c + 1) - 1].color
                    == pionts[r + 2][col_num - (c + 2) - 1].color
                    and pionts[r + 2][col_num - (c + 2) - 1].color
                    == pionts[r + 3][col_num - (c + 3) - 1].color
                ):
                    return True


def redraw_game_win():
    window.fill((0, 0, 0))
    pygame.draw.rect(
        window, (0, 0, 255), (0, div_h + 5, win_width, win_height - div_h - 5)
    )
    for blank in blanks:
        blank.draw(window)
    for k in range(0, len(pionts)):
        for p in pionts[k]:
            if p != 0:
                p.draw(window)
    playing.draw(window)

    # board = pygame.transform.scale(board_sprit, (win_width, win_height - div_h))
    # window.blit(board, (0, div_h))
    # window.blit(jetons[0], (50, 100))
    # window.blit(jetons[1], (200, 100))

    pygame.display.update()


div_w = win_width // (col_num + 1)
div_h = win_height // (row_num + 2) + 2

blanks = []
for i in range(1, row_num + 1):
    for k in range(1, col_num + 1):
        blanks += [piont(div_w * k, div_h * (i + 1), (0, 0, 0))]

pionts = [[0 for k in range(col_num)] for i in range(row_num)]

turn = 0
winner = 0
k = 1
cooldown = 0
playing = piont(div_w, div_h, (255, 0, 0))

lunched = True
while lunched:
    clock.tick(30)

    if cooldown > 0:
        cooldown += 1
    if cooldown > 5:
        cooldown = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] == 1 and cooldown == 0:
        if k > 1:
            playing.x -= div_w
            k -= 1
        cooldown = 1

    if keys[pygame.K_RIGHT] == 1 and cooldown == 0:
        if k < 7:
            playing.x += div_w
            k += 1
        cooldown = 1

    if keys[pygame.K_RETURN] == 1 and cooldown == 0:
        if turn == 0:
            if pionts[0][k - 1] == 0:
                pionts[0][k - 1] = piont(playing.x, div_h * 7, playing.color)
            elif pionts[1][k - 1] == 0:
                pionts[1][k - 1] = piont(playing.x, div_h * 6, playing.color)
            elif pionts[2][k - 1] == 0:
                pionts[2][k - 1] = piont(playing.x, div_h * 5, playing.color)
            elif pionts[3][k - 1] == 0:
                pionts[3][k - 1] = piont(playing.x, div_h * 4, playing.color)
            elif pionts[4][k - 1] == 0:
                pionts[4][k - 1] = piont(playing.x, div_h * 3, playing.color)
            elif pionts[5][k - 1] == 0:
                pionts[5][k - 1] = piont(playing.x, div_h * 2, playing.color)

            if check_win():
                winner = 1
                lunched = False

            cooldown += 1

            playing.color = (255, 255, 0)
            turn = 1

        if turn == 1 and cooldown == 0:
            if pionts[0][k - 1] == 0:
                pionts[0][k - 1] = piont(playing.x, div_h * 7, playing.color)
            elif pionts[1][k - 1] == 0:
                pionts[1][k - 1] = piont(playing.x, div_h * 6, playing.color)
            elif pionts[2][k - 1] == 0:
                pionts[2][k - 1] = piont(playing.x, div_h * 5, playing.color)
            elif pionts[3][k - 1] == 0:
                pionts[3][k - 1] = piont(playing.x, div_h * 4, playing.color)
            elif pionts[4][k - 1] == 0:
                pionts[4][k - 1] = piont(playing.x, div_h * 3, playing.color)
            elif pionts[5][k - 1] == 0:
                pionts[5][k - 1] = piont(playing.x, div_h * 2, playing.color)

            if check_win():
                winner = 2
                lunched = False

            cooldown += 1

            playing.color = (255, 0, 0)
            turn = 0

    redraw_game_win()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False

pygame.quit()

print(f"P{winner} WON !!!")
