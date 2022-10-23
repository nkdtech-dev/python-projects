import requests

stock_api_key = "9M9I7E0RKQI9CHEX."
stock_api_endpoint = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "FX_DAILY",
    "from_symbol": "BTC",
    "apikey": stock_api_key,

}
# TODO get hold of the news about the desired crypto currency
stock_response = requests.get(stock_api_endpoint, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
print(stock_data)
# todo get hold of the closing price of today


# todo get hold of the closing price of yesterday


# todo compute the defencence of the closing price of yesterday and today and conclude on  the percentage

# todo send a message using twilio to ur self about thet latest change in stocks
