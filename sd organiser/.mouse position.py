import pyautogui as pgui

while True:
    mouse_position = pgui.position()
    mouse_position = list(mouse_position)
    x = mouse_position[0]
    y = mouse_position[1]

    print(x, y)

# 1370 215
# 1475 1010

# 1130 210
# 1380 1015

# 1280 210
# 1380 445
