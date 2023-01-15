import random


for k in range(0, 100):
    r = random.randint(0, 100)
    r2 = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    r3 = str(r2[0]) + str(r2[1]) + str(r2[2]) + str(r2[3]) + str(r2[4])
    with open(
        "Playing with file\\Files\\Files\\file"
        + r3
        + ".txt",
        "w",
    ) as f:
        if r != 50:
            f.write("")
        else:
            f.write("test")
