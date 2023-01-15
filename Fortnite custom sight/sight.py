import pygame
import win32api
import win32con
import win32gui
import os
from ctypes import windll

pygame.init()

clock = pygame.time.Clock()
win_width, win_height = (
    pygame.display.Info().current_w,
    pygame.display.Info().current_h,
)
screen = pygame.display.set_mode(
    (win_width, win_height), pygame.RESIZABLE | pygame.NOFRAME
)  # For borderless, use pygame.NOFRAME

fullscreen = False

# dark_red = (139, 0, 0)

# --- Set window transparency color ---
fuchsia = (255, 0, 128)  # Transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(
    hwnd,
    win32con.GWL_EXSTYLE,
    win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED,
)
win32gui.SetLayeredWindowAttributes(
    hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY
)
# -------------------------------------

windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001)

init_sight = [
    pygame.image.load(
        "Fortnite custom sight\\Images de viseurs\\red_default_dot.png"
    ),
    pygame.image.load(
        "Fortnite custom sight\\Images de viseurs\\red_default.png"
    ),
    pygame.image.load(
        "Fortnite custom sight\\Images de viseurs\\red_ring.png"
    ),
]
ready_sight = [
    pygame.image.load(
        "Fortnite custom sight\\Images de viseurs\\green_default_dot.png"
    ),
    pygame.image.load(
        "Fortnite custom sight\\Images de viseurs\\green_default.png"
    ),
    pygame.image.load(
        "Fortnite custom sight\\Images de viseurs\\green_ring.png"
    ),
]

sight_num = 0
current_scale, current_scale = init_sight[sight_num].get_size()
x_added = 0
y_added = 0

with open("Fortnite custom sight\data.txt", "r") as f:
    data = f.readlines()[0]
    data = data.split(" ")
    x_added = int(data[0])
    y_added = int(data[1])
    current_scale = int(data[2])

tick = 30
ready = False
launched = True
while launched:
    clock.tick(tick)

    x = win_width // 2 - current_scale // 2 + x_added
    y = win_height // 2 - current_scale // 2 + y_added

    if not ready:
        sight = pygame.transform.scale(
            init_sight[sight_num], (current_scale, current_scale)
        )
    else:
        sight = pygame.transform.scale(
            ready_sight[sight_num], (current_scale, current_scale)
        )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_KP_PLUS] == 1:
        current_scale += 1
    if keys[pygame.K_KP_MINUS] == 1:
        current_scale -= 1
    if keys[pygame.K_UP] == 1:
        y_added -= 1
    if keys[pygame.K_DOWN] == 1:
        y_added += 1
    if keys[pygame.K_LEFT] == 1:
        x_added -= 1
    if keys[pygame.K_RIGHT] == 1:
        x_added += 1
    if keys[pygame.K_KP1] == 1:
        sight_num = 0
    if keys[pygame.K_KP2] == 1:
        sight_num = 1
    if keys[pygame.K_KP3] == 1:
        sight_num = 2
    if keys[pygame.K_l] == 1:
        tick = 1
        ready = True
    if keys[pygame.K_RETURN] == 1:
        os.startfile(
            "Ω ahk test\\no recoil.ahk"
        )

    screen.fill(fuchsia)  # Transparent background
    screen.blit(sight, (x, y))
    pygame.display.update()

pygame.quit()

if ready:
    with open("Fortnite custom sight\data.txt", "w") as f:
        data = str(x_added) + " " + str(y_added) + " " + str(current_scale)
        f.writelines(data)
