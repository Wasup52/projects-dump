import json
import requests
import random
from quickchart import QuickChart

quickchart_url = "https://quickchart.io/chart/create"


def get_charl_url(data, labels, colors):
    # post_data = {
    #     "chart": {
    #         "type": "pie",
    #         "data": {
    #             "datasets": [
    #                 {"data": data, "backgroundColor": colors, "label": "Dataset 1"}
    #             ],
    #             "labels": labels,
    #         },
    #         "options": {"title": {"display": "true", "text": "Your banking stats"}},
    #     }
    # }

    # response = requests.post(quickchart_url, json=post_data)

    # if response.status_code != 200:
    #     return "Error:", response.text
    # else:
    #     chart_response = json.loads(response.text)
    #     return chart_response

    qc = QuickChart()
    qc.width = 500 * 2
    qc.height = 300 * 2
    qc.background_color = "#ffffff00"
    qc.config = {
        "type": "doughnut",
        "data": {
            "datasets": [
                {"data": data, "backgroundColor": colors, "label": "Dataset 1"}
            ],
            "labels": labels,
        },
        "options": {"title": {"display": "true", "text": "Your banking stats"}},
    }
    return qc.get_short_url()


data = []
labels = []
colors = []

for k in range(0, 24):
    data += [random.randint(0, 1000)]
    labels += [k]
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    colors += [f"rgb{rgb}"]

print(get_charl_url(data, labels, colors))

