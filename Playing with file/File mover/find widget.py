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


def look_for_widget(path):
    file_list = os.listdir(path)
    for file_ in file_list:
        if file_[1:].count(".") != 0:
            if file_.count("widget") != 0:
                print(path + "\\" + file_)


look_for_widget(Initial_folder)
dir_list = find_dir(Initial_folder)

for dir_ in dir_list:
    look_for_widget(Initial_folder + dir_)
    sub_dirs = find_dir(Initial_folder + dir_)
    for sub_dir in sub_dirs:
        look_for_widget(Initial_folder + dir_ + "\\" + sub_dir)

print("done")
