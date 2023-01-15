import random


for k in range(0, 100):
    r = random.randint(0, 100)
    r2 = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    r3 = str(r2[0]) + str(r2[1]) + str(r2[2]) + str(r2[3]) + str(r2[4])
    r4 = random.randint(1, 4)

    if r4 == 1:
        ext = ".txt"
    elif r4 == 2:
        ext = ".py"
    elif r4 == 3:
        ext = ".jpg"
    elif r4 == 4:
        ext = ".png"

    with open(
        "Playing with file\\Files\\Files\\file"
        + r3
        + ext,
        "w",
    ) as f:
        f.write("")
