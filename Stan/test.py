from bs4 import BeautifulSoup

soup = BeautifulSoup(open("tram.html"), "html.parser")

dirs = soup.find_all("li")
directions = []

for dir in dirs:
    splited = dir.get_text("a", {"class":"tpsreel-temps-item large-1 "}).strip("Callota").replace("a","a-").split("-")
    string = ""
    for k in range(len(splited)):
        if splited[k].count("min"):
            pass
        else:
            string += splited[k]
    directions.append(string.strip("a"))

print(directions)

# direction = "Direction Vandoeuvre Chu Brabois"
direction = "Direction Essey Mouzimpré"

c = 0
ts = []
for dir in dirs:
    g_text = dir.get_text("a", {"class":"tpsreel-temps-item large-1 "})
    if g_text.count(direction):
        for el in g_text.split("a"):
            if el.count("min"):
                # print(el)
                ts.append(el)
                c += 1
        if c <= 1:
            print("Tram in station")
        else:
            print(f"Tram arrives in {ts[0]}")


# for icons in chu_bradbois.find_all("i"):
#     if str(icons) == '<i class="icon-car1"></i>':
#         print("Tram in station")