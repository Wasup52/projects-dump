import os


# dir_path = "D:\Robin\Galerie\dossier sd pas ok\Soirée chez Philippe _ok_"


def list_dir(dir_path):
    file_names = os.listdir(dir_path)

    dif_id_len = []
    ids = []
    for file_name in file_names:
        if file_name.count("_"):
            file_id = file_name.split("_")[1]
        else:
            file_id = file_name.split("-")[1]
            # file_id = file_id.split(".")[0]
        ids += [file_id]

        dif_id_len += [len(file_id)]

    ids.sort()

    dif_id_len = list(dict.fromkeys(dif_id_len))
    dif_id_len.sort()
    ids_lens = dif_id_len

    sort = []
    sorted_ids = []
    for i in range(0, len(ids_lens)):
        for id_ in ids:
            if len(id_) == ids_lens[i]:
                sorted_ids += [id_]
            else:
                pass

    sorted_names = []
    for id_ in sorted_ids:
        for file_name in file_names:
            if file_name.count(id_):
                sorted_names += [file_name]

    _files = []
    for file_name in sorted_names:
        if file_name.count("_") and file_name.count("VID") == 0:
            _files += [file_name]
        else:
            pass

    vid_files = []
    for file_name in sorted_names:
        if file_name.count("_") and file_name.count("VID"):
            vid_files += [file_name]
        else:
            pass

    files_w_dash = []
    for file_name in sorted_names:
        if file_name.count("_") == 0:
            files_w_dash += [file_name]
        else:
            pass

    _files.sort()

    sorted_file_names = _files + files_w_dash + vid_files

    return sorted_file_names


# print(os.listdir(dir_path))
# print(list_dir(dir_path))

# for name in list_dir(dir_path):
#     name = '"' + name + '"' + ","
#     print(name)
