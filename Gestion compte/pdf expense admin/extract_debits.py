def extract_debits(f):
    temp = []
    lines = f.readlines()
    for line in lines:
        line = line.split("/")
        for strings in line:
            if strings.count("FACT"):
                strings = strings.strip("\n")
                strings = strings.split(" ")
                for string in strings:
                    if string.count(","):
                        temp += [string]
                    if string.count("FACT"):
                        pass

    debits = []
    for price in temp:
        N = []
        S = price[6:]
        S = S.split(",")
        for num in S[1]:
            N += num
        debit = S[0] + "." + N[0] + N[1]
        debits += [debit]

    return debits


# with open("Gestion compte\\..temp data.txt", "r") as f:
#     debit = extract_debits(f)

# print(debit)
