import datetime

import requests
import data_manager,flight_search,notification_manager
from amadeus import Client, ResponseError, Location

amadeus_auth_token ="0FiO9KW1lrAvFqvHZ53yYGfuR713"
amadeus_city_airport_serach_url ="https://test.api.amadeus.com/v1/reference-data/locations/cities"
amadeus_flight_search_url = ""

amadeus_auth_token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.data_manager = data_manager.DataManager()
        today = datetime.datetime.today().strftime('%d/%m/%Y')
        self.notification_manager = notification_manager.NotificationManager();
        for row in  self.data_manager.get_rows_from_googleSheet():
           if row['iataCode'] is None or len(row['iataCode']) == 0:
               self.update_airport_code(row)
           self.flight_search = flight_search.FlightSearch()
           if row['iataCode'] is not None and len(row['iataCode']) > 0:
               data = self.flight_search.check_for_flights('JFK',row['iataCode'][0:3],row['lowestPrice'])
               if data is not None:
                   self.notification_manager.notification_email(data)


    def update_airport_code(self, row):
        try:
            amadeus = Client(
                client_id='RmLGCmGGa1z4GqIWRo3vn6A2aPYKEDBj',
                client_secret='0nEdmYWkcx2jOBHb'
            )
            response = amadeus.reference_data.locations.get(keyword=row['city'], subType=Location.AIRPORT)
            if len(response.data) > 0:
                row['iataCode'] = response.data[0]['id']
                self.data_manager.update_airport_code(row['id'], row)
            else :
                print(f"Cant find the IATA code for the city : {row['city']}")
        except ResponseError as error:
            print(f"error:{error}")