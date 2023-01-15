import os

path = "D:\Robin\Galerie\\backup ok"

dirs_list = os.listdir("D:\Robin\Galerie\\backup not ok")

for dir_name in dirs_list:
    try:
        print(dir_name)
        os.mkdir(path + "\\" + dir_name)
    except:
        pass
