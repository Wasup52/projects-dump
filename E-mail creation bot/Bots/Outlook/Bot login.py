with open(
    "E-mail creation bot\\Bots\\Outlook\\.Identifiant.txt",
    "r",
) as f:
    L = f.readlines()
    line = f.readlines()
    for k in range(3, len(L)):
        UP = L[k]
        sp = UP.split()
        username = sp[1]
        password = sp[3]
        f.close()
        print(username, password)
