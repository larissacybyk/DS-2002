# pip install requests (in notebook)
import requests
import pandas as pd


country = input("Please enter a country name: ")
country = country.strip().lower()
url = "https://restcountries.com/v3.1/name/" + country
response = requests.request("GET", url)
json = response.json()
print(json)
# data = json_data.loads(json_data)
# df = pd.DataFrame(json_data)
# print(df.head(10), "\n")