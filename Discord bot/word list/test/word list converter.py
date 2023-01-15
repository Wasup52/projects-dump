with open("word list\\word list shuffle.txt", encoding="utf8") as f:
    lines = f.readlines()

final = ""
doubles = 0

for line in lines:
    if lines.count(line) != 1:
        doubles += 1
        lines.pop(lines.index(line) - 1)
        print(line, lines.count(line))
    line = line.strip("\n")
    final = final + "," + line
    final = final.strip(",")

# print(doubles)
final = [final.encode("utf8")]

with open("word list\\word list suffle with coma .txt", "bw") as f:
    f.writelines(final)

print("done")
