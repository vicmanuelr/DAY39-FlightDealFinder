import os
import requests
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_HEADERS = {"Authorization": os.environ.get("SHEETY_HEADERS")}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = []
        self.get_sheet_data()

    def get_sheet_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        print(data)
        self.sheet_data = data["prices"]

    def update_iata(self, index: int):
        params = {"price": self.sheet_data[index]}
        index += 2
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{index}", json=params)
        response.raise_for_status()
        print(response.text)

