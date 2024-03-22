import requests

TEQUILA_API = "BL-w6e-9f5rANcD3rPqof0OCWOVeG19Y"
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.locations_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.city_name = ""
        self.iata = ""
        self.headers = {
            "apikey": TEQUILA_API,
        }

    def get_location_data(self):
        self.params = {
            "term": f"{self.city_name}",
            "location_types": "city",
            "limit": 1,
        }
        self.location_response = requests.get(url=self.locations_endpoint, params=self.params, headers=self.headers)
        self.location_response.raise_for_status()
        self.data = self.location_response.json()
        self.iata = self.data["locations"][0]["code"]