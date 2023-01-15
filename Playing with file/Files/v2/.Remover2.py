import os

list_txt = os.listdir(
    "Playing with file\\File mover\\Destination folder\\.txt\\"
)
list_py = os.listdir(
    "Playing with file\\File mover\\Destination folder\\.py\\"
)
list_jpg = os.listdir(
    "Playing with file\\File mover\\Destination folder\\.jpg\\"
)
list_other = os.listdir(
    "Playing with file\\File mover\\Destination folder\\other\\"
)


for k in range(0, len(list_txt)):
    file = list_txt[k]
    os.remove(
        "Playing with file\\File mover\\Destination folder\\.txt\\"
        + file
    )

for k in range(0, len(list_py)):
    file = list_py[k]
    os.remove(
        "Playing with file\\File mover\\Destination folder\\.py\\"
        + file
    )

for k in range(0, len(list_jpg)):
    file = list_jpg[k]
    os.remove(
        "Playing with file\\File mover\\Destination folder\\.jpg\\"
        + file
    )

for k in range(0, len(list_other)):
    file = list_other[k]
    os.remove(
        "Playing with file\\File mover\\Destination folder\\other\\"
        + file
    )
