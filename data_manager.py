import requests
from flight_data import FlightData

SHEETY_TOKEN = "kfajlkfjskljfi334td"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, flight_data: FlightData):
        self.flight_data = flight_data
        self.sheety_endpoint = "https://api.sheety.co/8dd3ef63d3d0bbabb1e9de0aa640bdfd/flightDeals/prices"
        self.headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
            "Content-Type": "application/json"
        }

        self.params = {}

    def get_sheet_data(self):
        self.response = requests.get(url=self.sheety_endpoint, headers=self.headers)
        self.response.raise_for_status()
        self.data = self.response.json()

    def put_iata_data(self):
        self.get_sheet_data()

        for row in self.data["prices"]:
            self.flight_data.city_name = row["city"]
            self.flight_data.get_location_data()
            self.params = {
                "price": {
                    "iataCode": self.flight_data.iata
                }
            }
            self.put_iata = requests.put(url=f"{self.sheety_endpoint}/{row['id']}", headers=self.headers, json=self.params)
            self.put_iata.raise_for_status()

