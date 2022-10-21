import os
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_KEY = os.environ.get("TEQUILA_KEY")


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self, flight_data):
        self.sheet_data = flight_data

    def get_iata_code(self):
        header = {
            "apikey": TEQUILA_KEY
        }
        params = {
            "term": self.sheet_data["city"],
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": "true"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)
        iata_code = data["locations"][0]["id"]
        return iata_code
