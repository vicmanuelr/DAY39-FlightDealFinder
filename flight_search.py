

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.get_iata_code()

    def get_iata_code(self):
        self.flight_data["iataCode"] = "TESTING"