from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

flight_data = FlightData()

data_manager = DataManager(flight_data)
data_manager.put_iata_data()

flight_search = FlightSearch(data_manager)

flight_search.get_cheap_flight_data()

