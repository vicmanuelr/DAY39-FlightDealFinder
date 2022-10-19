import os
import requests

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.old_prices = []

    def get_old_prices(self) -> list:
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.old_prices = data["prices"]
        return self.old_prices



