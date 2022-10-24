import os
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_KEY = os.environ.get("TEQUILA_KEY")


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, spreadsheet_data):
        self.sheet_data = spreadsheet_data

    def get_airport(self):
        """This method will return the iata code and airport name from tequila api"""
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
        iata_code = data["locations"][0]["id"]
        airport_name = data["locations"][0]["name"]
        return iata_code, airport_name

    def search_cheap_flights(self, departure_airport, date_from, date_to, destination_airport, currency, min_stay,
                             max_stay, adults, children, infants, flight_type, destination_city):
        header = {
            "apikey": TEQUILA_KEY
        }
        params = {
            "fly_from": departure_airport,
            "fly_to": destination_airport,
            "date_from": date_from,
            "date_to": date_to,
            "curr": currency,
            "nights_in_dst_from": min_stay,
            "nights_in_dst_to": max_stay,
            "flight_type": flight_type,
            "adults": adults,
            "children": children,
            "infants": infants,
            "limit": 1,
            "sort": "price"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=header)
        response.raise_for_status()
        data = response.json()
        list_data = data["data"]
        try:
            flight_data = FlightData(price=list_data[0]["price"], origin_city=list_data[0]["cityFrom"],
                                     origin_airport=list_data[0]["flyFrom"], destination_city=list_data[0]["cityTo"],
                                     destination_airport=list_data[0]["flyTo"], out_date=list_data[0]["local_departure"].split("T")[0],
                                     return_date=list_data[0]["local_arrival"].split("T")[0])
        except IndexError:
            print(f"No flights found for {destination_city}")
        else:
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
