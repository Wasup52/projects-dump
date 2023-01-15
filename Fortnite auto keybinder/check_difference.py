import json


def check_difference(data, custom_keybinds):

    same_keybind = []
    cont_count = 0
    global_cat_count = 0
    global_cont_count = 0
    passed = False

    for categorie in custom_keybinds.keys():

        for control in custom_keybinds[categorie].keys():

            passed = False

            data_cat_list = list(data.keys())

            for cat in range(global_cat_count, len(data_cat_list)):
                data_cont_list = list(data.keys())[cat]

                if passed:
                    cont_count = 0
                else:
                    cont_count = global_cont_count

                for cont in range(cont_count, len(list(data[data_cont_list].keys()))):
                    comparaison_keybind = data[data_cont_list][
                        list(data[data_cont_list].keys())[cont]
                    ]

                    if (
                        custom_keybinds[categorie][control] == comparaison_keybind
                        and control != list(data[data_cont_list].keys())[cont]
                    ):
                        print(
                            control,
                            " and ",
                            list(data[data_cont_list].keys())[cont],
                            " have the same keybind",
                        )

                        if same_keybind.count(control) < 1:
                            same_keybind += [control]
                        else:
                            same_keybind = same_keybind
                        
                    else:
                        pass

                passed = True

            global_cont_count += 1
        global_cont_count = 0
        global_cat_count += 1

    output = ""
    for k in range(0, len(same_keybind)):
        output += same_keybind[k] + ","

    with open("Fortnite auto keybinder\\Data\\similar keybind.txt", "w") as f:
        f.write(output)

    print(output)

with open("Fortnite auto keybinder\\Data\\data.json", "r") as f:
    data = json.load(f)

with open(
    "Fortnite auto keybinder\\Custom_Keybinds\\output2.json",
    "r",
) as f:
    custom_keybinds = json.load(f)

check_difference(data, custom_keybinds)
