from data_manager import DataManager
from flight_search import FlightSearch
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

sheet_data = DataManager()

# updating IATA code from the list of cities in spreadsheet
i = 0
for entry in sheet_data.sheet_data:
    new_entry = FlightSearch(entry).get_iata_code()
    sheet_data.update_iata(index=i, new_iata_code=new_entry)
    i += 1

