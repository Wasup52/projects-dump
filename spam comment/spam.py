from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as Keyboard
import time
import random

t1 = time.time()

mouse = Controller()
keyboard = Keyboard()

with open("spam insta\\words.txt", "r") as f:
    words = f.readlines()

words_plus = []
for word in words:
    if word.count("pluriel") == 1:
        word_plus = f"les {word.split()[0]}"
        words_plus += [word_plus]
    elif word.count("masculin") == 1:
        if word.split()[0][0] == "a":
            word_plus = f"l'{word.split()[0]}"
        elif word.split()[0][0] == "e":
            word_plus = f"l'{word.split()[0]}"
        else:
            word_plus = f"le {word.split()[0]}"
        words_plus += [word_plus]
    elif word.count("feminin") == 1:
        if word.split()[0][0] == "a":
            word_plus = f"l'{word.split()[0]}"
        elif word.split()[0][0] == "e":
            word_plus = f"l'{word.split()[0]}"
        else:
            word_plus = f"la {word.split()[0]}"
        words_plus += [word_plus]

print(words_plus)

# for word in words_plus:
#     wait = random.randint(3, 10)
#     time.sleep(wait)

#     r = random.randint(0, 3)

#     if r == 0:
#         msg = f"pour mettre {word} à l'abri"
#     elif r == 1:
#         msg = f"{word} va être a l'abri"
#     elif r == 2:
#         msg = f"tout pour {word}"
#     else:
#         msg = f"pour mettre {word} en sécurité"

#     mouse.position = (1206, 825)
#     mouse.click(Button.left, 1)
#     keyboard.type(msg)
#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
#     print(msg)

# t2 = time.time()

# print(f"runed for {t2 - t1}")
