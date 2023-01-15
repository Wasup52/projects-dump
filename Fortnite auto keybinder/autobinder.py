import json
import tkinter as tk
import cv2
import os
import json
import tkinter as tk
from tkinter import filedialog
import cv2
import os


with open("Fortnite auto keybinder\data.json", "r") as f:
    data = json.load(f)

mouse_start_pos = (560, 316)
lunch_key = "NumpadeEnter"
crouch_key = False
use_key = False

titles = []

movement = []
combat = []
building = []
communication = []
emote = []
miscellaneous = []
vehicles_motorboat = []

categories = [movement, combat, building, communication, emote, miscellaneous]

output = {}

input_box_width = 20
space_between_box = 1
c = 0

os.startfile(
    "Fortnite auto keybinder\\Other keys.ahk"
)


class input_box(object):
    def __init__(self, row, column, width, height, name, keybind):
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.name = name
        self.keybind = keybind

    def keypressed(self):
        global waiting
        global crouch_key
        global use_key

        waiting = True

        ### --- Detect mouse event ---#
        def mouse(event, x, y, flags, param):
            global waiting
            if event == cv2.EVENT_LBUTTONDOWN:
                self.keybind = "Left Mouse Button"
                self.button.config(text=self.keybind)
                cv2.destroyAllWindows()
                waiting = False
            if event == cv2.EVENT_RBUTTONDOWN:
                self.keybind = "Right Mouse Button"
                self.button.config(text=self.keybind)
                cv2.destroyAllWindows()
                waiting = False
            if event == cv2.EVENT_MBUTTONDOWN:
                self.keybind = "Middle Mouse Button"
                self.button.config(text=self.keybind)
                cv2.destroyAllWindows()
                waiting = False

        ### --------------------------#

        if self.name == "Crouch":
            crouch_key = True
        if self.name == "Use":
            use_key = True

        while waiting:
            waiting_frame = cv2.imread("Fortnite auto keybinder\Black.jpg")
            cv2.imshow("waiting...", waiting_frame)

            cv2.setMouseCallback("waiting...", mouse)

            key = cv2.waitKey(1)

            if key != -1:  # only if a key is pressed

                key = chr(key)

                if key == "	":
                    if crouch_key == True:
                        building[0].keybind = "Tab"
                        building[11].keybind = "Tab"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Tab"
                        miscellaneous[10].keybind = "Tab"
                        miscellaneous[11].keybind = "Tab"
                        miscellaneous[12].keybind = "Tab"
                    self.keybind = "Tab"
                elif key == " ":
                    if crouch_key == True:
                        building[0].keybind = "Space Bar"
                        building[11].keybind = "Space Bar"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Space Bar"
                        miscellaneous[10].keybind = "Space Bar"
                        miscellaneous[11].keybind = "Space Bar"
                        miscellaneous[12].keybind = "Space Bar"
                    self.keybind = "Space Bar"
                elif key == "":
                    if crouch_key == True:
                        building[0].keybind = "BackSpace"
                        building[11].keybind = "BackSpace"
                    elif use_key == True:
                        miscellaneous[9].keybind = "BackSpace"
                        miscellaneous[10].keybind = "BackSpace"
                        miscellaneous[11].keybind = "BackSpace"
                        miscellaneous[12].keybind = "BackSpace"
                    self.keybind = "BackSpace"
                elif key == "\r":
                    if crouch_key == True:
                        building[0].keybind = "Enter"
                        building[11].keybind = "Enter"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Enter"
                        miscellaneous[10].keybind = "Enter"
                        miscellaneous[11].keybind = "Enter"
                        miscellaneous[12].keybind = "Enter"
                    self.keybind = "Enter"
                elif key == "A":
                    if crouch_key == True:
                        building[0].keybind = "CapsLock"
                        building[11].keybind = "CapsLock"
                    elif use_key == True:
                        miscellaneous[9].keybind = "CapsLock"
                        miscellaneous[10].keybind = "CapsLock"
                        miscellaneous[11].keybind = "CapsLock"
                        miscellaneous[12].keybind = "CapsLock"
                    self.keybind = "CapsLock"
                elif key == "Î":
                    if crouch_key == True:
                        building[0].keybind = "Shift"
                        building[11].keybind = "Shift"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Shift"
                        miscellaneous[10].keybind = "Shift"
                        miscellaneous[11].keybind = "Shift"
                        miscellaneous[12].keybind = "Shift"
                    self.keybind = "Shift"
                elif key == "Â":
                    if crouch_key == True:
                        building[0].keybind = "Left Ctrl"
                        building[11].keybind = "Left Ctrl"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Left Ctrl"
                        miscellaneous[10].keybind = "Left Ctrl"
                        miscellaneous[11].keybind = "Left Ctrl"
                        miscellaneous[12].keybind = "Left Ctrl"
                    self.keybind = "Left Ctrl"
                elif key == "â":
                    if crouch_key == True:
                        building[0].keybind = "Left Alt"
                        building[11].keybind = "Left Alt"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Left Alt"
                        miscellaneous[10].keybind = "Left Alt"
                        miscellaneous[11].keybind = "Left Alt"
                        miscellaneous[12].keybind = "Left Alt"
                    self.keybind = "Left Alt"
                elif key == "/":
                    if crouch_key == True:
                        building[0].keybind = "Mouse Down"
                        building[11].keybind = "Mouse Down"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Mouse Down"
                        miscellaneous[10].keybind = "Mouse Down"
                        miscellaneous[11].keybind = "Mouse Down"
                        miscellaneous[12].keybind = "Mouse Down"
                    self.keybind = "Mouse Down"
                elif key == "*":
                    if crouch_key == True:
                        building[0].keybind = "Mouse Up"
                        building[11].keybind = "Mouse Up"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Mouse Up"
                        miscellaneous[10].keybind = "Mouse Up"
                        miscellaneous[11].keybind = "Mouse Up"
                        miscellaneous[12].keybind = "Mouse Up"
                    self.keybind = "Mouse Up"
                elif key == "[":
                    if crouch_key == True:
                        building[0].keybind = "Xbutton2"
                        building[11].keybind = "Xbutton2"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Xbutton2"
                        miscellaneous[10].keybind = "Xbutton2"
                        miscellaneous[11].keybind = "Xbutton2"
                        miscellaneous[12].keybind = "Xbutton2"
                    self.keybind = "Xbutton2"
                elif key == "]":
                    if crouch_key == True:
                        building[0].keybind = "Xbutton1"
                        building[11].keybind = "Xbutton1"
                    elif use_key == True:
                        miscellaneous[9].keybind = "Xbutton1"
                        miscellaneous[10].keybind = "Xbutton1"
                        miscellaneous[11].keybind = "Xbutton1"
                        miscellaneous[12].keybind = "Xbutton1"
                    self.keybind = "Xbutton1"
                elif key == ".":
                    if crouch_key == True:
                        building[0].keybind = None
                        building[11].keybind = None
                    elif use_key == True:
                        miscellaneous[9].keybind = None
                        miscellaneous[10].keybind = None
                        miscellaneous[11].keybind = None
                        miscellaneous[12].keybind = None
                    self.keybind = None
                else:
                    if crouch_key == True:
                        building[0].keybind = key
                        building[11].keybind = key
                    elif use_key == True:
                        miscellaneous[9].keybind = key
                        miscellaneous[10].keybind = key
                        miscellaneous[11].keybind = key
                        miscellaneous[12].keybind = key
                    self.keybind = key

                if crouch_key == True:
                    building[0].button.config(text=str(building[0].keybind))
                    building[11].button.config(text=str(building[11].keybind))
                    crouch_key = False
                elif use_key == True:
                    miscellaneous[9].button.config(text=str(miscellaneous[9].keybind))
                    miscellaneous[10].button.config(text=str(miscellaneous[10].keybind))
                    miscellaneous[11].button.config(text=str(miscellaneous[11].keybind))
                    miscellaneous[12].button.config(text=str(miscellaneous[12].keybind))
                    use_key = False
                self.button.config(text=str(self.keybind))

                cv2.destroyAllWindows()
                waiting = False

    def place_(self, root):
        label = tk.Label(root, text=self.name)
        label.grid(row=self.row, column=self.column)
        self.button = tk.Button(
            root, width=self.width, text=self.keybind, command=self.keypressed
        )
        self.button.grid(row=self.row, column=self.column + 1)


class title(object):
    def __init__(self, row, column, name):
        self.row = row
        self.column = column
        self.name = name

    def place_(self, root):
        label = tk.Label(root, text=self.name, font=("bold"))
        label.grid(row=self.row, column=self.column)


root = tk.Tk()
root.title("Keybinds")
root.geometry("640x640")


def apply():
    k = 0
    keys_list = list(data.keys())
    for categorie in categories:
        output[keys_list[k]] = {}
        for inputs in categorie:
            keybind = inputs.keybind
            if keybind != "":
                output[keys_list[k]][inputs.name] = keybind
            else:
                output[keys_list[k]][inputs.name] = None
        k += 1
    with open("Fortnite auto keybinder\output2.json", "w") as f:
        json.dump(output, f)

def load_keybind():
    filename = tk.filedialog.askopenfilename(initialdir="Fortnite auto keybinder\\Custom_Keybinds", filetype=(("json", "*.json"), ("txt", "*.txt")), title="Select saved keydind")
    
    categorie_cont = 0

    with open(filename, "r") as f:
        saved_keybind = json.load(f)
    
    for categorie in categories:
        for control in categorie:
            control.keybind = saved_keybind[list(saved_keybind.keys())[categorie_cont]][control.name]
            control.button.config(text=str(control.keybind))
        print(list(saved_keybind.keys())[categorie_cont], categorie_cont)
        categorie_cont += 1
        

for categorie in data.keys():
    if categorie == "Movement":
        titles += [title(0 + c, 0, categorie)]
        c += 1
        for keys in data[categorie].keys():
            movement += [
                input_box(0 + c, 0, input_box_width, 0, keys, data[categorie][keys])
            ]
            c += space_between_box
    elif categorie == "Combat":
        titles += [title(0 + c, 0, categorie)]
        c += 1
        for keys in data[categorie].keys():
            combat += [
                input_box(0 + c, 0, input_box_width, 0, keys, data[categorie][keys])
            ]
            c += space_between_box
    elif categorie == "Building":
        titles += [title(0 + c, 0, categorie)]
        c += 1
        for keys in data[categorie].keys():
            building += [
                input_box(0 + c, 0, input_box_width, 0, keys, data[categorie][keys])
            ]
            c += space_between_box
    elif categorie == "Communication":
        titles += [title(0 + c, 0, categorie)]
        c += 1
        for keys in data[categorie].keys():
            communication += [
                input_box(0 + c, 0, input_box_width, 0, keys, data[categorie][keys])
            ]
            c += space_between_box
    elif categorie == "Emote":
        titles += [title(0 + c, 0, categorie)]
        c += 1
        for keys in data[categorie].keys():
            emote += [
                input_box(0 + c, 0, input_box_width, 0, keys, data[categorie][keys])
            ]
            c += space_between_box
    elif categorie == "Miscellaneous":
        titles += [title(0 + c, 0, categorie)]
        c += 1
        for keys in data[categorie].keys():
            miscellaneous += [
                input_box(0 + c, 0, input_box_width, 0, keys, data[categorie][keys])
            ]
            c += space_between_box
    elif categorie == "Vehicles - Motorboat":
        titles += [title(0 + c, 0, categorie)]
        c += 1
        for keys in data[categorie].keys():
            vehicles_motorboat += [
                input_box(0 + c, 0, input_box_width, 0, keys, data[categorie][keys])
            ]
            c += space_between_box

### ----- Scrollbar ----- ###
def myfunction(envent):
    canvas.configure(scrollregion=canvas.bbox("all"), width=400, height=400)


frame_1 = tk.Frame(root, width=50, height=100, bd=1)
frame_1.place(x=10, y=100)

canvas = tk.Canvas(frame_1)
frame_2 = tk.Frame(canvas)
scrollbar = tk.Scrollbar(frame_1, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=frame_2, anchor="nw")
frame_2.bind("<Configure>", myfunction)
### --------------------- ###

### ------ Placing ------ ###
for categorie in categories:
    for control in categorie:
        control.place_(frame_2)
for title in titles:
    title.place_(frame_2)
### --------------------- ###

apply_button = tk.Button(root, text="Apply", width=10, height=1, command=apply)
apply_button.place(x=520, y=600)

load_button = tk.Button(root, text="Load saved keybind", width=15, height=1, command=load_keybind)
load_button.place(x=400, y=600)

root.mainloop()

os.system("TASKKILL /F /IM AutoHotkey.exe")
