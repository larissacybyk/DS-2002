import time
import requests
import pandas as pd
import json


def api_call():
    url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi" 
    response = requests.request("GET", url)
    json_data = response.json()

    while response.status_code != 200:
        response = requests.request("GET", url)
        json_data = response.json()
    return json_data

def runbot():
    start_time = time.perf_counter()

    while time.perf_counter() - start_time < 3600:
        if (time.perf_counter() - start_time) % 60 == 0:
            #call api and update db
            json_data = api_call()


# running
runbot()