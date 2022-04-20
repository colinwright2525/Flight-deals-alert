
class FlightData:
    #This class is responsible for structuring the flight data.
    def extract_id(self, id_data, city_list):
        city_id_list = []
        for city in city_list:
            for location in id_data['locations']:
                if city == location['name']:
                    city_id = location['code']
                    city_id_list.append(city_id)
        return city_id_list

    def find_cheapest_flight(self, cheap_flights_all, prices):
        #prices = ['54', '42', '485', '551', '95', '414', '240', '260', '378']
        lowest_price_list = []
        out_flights = []
        return_flights = []
        count = 0
        for price in prices:
            try:
                flights = cheap_flights_all[count]
            except:
                lowest_price = 'no flights found'
                out_flight = ''
                return_flight = ''
                continue
            else:
                lowest_price = int(price)
                try:
                   print(flights['data'])
                except:
                    lowest_price = 'no flights found'
                    out_flight = ''
                    return_flight = ''
                    continue
                else:
                    for cost in flights['data']:
                        if cost['price'] < lowest_price:
                            lowest_price = cost['price']
                            out_flight = cost['route'][0]['local_departure'].split('T')[0]
                            return_flight = cost['route'][1]['local_departure'].split('T')[0]


                    if lowest_price == int(price):
                        lowest_price = 'no cheap flights'
                        out_flight = ''
                        return_flight = ''
            finally:
                lowest_price_list.append(lowest_price)
                out_flights.append(out_flight)
                return_flights.append(return_flight)
                flight_info = [lowest_price_list, out_flights, return_flights]
                count += 1
        #print(lowest_price_list)
        return flight_info





