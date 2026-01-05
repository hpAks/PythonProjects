import json

import requests
google_sheet_get_url = "https://api.sheety.co/191f935a803a76b2575fbcb4c0cd4039/flightDeals/prices"
google_sheet_put_url = "https://api.sheety.co/191f935a803a76b2575fbcb4c0cd4039/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = requests.get(google_sheet_get_url)

    def get_rows_from_googleSheet(self):
        return self.data.json()['prices']

    def update_airport_code(self, id,json_data):
        url = google_sheet_put_url +"/"+str(id)
        json_data = "{ \"price\":"+str(json_data) +"}"
        json_data = json_data.replace("'","\"")
        data = json.loads(json_data)
        response = requests.put(url=url,json=data)