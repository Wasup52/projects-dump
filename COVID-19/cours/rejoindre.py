from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as Keyboard
import time

clock = (time.localtime().tm_hour, time.localtime().tm_min)
t = time.sleep

maths_url = "https://lycee.cned.fr/cv/227312/350"
physics_url = "https://lycee.cned.fr/cv/227207/58"
si_url = "https://lycee.cned.fr/cv/227259/287"

mouse = Controller()
keyboard = Keyboard()

mouse.position = (191, 52)
mouse.click(Button.left, 1)

keyboard.press(Key.ctrl)
keyboard.press("a")
keyboard.release("a")
keyboard.release(Key.ctrl)
keyboard.press(Key.backspace)
keyboard.release(Key.backspace)
keyboard.type(maths_url)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

mouse.position = (958, 344)
mouse.click(Button.left, 1)
