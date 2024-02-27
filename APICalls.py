# pip install requests (in console)
import requests
import pandas as pd
import json

country = input("Please enter a country name: ")
country = country.strip()
url = "https://restcountries.com/v3.1/name/" + country 
response = requests.request("GET", url)
json_data = response.json()

if response.status_code >= 400: 
    print("Invalid input, please try again.")
    exit()
if response.status_code != 200:
    print("Please try again")
    exit()
cap = json_data[0]["capital"][0]
pop = json_data[0]["population"]
print("Capital: " + cap)
print("Population: " + str(pop))

data = [country.capitalize(), cap, pop]
df = pd.DataFrame([data], columns=["country", "capital", "population"])

print(df)

# writing to json file
# new_country = {"country": country, "capital": cap, "population": pop}

new_country = df.to_dict(orient="records")[0]
try:
    file = open("APICalls.json", 'r+')
except:
    file = open("APICalls.json", 'a')
try:
    file_data = json.load(file)
    file_data["countries"].append(new_country)
    file.seek(0)
    json.dump(file_data, file, indent=4)      
except:
    json_obj = {"countries":[new_country]}
    json2 = json.dump(json_obj, file, indent=4)
file.close()