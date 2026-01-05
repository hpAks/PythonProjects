import datetime

from amadeus import Client, ResponseError

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    def check_for_flights(self, origin, dest, lowest_fare):
        try:
            '''
            Find the cheapest flights from SYD to BKK
            GET https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=MUC

            '''
            amadeus = Client(
                client_id='RmLGCmGGa1z4GqIWRo3vn6A2aPYKEDBj',
                client_secret='0nEdmYWkcx2jOBHb'
            )
            today_date = (datetime.datetime.today()+ datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            print(f"date: {today_date}")
            print(f"IATA codes for origin :{origin}, destination :{dest}")
            timedelta_days_60 = (datetime.datetime.today() + datetime.timedelta(days=(6 * 30))).strftime("%Y-%m-%d")
            response = amadeus.shopping.flight_offers_search.get(originLocationCode=origin, destinationLocationCode=dest, departureDate=today_date, adults=1, currencyCode="USD")
            lowest_option = None
            for row in response.data:
                if row is not None and row['price'] is not None:
                    row_price_grand_total_ = row['price']['grandTotal']
                    print(f"lowest fare for this trip : {row_price_grand_total_} and expected min fare : {lowest_fare}")
                    if lowest_fare > float(row_price_grand_total_):
                        lowest_option = row
            if lowest_option is not None:
                print(f"flight search response flight price :{lowest_option['price']['grandTotal']}")
                origin_dest = lowest_option["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination = lowest_option["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = lowest_option["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                trip_plan = f"Flight available for {destination} from {origin_dest} leaving on {out_date} for a total of {lowest_option['price']['grandTotal']}"
                return trip_plan
            else:
                return None
        except ResponseError as error:
            raise error