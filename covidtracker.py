import requests
import json
import os

def countryName(cn):
    req = requests.get(f"https://api.covid19api.com/country/{cn}")
    data = list(json.loads(req.text))
    data = data[-1]
    date = "/".join(data['Date'].replace("T00:00:00Z","").split("-")[::-1])
    print(f"Country: {data['Country']}")
    print(f"Confirmed: {data['Confirmed']}")
    print(f"Deaths: {data['Deaths']}")
    print(f"Recovered: {data['Recovered']}")
    print(f"Active: {data['Active']}")
    print(f"Data: {date}")

def globalData():
    req = requests.get(f"https://api.covid19api.com/summary")
    data = dict(json.loads(req.text)["Global"])
    print()
    print("*" * 20)
    print(f"New Confirmed: {data['NewConfirmed']}")
    print(f"Total Confirmed: {data['TotalConfirmed']}")
    print(f"New Deaths: {data['NewDeaths']}")
    print(f"Total Deaths: {data['TotalDeaths']}")
    print(f"New Recovered: {data['NewRecovered']}")
    print(f"Total Recovered: {data['TotalRecovered']}")
    print("*" * 20)
    print()

while True:
    print("*" * 20)
    print("Choose a search option")
    print("")
    print("Search By Country Name - [n]")
    print("Global Data - [g]")
    print("Quit - [q]")
    print("*" * 20)
    op = str(input()).lower()

    if op == "n":
        cn = str(input("Country Name: ")).lower()
        cn = cn.replace(" ","-")

        countryName(cn)
    
    elif op == "g":
        globalData()
    
    else:
        break