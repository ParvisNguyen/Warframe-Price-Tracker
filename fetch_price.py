import requests
import time
import os
import psycopg
from dotenv import load_dotenv

# Loads database settings from .env so password is not stored in code
load_dotenv()

# Connected to PostgreSQL database running in Docker
conn = psycopg.connect(
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    dbname = os.getenv ("DB_NAME"),
    user = os.getenv ("DB_USER"),
    password = os.getenv("DB_PASSWORD")
)

# The cursor sends SQL commands through the connection
cur = conn.cursor()

# Warframe items in the format of slugs (all lowercase with underscores)
items = ["despoil", "eternal_war", "infernum", "pilfering_swarm", 
         "pilfering_strangledome", "razorwing_blitz", "volt_prime_set", "dual_viciss_set"]

# Header for displaying who you are, and what you want
headers = {
    "User-Agent": "Warframe-Price-Tracker (parvisnguyen.ca; https://github.com/ParvisNguyen/Warframe-Price-Tracker) ",  
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

    # Formats the 'slug' to replace all underscores, and uppercase the first letter of each word
    slug_format = slug.replace("_", " ").title()

    print (f"The lowest selling platinum cost for {slug_format} is {first_price}")


    # Parameterized query: values sent seperately from SQL to prevent SQL injection
    cur.execute(
    "INSERT INTO prices (item_slug, lowest_price) VALUES (%s ,%s)", 
    (slug, first_price)
    )

    print("Inserted into database")

    time.sleep(0.5)

conn.commit()
conn.close()