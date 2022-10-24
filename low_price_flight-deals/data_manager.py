import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/6e7fcee8d722ea977fcdd89370bae85c/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        header = {
            "Authorization": "Bearer jsgdgsodhpihdpsdoosdosgdougo"
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        header = {
            "Authorization": "Bearer jsgdgsodhpihdpsdoosdosgdougo"
        }
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=header
            )
            print(response.text)
