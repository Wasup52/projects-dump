import random


with open("word list\\word list.txt", "br") as f:
    lines = f.readlines()

random.shuffle(lines)

with open("word list\\word list shuffle.txt", "bw") as f:
    f.writelines(lines)

print("done")
