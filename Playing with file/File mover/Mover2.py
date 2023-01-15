import os
import shutil


Initial_folder = (
    "Playing with file\\Files\\Files\\"
)
Destination_folder_txt = "Playing with file\\File mover\\Destination folder\\.txt\\"
Destination_folder_py = "Playing with file\\File mover\\Destination folder\\.py\\"
Destination_folder_jpg = "Playing with file\\File mover\\Destination folder\\.jpg\\"
Destination_folder_other = "Playing with file\\File mover\\Destination folder\\other\\"


# def lunched():
#     list = os.listdir(Initial_folder)
#     if len(list) != 0:
#         return True
#     else:
#         return False

lunched = True

while lunched is True:
    list = os.listdir(Initial_folder)
    if len(list) != 0:

        list = os.listdir(Initial_folder)
        L = list[0].split(".")
        ext = L[1]

        if ext == "txt":
            shutil.move(Initial_folder + list[0], Destination_folder_txt + list[0])
        elif ext == "py":
            shutil.move(Initial_folder + list[0], Destination_folder_py + list[0])
        elif ext == "jpg":
            shutil.move(Initial_folder + list[0], Destination_folder_jpg + list[0])
        else:
            shutil.move(Initial_folder + list[0], Destination_folder_other + list[0])
    else:
        lunched = False

