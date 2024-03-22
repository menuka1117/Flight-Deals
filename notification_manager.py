from flight_search import FlightSearch
from data_manager import DataManager

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_search: FlightSearch, data_manager: DataManager):
        self.flight_search = flight_search
        self.data_manager = data_manager


