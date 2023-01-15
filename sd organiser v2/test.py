import os
import progress.bar

initial_dir = ""Galerie\\backup not ok"

dirs_list = os.listdir(initial_dir)

for k, dir_name in enumerate(dirs_list):
    print(dir_name)
    files_names = os.listdir(initial_dir + "\\" + dir_name)

    for file_name in files_names:
        print(f"\t{file_name}")

    if k == 4:
        break
