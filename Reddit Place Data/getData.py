import requests

for i in range(78):
    if i < 10:
        index = f"0{i}"
    else:
        index = f"{i}"
    
    url = f"https://placedata.reddit.com/data/canvas-history/2022_place_canvas_history-0000000000{index}.csv.gzip"
    print(url)
    r = requests.get(url, allow_redirects=True)

    path = f"/root/Documents/Reddit Place Data/2022_place_canvas_history-0000000000{index}.csv.gz"

    with open(path, "wb") as f:
        f.write(r.content)