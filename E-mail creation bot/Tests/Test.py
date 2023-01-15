import random


def r():
    s = random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 4)
    s2 = ""
    for k in range(0, len(s)):
        s2 = s2 + s[k]
    return s2


s2 = r()
username = "test" + s2
s3 = r()
password = "pass" + s3

print(username)
print(password)

with open("Identifiant", "a+") as f:
    line = (
        "|           "
        + username
        + "            |         "
        + password
        + "      |"
        + "\n"
    )
    f.write(line)
