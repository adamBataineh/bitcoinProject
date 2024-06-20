import requests
import json

# URL for the CoinDesk API to fetch the current Bitcoin price
api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Send a GET request to the API
response = requests.get(api_url)

# Print the response status code and JSON response
print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(response.json())
