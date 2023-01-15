import random


with open("word list\\word list.txt", "br") as f:
    lines = f.readlines()

random.shuffle(lines)

final_str = b""
for line in lines:
    line = line.strip(b"\r\n")
    final_str = final_str + line + b","

final_str = [final_str.strip(b",")]

with open("word list\\.Shuffled word list.txt", "bw") as f:
    f.writelines(final_str)

print("done")
