import pyautogui as pgui

while True:
    mouse_position = pgui.position()
    mouse_position = list(mouse_position)
    x = mouse_position[0]
    y = mouse_position[1]

    print(x, y)

# url
# 191 52
# close chat
# 1890, 1010
# join
# 958 344
# statut
# 897,1008
# quitter
# 1002, 801
# ignorer
# 1105 758
# coin:
# haut gauche,1663,1016   haut droite,1682,1016
# bas gauche,1663,1028    bas droite,1682,1028
# coin 2:
# haut gauche,1256,152
#                          bas droite,1279,175
# password
# 645 475
# conection
# 635 575

