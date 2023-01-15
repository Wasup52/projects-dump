import json
from check_difference import check_difference


nl = "\n"
tab = "    "
sleep = "sleep 100"
lunch_key = "NumpadEnter"
mouse_start_pos = (560, 316)
cancel_button_pos = (848, 316)
ahk_output = ""
nlt = nl + tab
nls = nlt + sleep + nl

with open("Fortnite auto keybinder\\Data\\data.json", "r") as f:
    data = json.load(f)

with open(
    "Fortnite auto keybinder\\Custom_Keybinds\\output2.json",
    "r",
) as f:
    custom_keybind = json.load(f)

with open("Fortnite auto keybinder\\Data\\scroll data.json", "r") as f:
    scroll_data = json.load(f)

check_difference(data, custom_keybind)

with open("Fortnite auto keybinder\\Data\\similar keybind.txt", "r") as f:
    similar_keys = f.readline()
    similar_keys = similar_keys.strip(", ")
    similar_keys = similar_keys.split(",")
    print(similar_keys)

previous_control = list(custom_keybind["Movement"].keys())[0]
previous_categorie = list(custom_keybind.keys())[0]

ahk_output += lunch_key + "::" + "\n"
ahk_output += "{" + nl
ahk_output += (
    tab
    + "Send, {Escape}"
    + nlt
    + "MouseMove, 1876, 44"
    + nlt
    + "Click"
    + nls
    + tab
    + "MouseMove, 1876, 100"
    + nlt
    + "Click"
    + nls
    + tab
    + "MouseMove, 1104, 46"
    + nlt
    + "Click"
    + nls
)
ahk_output += tab + f"MouseMove, {mouse_start_pos[0]}, {mouse_start_pos[1]}" + nls


for categorie in custom_keybind:
    for control in custom_keybind[categorie]:

        # print(control, categorie, previous_control, previous_categorie)
        # print(
        #     scroll_data[categorie][control]
        #     - scroll_data[previous_categorie][previous_control]
        # )

        ahk_output += tab + (
            "Click "
            + str(
                scroll_data[categorie][control]
                - scroll_data[previous_categorie][previous_control]
            )
            + ", WheelDown"
            + nls
        )
        if custom_keybind[categorie][control] == "Right Mouse Button":
            ahk_output += tab +"Click" + nlt + "Send, " + "{RButton}" + nls
        elif custom_keybind[categorie][control] == "Left Mouse Button":
            ahk_output += tab +"Click" + nlt + "Send, " + "{LButton}" + nls
        elif custom_keybind[categorie][control] == "Middle Mouse Button":
            ahk_output += tab +"Click" + nlt + "Send, " + "{MButton}" + nls
        elif custom_keybind[categorie][control] == "Shift":
            ahk_output += tab +"Click" + nlt + "Send, " + "{Shift}" + nls
        elif custom_keybind[categorie][control] == "Left Alt":
            ahk_output += tab +"Click" + nlt + "Send, " + "{Alt}" + nls
        elif custom_keybind[categorie][control] == "Left Ctrl":
            ahk_output += tab +"Click" + nlt + "Send, " + "{Control}" + nls
        elif custom_keybind[categorie][control] == "Tab":
            ahk_output += tab +"Click" + nlt + "Send, " + "{Tab}" + nls
        elif custom_keybind[categorie][control] == "Space Bar":
            ahk_output += tab +"Click" + nlt + "Send, " + "{Space}" + nls
        elif custom_keybind[categorie][control] == "BackSpace":
            ahk_output += tab +"Click" + nlt + "Send, " + "{Backspace}" + nls
        elif custom_keybind[categorie][control] == "Enter":
            ahk_output += tab +"Click" + nlt + "Send, " + "{Enter}" + nls
        elif custom_keybind[categorie][control] == "CapsLock":
            ahk_output += tab +"Click" + nlt + "Send, " + "{CapsLock}" + nlt + "SetCapsLockState, AlwaysOff" + nls
        elif custom_keybind[categorie][control] == "Mouse Down":
            ahk_output += tab +"Click" + nlt + "Send, " + "{WheelDown}" + nls
        elif custom_keybind[categorie][control] == "Mouse Up":
            ahk_output += tab +"Click" + nlt + "Send, " + "{WheelUp}" + nls
        elif custom_keybind[categorie][control] == "\u00e9":
            ahk_output += tab +"Click" + nlt + "Send, é" + nls
        elif custom_keybind[categorie][control] == None:
            ahk_output += (
                tab
                + f"MouseMove, {cancel_button_pos[0]}, {cancel_button_pos[1]}"
                + nl
                + tab
                + "Click"
                + nl
            )
        else:
            ahk_output += (
                tab
                + "Click"
                + nlt
                + "Send, "
                + str(custom_keybind[categorie][control])
                + nls
            )

        for k in range(0, len(similar_keys)):
            if control == similar_keys[k]:
                ahk_output += (
                    tab
                    + "MouseMove, 1105, 784"
                    + nlt
                    + "Click"
                    + nlt
                    + f"MouseMove, {mouse_start_pos[0]}, {mouse_start_pos[1]}"
                    + nls
                )
                break

        previous_control = control
        previous_categorie = categorie


ahk_output += "}"

with open("Fortnite auto keybinder\output.ahk", "w") as f:
    f.write(ahk_output)

print("done")
