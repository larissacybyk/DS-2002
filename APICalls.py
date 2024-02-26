# pip install requests (in console)
import requests
import pandas as pd

print("Enter 'e' to exit")
df = pd.DataFrame([], columns=["Country", "Capital", "Population"])
country = input("Please enter a country name: ")
while (country != "e"):
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

    data = [country.capitalize(), cap, pop]
    df.loc[len(df.index)] = data

    print(df)
    country = input("Please enter a country name: ")
