import requests
import time

items = ["despoil", "eternal_war"]

# Header for displaying who you are, and what you want
headers = {
    "User-Agent": "Warframe-Price-Tracker",  
    "Accept": "application/json",                             
}

for slug in items:
    # API URL
    url = f"https://api.warframe.market/v2/orders/item/{slug}/top"

    # Request with url and header into 'response'
    response = requests.get(url, headers=headers)

    # Converts JSON text from response into a Python dictionary
    data = response.json()

    # Takes only the number for the cost of the first/lowest Sell posting
    first_price = data["data"]["sell"][0]["platinum"]

    slug_format = slug.replace("_", " ")
    slug_format = slug_format.title()

    print (f"The first platinum cost for {slug_format} is {first_price}")
    time.sleep(0.5)