# Look for a specific word in a bunch of files and return the path of the files wich contain it
import os

p = 0
word_to_find = "test"

path = "Playing with file\\Files\\Files"
list = os.listdir(path)

for k in range(2, len(list)):
    file = list[k]
    with open(
        "Playing with file\\Files\\Files\\"
        + file,
        "r",
    ) as f:

        lines = f.readlines()
        count = lines.count(word_to_find)
        if count != 0:
            print(f.name, count)
            p = p + 1
if p == 0:
    print("no files contain '", word_to_find, "' in ", path)
