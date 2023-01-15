from email import header
import requests

# payload = [
#     {
#         "operationName": "FilterableVideoTower_Videos",
#         "variables": {
#             "limit": 30,
#             "channelOwnerLogin": "aminematue",
#             "broadcastType": None,
#             "videoSort": "TIME",
#         },
#         "extensions": {
#             "persistedQuery": {
#                 "version": 1,
#                 "sha256Hash": "a937f1d22e269e39a03b509f65a7490f9fc247d7f83d6ac1421523e3b68042cb",
#             }
#         },
#     },
# ]

payload = [
    {
        "operationName": "VideoMetadata",
        "variables": {
            "channelLogin": "aminematue",
            "videoID": "1601100638"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "49b5b8f268cdeb259d75b58dcb0c1a748e3b575003448a2333dc5cdafd49adad"
            }
        }
    }
]

url = "https://gql.twitch.tv/gql"

headers = {
    "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
}

response = requests.post(url, headers=headers, json=payload)
print(response.text)