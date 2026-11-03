import requests
import time

# Warframe items in the format of slugs
items = ["despoil"]#, "eternal_war", "infernum", "pilfering_swarm", 
         #"pilfering_strangledome", "razorwing_blitz", "volt_prime_set", "dual_viciss_set"]

# Header for displaying who you are, and what you want
headers = {
    "User-Agent": "Warframe-Price-Tracker  (parvisnguyen.ca; https://github.com/ParvisNguyen/Warframe-Price-Tracker) ",  
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
    first_price = data["data"]["sell"][0]["rank"]

    # Formats the 'slug' to replace all underscores, and uppercase the first letter of each word
    slug_format = slug.replace("_", " ").title()

    print (f"The lowest selling platinum cost for {slug_format} is {first_price}")
    time.sleep(0.5)

total = 0
for order in data["data"]["sell"]:
    total += order["platinum"]
    print (order["platinum"])
average = total / len(data["data"]["sell"])
print (average)