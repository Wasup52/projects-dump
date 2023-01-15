from pynput.mouse import Button, Controller
import time


mouse = Controller()

time.sleep(1)

mouse.position = (1720, 1025)

# mouse.click(Button.left, 1)

time.sleep(0.5)

mouse.position = (1720, 975)

# mouse.click(Button.left, 1)

print("done")
