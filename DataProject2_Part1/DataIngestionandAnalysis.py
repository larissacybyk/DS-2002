import time
import requests
import pandas as pd
import json
import sqlite3


def api_call():
    url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi" 
    response = requests.request("GET", url)
    json_data = response.json()

    while response.status_code != 200:
        response = requests.request("GET", url)
        json_data = response.json()
    return json_data

def runbot():
    #creation of SQLite database
    conn = sqlite3.connect('data_ingestion.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (factor integer, pi real, time text)")
    start_time = time.perf_counter()
    curr = int(time.perf_counter() - start_time)
    while curr < 3600:
        if curr % 60 == 0:
            #call api and update db
            json_data = api_call()
            cursor.execute('''
            INSERT OR IGNORE INTO data (factor, pi, time)
            VALUES (?, ?, ?)
        ''', (json_data['factor'], json_data['pi'], json_data['time']))
            conn.commit()
        time.sleep(1)
        curr = int(time.perf_counter() - start_time)
            


# running
runbot()