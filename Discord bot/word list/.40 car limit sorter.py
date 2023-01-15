with open("word list\\word list.txt", "br") as f:
    lines = f.readlines()

sorted_list = []

for line in lines:
    line = line.strip(b"\r\n")
    if len(line) > 40:
        print(line, len(line))
        pass
    else:
        sorted_list += [line + b"\n"]

with open("word list\\word list.txt", "bw") as f:
    f.writelines(sorted_list)

print("done")
