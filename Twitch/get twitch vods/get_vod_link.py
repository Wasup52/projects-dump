import datetime
import hashlib
import requests

with open("Twitch\get twitch vods\_domains.txt", "r") as f:
    domains = f.readlines()


def totimestamp(dt, epoch=datetime.datetime(1970, 1, 1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10 ** 6) / 10 ** 6


def get(link, date):
    streamername = link.split("/")[1]
    vodID = link.split("/")[3]
    timestamp = date

    year = int(timestamp[:4])
    month = int(timestamp[5:7])
    day = int(timestamp[8:10])

    hour = int(timestamp[11:13])
    minute = int(timestamp[14:16])
    seconds = int(timestamp[17:])

    td = datetime.datetime(year, month, day, hour, minute, seconds)

    converted_timestamp = totimestamp(td)

    formattedstring = streamername + "_" + vodID + "_" + str(int(converted_timestamp))

    hash = str(hashlib.sha1(formattedstring.encode("utf-8")).hexdigest())

    requiredhash = hash[:20]

    finalformattedstring = requiredhash + "_" + formattedstring

    for domain in domains:
        domain = domain.strip("\n")
        url = f"{domain}/{finalformattedstring}/chunked/index-dvr.m3u8"
        try:
            r = requests.get(url)
            content = str(r.content)
            if content.count(f"#EXTM3U"):
                return url
        except:
            pass


# print(get("/aminematue/streams/42404211805", "2021-06-16 19:01:17"))
# https://d1m7jfoe9zdc1j.cloudfront.net/bf7a1b683c3f25ed0249_aminematue_42404211805_1623870077/chunked/index-dvr.m3u8

# print(get("/zwave69/streams/42371119852", "2021-06-16 20:29:48"))
# https://dgeft87wbj63p.cloudfront.net/66e1ae92b4c192d2dc0d_zwave69_42371119852_1623875388/chunked/index-dvr.m3u8
