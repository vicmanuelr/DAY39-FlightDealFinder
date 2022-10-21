from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheet_data = DataManager()

i = 0
for entry in sheet_data.sheet_data:
    new_entry = FlightSearch(entry)
    sheet_data.update_iata(index=i)
    i += 1

