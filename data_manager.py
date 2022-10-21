import os
import requests
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_HEADERS = {"Authorization": os.environ.get("SHEETY_HEADERS")}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = []
        self.get_sheet_data()

    def get_sheet_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.sheet_data = data["prices"]

    def update_iata(self, index: int, new_iata_code):
        row_data = self.sheet_data[index]
        row_data["iataCode"] = new_iata_code
        params = {"price": row_data}
        index += 2
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{index}", json=params)
        response.raise_for_status()
