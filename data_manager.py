import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_endpoint = 'https://api.sheety.co/57847da89fd951012d39fa01b640737f/myFlightDeals/prices'

    def get_cities(self):
        response_cities = requests.get(url=self.sheet_endpoint)
        cities_data = response_cities.json()
        city_list = []
        for city in cities_data['prices']:
            new_city = city['city']
            city_list.append(new_city)
        print(city_list)
        return city_list

    def add_id(self, id_data):
        row_number = 2
        headers = {
            'Content-Type': 'application/json',
        }
        for id in id_data:
            sheet_edit_endpoint = f'https://api.sheety.co/57847da89fd951012d39fa01b640737f/myFlightDeals/prices/{row_number}'
            id_params = {
                'price': {
                    'code': id,
                }
            }

            print(id)
            create_id = requests.put(url=sheet_edit_endpoint, json=id_params, headers=headers)
            print(create_id)
            row_number += 1

    def get_prices(self, id_data):
        response_prices = requests.get(url=self.sheet_endpoint)
        prices_data = response_prices.json()
        prices = []
        for price in prices_data['prices']:
            new_price = price['price']
            prices.append(new_price)
        return prices
