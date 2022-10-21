from data_manager import DataManager
from flight_search import FlightSearch
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

spreadsheet_data = DataManager()

# updating IATA code from the list of cities in spreadsheet
i = 0
for entry in spreadsheet_data.data_list:
    try:
        if len(entry["iataCode"]) == 0:
            new_iata = FlightSearch(entry).get_iata_code()
            spreadsheet_data.update_iata(index=i, new_iata_code=new_iata)
    except KeyError:
        new_iata = FlightSearch(entry).get_iata_code()
        spreadsheet_data.update_iata(index=i, new_iata_code=new_iata)
    finally:
        i += 1
