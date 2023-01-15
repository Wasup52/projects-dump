import cv2
import numpy as np
import pyautogui as pgui

import pygame

import tkinter as tk
from tkinter import filedialog, Text
import os

# Start of code to get the path of the image we want to analyse
root = tk.Tk()


def img_path():
    filename = tk.filedialog.askopenfilename(
        initialdir="cv2\\Color detector\\Img to analyse",
        title="Select Image",
        filetypes=(("png", "*.png"), ("jpg", "*.jpg")),
    )
    with open(
        "cv2\\Color detector\\Data.txt",
        "w",
    ) as f:
        f.write(filename)
    root.destroy()
    root.quit()


canvas = tk.Canvas(root, height=80, width=340, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button = tk.Button(
    frame,
    text="Choose Image To ANnalyse",
    padx=10,
    pady=5,
    fg="black",
    command=img_path,
)
button.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button2 = tk.Button

root.mainloop()

with open(
    "cv2\\Color detector\\Data.txt", "r"
) as f:
    img_path = f.read()
# End of code to get the path of the image we want to analyse

# place the pygame window to (275,750) (without this the pygame window's initial position is behind the cv2 window)
os.environ["SDL_VIDEO_WINDOW_POS"] = "275,750"

pygame.init()
pygame.display.set_caption("RGB color visualisation")
screen = pygame.display.set_mode((340, 280))

frame = cv2.imread(img_path)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

height, width, _ = frame.shape

# You have to place the cv2 window on the top left to make the mouse position's acuarate

while True:

    black_bg = cv2.imread(
        "cv2\\Color detector\\Black.jpg"
    )
    mouse_position = pgui.position()
    mouse_position = list(mouse_position)
    # (9, 32) are the coordinates of the top left corner of the cv2 window when it is on the top left corner of the screen
    # so this set it to (0,0)
    x = mouse_position[0] - 9
    y = mouse_position[1] - 32

    # If mouse position is out of the window don't actualize the mouse position
    if x > width - 1 or x < 0:
        x = width - 1
    if y > height - 1:
        y = height - 1

    coord_hsv = str(hsv[y][x])
    coord_rgd = str(rgb[y][x])

    screen.fill(rgb[y][x])
    pygame.display.flip()

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(black_bg, f"HSV : {coord_hsv}", (10, 20), font, 0.5, (255, 255, 255), 2)
    cv2.putText(
        black_bg, f"RGB : {coord_rgd}", (10, 100), font, 0.5, (255, 255, 255), 2
    )

    cv2.imshow("Info", black_bg)
    cv2.imshow("hsv", hsv)

    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break

