import requests

url = "https://api.warframe.market/v2/orders/item/despoil/top"

headers = {
    "User-Agent": "Warframe-Price-Tracker",  
    "Accept": "application/json",                             
}

response = requests.get(url, headers=headers)

data = response.json()

print (data["data"]["sell"][0]["platinum"])

# print(data.keys())