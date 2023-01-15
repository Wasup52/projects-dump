with open("word list\\word list a trier.txt", encoding="utf8") as f:
    lines = f.readlines()

sorted_list = []

for line in lines:
    final = ""
    line = line.strip("\n")
    if len(line.split(" ")) > 3:
        pass
    else:
        line += "\n"
        line = line.encode("utf8")
        sorted_list += [line]

with open("word list\\word list avec bug.txt", "bw") as f:
    f.writelines(sorted_list)

print("done")
