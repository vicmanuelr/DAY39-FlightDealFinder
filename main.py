from data_manager import DataManager
from flight_search import FlightSearch
import datetime
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
DEPARTURE_CITY = "Guatemala"
DEPARTURE_AIRPORT = "GUA"
CURRENCY = "USD"
MINIMUN_STAY = 8
MAXIMUN_STAY = 25
FLIGHT_TYPE = "round"
ADULTS = 2
CHILDREN = 0
INFANTS = 1

spreadsheet_data = DataManager()
notification_manager = NotificationManager()

# updating IATA code from the list of cities in spreadsheet
i = 0
for entry in spreadsheet_data.data_list:
    try:
        if len(entry["iataCode"]) == 0 or len(entry["airportName"]) == 0:
            new_iata, new_airport = FlightSearch(entry).get_airport()
            spreadsheet_data.update_airport(index=i, new_iata_code=new_iata, new_airport_name=new_airport)
    except KeyError:
        new_iata, new_airport = FlightSearch(entry).get_airport()
        spreadsheet_data.update_airport(index=i, new_iata_code=new_iata, new_airport_name=new_airport)
    finally:
        i += 1

date_from = datetime.date.today().strftime("%d/%m/%Y")
six_months = datetime.timedelta(days=30) * 6
date_to = (datetime.date.today() + six_months).strftime("%d/%m/%Y")

# serach of cheap flights and update price if lower found, also notifications sent
i = 0
for row in spreadsheet_data.data_list:
    flight_data = FlightSearch(row).search_cheap_flights(departure_airport=DEPARTURE_AIRPORT, date_from=date_from, date_to=date_to, destination_airport=row["iataCode"], currency=CURRENCY,
                                           min_stay=MINIMUN_STAY, max_stay=MAXIMUN_STAY, adults=ADULTS, children=CHILDREN, infants=INFANTS, flight_type=FLIGHT_TYPE, destination_city=row["city"])
    if flight_data is not None:
        if row["lowestPrice"] > flight_data.price:
            spreadsheet_data.update_price(index=i, new_price=flight_data.price)
            for user in spreadsheet_data.users_list:
                notification_manager.send_email(message=flight_data, email_to=user["email"])
    i += 1
