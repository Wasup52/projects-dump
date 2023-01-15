with open(
    "E-mail creation bot\\Bots\\Yahoo\\.Identifiant.txt",
    "r",
) as f:
    lines = f.readlines()


for k in range(3, len(lines)):
    lines[k] = ""


with open(
    "E-mail creation bot\\Bots\\Yahoo\\.Identifiant.txt",
    "w",
) as f:
    f.writelines(lines)

print("Done")
