import os
import shutil


Initial_folder = "Bluetooth battery\\"
Destination_folder = "Playing with file\\File mover\\Destination folder\\images\\"


lunched = True


def find_dir(path):
    inside_list = os.listdir(path)
    dir_list = []
    for element in inside_list:
        if element[1:].count(".") == 0 and element != ".gitignore":
            dir_list += [element]
    return dir_list


def look_for_images(path):
    file_list = os.listdir(path)
    print(path)

    for file_ in file_list:
        if file_[1:].count(".") != 0:
            L = file_.split(".")
            ext = L[1]
            if ext == "jpg" or ext == "png" or ext == "jpeg":
                shutil.move(path + "\\" + file_, Destination_folder + file_)


look_for_images(Initial_folder)
dir_list = find_dir(Initial_folder)

for dir_ in dir_list:
    print(Initial_folder + dir_)
    look_for_images(Initial_folder + dir_)
    sub_dirs = find_dir(Initial_folder + dir_)
    for sub_dir in sub_dirs:
        look_for_images(Initial_folder + dir_ + "\\" + sub_dir)

print(find_dir(Initial_folder))
