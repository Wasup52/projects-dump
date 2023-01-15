import requests
from bs4 import BeautifulSoup
import time


header = {
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"content-length": "378",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"origin": "https://www.reseau-stan.com",
"referer": "https://www.reseau-stan.com/",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
"x-requested-with": "XMLHttpRequest",
}

payload_callot = {"requete":"tempsreel_submit",
"requete_val[arret]": "stop_point:GST:SP:VACAO0",
"requete_val[arret_name]": "Callot",
"requete_val[ligne_id]": "2329",
"requete_val[ligne_omsid]": "line:GST:1-97",
"requete_val[numlignepublic]": "T1",
"requete_val[color]": "#0",
"requete_val[background]": "#E30613",
"requete_val[libelle]": "Tempo 1 - Essey Mouzimpré <> Vandoeuvre Chu Brabois"}

payload_standre = {"requete":"tempsreel_submit",
"requete_val[arret]": "stop_point:GST:SP:VAAND0",
"requete_val[arret_name]": "Saint+André",
"requete_val[ligne_id]": "2329",
"requete_val[ligne_omsid]": "line:GST:1-97",
"requete_val[numlignepublic]": "T1",
"requete_val[color]": "#0",
"requete_val[background]": "#E30613",
"requete_val[libelle]": "Tempo 1 - Essey Mouzimpré <> Vandoeuvre Chu Brabois"}

payload_vel = {"requete":"tempsreel_submit",
"requete_val[arret]": "stop_point:GST:SP:VALOD0",
"requete_val[arret_name]": "Vélodrome",
"requete_val[ligne_id]": "2329",
"requete_val[ligne_omsid]": "line:GST:1-97",
"requete_val[numlignepublic]": "T1",
"requete_val[color]": "#0",
"requete_val[background]": "#E30613",
"requete_val[libelle]": "Tempo 1 - Essey Mouzimpré <> Vandoeuvre Chu Brabois"}

def chack_if_in_station(payload, header, cookies, direction):
    r_callot = requests.post('https://www.reseau-stan.com/?type=476',headers=header, data=payload, cookies=cookies)

    soup = BeautifulSoup(r_callot.text, 'html.parser')

    dirs = soup.find_all("li")

    ts = []
    c = 0
    for dir in dirs:
        g_text = dir.get_text("a", {"class":"tpsreel-temps-item large-1 "})
        
        if g_text.count(direction):
            for el in g_text.split("a"):
                if el.count("min"):
                    # print(el)
                    ts.append(el)
                    c += 1
            if c <= 1:
                print(f"Tram in station, other tram comming in {ts[0]}")
                return True
            else:
                print(f"Tram arrives in {ts[0]}")
                return False
        else:
            print("Direction not found")
            return False
            

direction = "Direction Vandoeuvre CHU Brabois"
# direction = "Direction Essey Mouzimpré"

# in_station = False
# while not in_station:
while True:
    session = requests.Session()
    response = session.get('https://www.reseau-stan.com')
    cookies = session.cookies.get_dict()

    in_station = chack_if_in_station(payload_standre, header, cookies, direction)

    time.sleep(10)

# print(time.time())