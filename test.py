import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 34, "name": "Kekv", "views": 1000},
        {"likes": 64545, "name": "Youtube", "views": 1000000},
        {"likes": 10, "name": "Slava", "views": 1000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/6")
print(response.json())