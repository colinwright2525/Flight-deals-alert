#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

HOME = 'London'
HOME_ID = 'STN'

sheety_manager = DataManager()
data_organizer = FlightData()
flight_finder = FlightSearch(data_organizer)
phone = NotificationManager()

city_list = sheety_manager.get_cities()
#city_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
id_data = flight_finder.find_id(city_list)
#id_data = ['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT', 'BZZ']
print(id_data)

sheety_manager.add_id(id_data)
prices = sheety_manager.get_prices(id_data)
#prices = ['54', '42', '485', '551', '95', '414', '240', '260', '378', '501']

flight_info = flight_finder.find_cheap_flights(id_data, prices)
cheap_flights_list = flight_info[0]
flights_out_info = flight_info[1]
flights_return_info = flight_info[2]

print(cheap_flights_list)

num = 0
for price in cheap_flights_list:
    if price != 'no cheap flights' and price != 'no flights found':
        message = f'Low price alert! Only {price} euros to fly from {HOME}-{HOME_ID} ' \
                  f'to {city_list[num]}-{id_data[num]}, from {flights_out_info[num]} to {flights_return_info[num]}.'

        phone.send_alert(message)
    num += 1









