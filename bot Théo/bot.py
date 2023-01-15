from pynput.keyboard import Key, Controller as k_controller
from pynput.mouse import Button, Controller as m_controller
import time
import tkinter as tk

keyboard = k_controller()
mouse = m_controller()

doing_something = False
duree_activation = 1  # in hour
time_between_refresh = 20  # in minutes
t1 = time.time()
t2 = time.time()

root = tk.Tk()


def get_entry():
    global time_between_refresh
    global duree_activation
    global doing_something
    time_between_refresh = time_between_refresh_entry.get()
    duree_activation = duree_activation_entry.get()
    # doing_something = doing_something_true.getboolean()
    print(time_between_refresh, duree_activation, doing_something)


time_between_refresh_txt = ""
time_between_refresh_label = tk.Label(
    root, text="temps entre refresh", font=("bold", 14), pady=20
)
time_between_refresh_label.grid(row=0, column=0)
time_between_refresh_entry = tk.Entry(root, textvariable=time_between_refresh_txt)
time_between_refresh_entry.grid(row=0, column=1)

duree_activation_txt = ""
duree_activation_label = tk.Label(root, text="durée d'activation", font=("bold", 14))
duree_activation_label.grid(row=0, column=3)
duree_activation_entry = tk.Entry(root, textvariable=duree_activation_txt)
duree_activation_entry.grid(row=0, column=4)

doing_something_true = tk.Checkbutton(root, text="qqc en même temps")
doing_something_true.grid(row=1, column=1)
doing_something_false = tk.Checkbutton(root, text="rien en même temps")
doing_something_false.grid(row=1, column=3)

ok_btn = tk.Button(root, text="Ok", font=("bold", 14), width=10, command=get_entry)
ok_btn.grid(row=2, column=2)

root.mainloop()

# while t2 - t1 < duree_activation * 360:
#     keyboard.press(Key.f5)
#     keyboard.release(Key.f5)

#     time.sleep(time_between_refresh * 60)

#     t2 = time.time()

# --- mode if you're doing something at the same time ---
if doing_something:
    while t2 - t1 < duree_activation * 360:
        count = 0
        while count != 50:
            mouse.position = (560, 1050)
            if count == 49:
                mouse.click(Button.left)
            count += 1

        time.sleep(0.5)

        count = 0
        while count != 50:
            mouse.position = (540, 1020)
            if count == 49:
                mouse.click(Button.left)
            count += 1

        time.sleep(0.5)

        keyboard.press(Key.f5)
        keyboard.release(Key.f5)

        time.sleep(1)

        keyboard.press(Key.alt_l)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.alt_l)

        t2 = time.time()
# -------------------------------------------------------
