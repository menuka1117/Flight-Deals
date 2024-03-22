import requests
import datetime
from data_manager import DataManager
TEQUILA_API = "BL-w6e-9f5rANcD3rPqof0OCWOVeG19Y"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
        self.search_cheap_flight_endpoint = "https://api.tequila.kiwi.com/search"

        self.headers = {
            "apikey": TEQUILA_API,
        }
        self.today = datetime.datetime.today()
        self.tommorow = (self.today + datetime.timedelta(days=1)).strftime(f"%d/%m/%Y")
        self.six_months_after_day = (self.today + datetime.timedelta(days=180)).strftime(f"%d/%m/%Y")





    def get_cheap_flight_data(self):
        self.prices = {}

        self.data_manager.get_sheet_data()

        for row in self.data_manager.data["prices"]:
            self.iata_code = row["iataCode"]

            self.search_cheap_flight_params = {
                "fly_from": "CMB",
                "fly_to": f"{self.iata_code}",
                "date_from ": f"{self.tommorow}",
                "date_to ": f"{self.six_months_after_day}",
                "one_for_city": 1,
            }

            self.search_cheap_flight = requests.get(url=self.search_cheap_flight_endpoint,
                                                    params=self.search_cheap_flight_params, headers=self.headers)

            self.cheap_filght_data = self.search_cheap_flight.json()

            self.prices = {f"{self.cheap_filght_data['data'][0]['cityCodeTo']}": f"{self.cheap_filght_data['data'][0]['price']}"}
            print(self.prices)