import os
import requests
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_HEADERS = {"Authorization": os.environ.get("SHEETY_HEADERS")}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data_list = []
        self.users_list = []
        self.get_sheet_data()
        self.get_users()

    def get_sheet_data(self):
        """This will get data in a list from spreadsheet"""
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.data_list = data["prices"]

    def update_airport(self, index: int, new_iata_code, new_airport_name):
        """This method is in charge of writing the new IATA and airport to spreadsheet"""
        new_row = self.data_list[index]
        new_row["iataCode"] = new_iata_code
        new_row["airportName"] = new_airport_name
        params = {"price": new_row}
        index += 2
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{index}", json=params)
        response.raise_for_status()

    def update_price(self, index: int, new_price):
        """This method will update price in spreadsheet if new lower price is found"""
        new_row = self.data_list[index]
        new_row["lowestPrice"] = new_price
        params = {"price": new_row}
        index += 2
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{index}", json=params)
        response.raise_for_status()

    def get_users(self):
        """This will get data in a list from spreadsheet users sheet"""
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.users_list = data["users"]
