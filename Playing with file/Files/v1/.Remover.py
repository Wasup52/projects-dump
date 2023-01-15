import os

list = os.listdir(
    "Playing with file\\Files\\Files"
)

for k in range(0, len(list)):
    file = list[k]
    os.remove(
        "Playing with file\\Files\\Files\\"
        + file
    )
