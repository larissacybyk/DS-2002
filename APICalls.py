# pip install requests (in notebook)
import requests
import pandas as pd


country = input("Please enter a country name: ")
country = country.strip().lower()
url = "https://restcountries.com/v3.1/name/" + country
response = requests.request("GET", url)
json = response.json()

if response.status_code >= 400: 
    print("Invalid input, please try again.")
    exit()

cap = json[0]["capital"][0]
pop = json[0]["population"]
print("Capital: " + cap)
print("Population: " + str(pop))