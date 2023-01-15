import requests
import os

base_url = "https://s3-us-east-2.amazonaws.com/apkdecompiler-decompiled/qpazcvqr8x.apk/"

with open("Web scraping\get decompiled apk\\sources.txt") as f:
    lines = f.readlines()

for line in lines:
    url = base_url + line.strip("\n")
    line2 = line.replace("/", "\\").strip("\n").split("\\")
    path = ["apk_decompiled"] + line2[: len(line2) - 1]
    name = line2[len(line2) - 1]

    file_path = "apk_decompiled\\" + line.replace("/", "\\").strip("\n")

    for k in range(1, len(path) + 1):
        string_path = ""
        for path_element in path[0:k]:
            string_path += path_element + "\\"
        try:
            os.mkdir(string_path)
        except:
            pass

    print(url)
    r = requests.get(url)

    with open(file_path, "wb") as f:
        f.write(r.content)


# url = base_url + lines[0].strip("\n")
# print(url)

# r = requests.get(url)

# with open("file_path.java", "wb") as f:
#     f.write(r.content)
