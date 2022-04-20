import requests
from flight_data import FlightData
from datetime import datetime
from datetime import timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, flight_data: FlightData):
        self.data_organizer = flight_data
        self.API_KEY = 'SVvhZUzIJTid86ygG1-zLHwMS8jOh1Xx'
        self.FLY_FROM = 'LON'

        self.tomorrow = (datetime.now().date() + timedelta(days=1))
        self.tomorrow_day = self.tomorrow.strftime('%d')
        self.tomorrow_month = self.tomorrow.strftime('%m')
        self.tomorrow_year = self.tomorrow.strftime('%Y')
        self.tomorrow_date = f'{self.tomorrow_day}%2F{self.tomorrow_month}%2F{self.tomorrow_year}'

        self.six_months = (datetime.now().date() + timedelta(days=180))
        self.six_months_day = self.six_months.strftime('%d')
        self.six_months_month = self.six_months.strftime('%m')
        self.six_months_year = self.six_months.strftime('%Y')
        self.six_months_date = f'{self.six_months_day}%2F{self.six_months_month}%2F{self.six_months_year}'

        self.headers = {
            'apikey': self.API_KEY
        }

        self.id_endpoint = 'https://tequila-api.kiwi.com/locations/topdestinations'

        self.id_params = {
            'term': 'london_gb',
            'locale': 'en-US',
            'limit': '100',
            'sort': 'name',
            'active_only': 'true',
            'source_popularity': 'searches',
        }

        self.cheap_endpoint = 'https://tequila-api.kiwi.com/v2/search'


    def find_id(self, city_list):
        response_id = requests.get(url=self.id_endpoint, params=self.id_params, headers=self.headers)
        print(response_id)
        id_data = response_id.json()
        id_list = self.data_organizer.extract_id(id_data, city_list)
        return id_list

    def find_cheap_flights(self, id_data, prices):
        cheap_flights_all = []
        for id in id_data:
            response_cheap = requests.get(url=f'https://tequila-api.kiwi.com/v2/search?fly_from={self.FLY_FROM}&fly_to={id}'
                                              f'&date_from={self.tomorrow_date}&date_to={self.six_months_date}&nights_in_dst_from=7&nights_in_dst_to=28', headers=self.headers)
            cheap_flights = response_cheap.json()
            cheap_flights_all.append(cheap_flights)


        cheap_flights_list = self.data_organizer.find_cheapest_flight(cheap_flights_all, prices)
        return cheap_flights_list


