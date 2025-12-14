#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os
import smtplib
import requests
from pprint import pprint
from dotenv import load_dotenv
from flight_search import FlightSearch
from data_manager import DataManager

# Load environment variables
load_dotenv()

# Get environment variables
AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')
SHEET_ENDPOINT = os.getenv('SHEET_ENDPOINT')

# Validate environment variables
if not AMADEUS_API_KEY or not AMADEUS_API_SECRET or not SHEET_ENDPOINT:
    raise ValueError("Missing required environment variables")


response = requests.get(SHEET_ENDPOINT)
sheet_data = response.json()

for data in sheet_data['prices']:
    # pprint(data)
    id = data['id']
    city = data['city']
    iataCode = data['iataCode']
    if not iataCode:
        flightSearch = FlightSearch(city)
        flight_data = DataManager(data)
        sheet_body = {
            'price': {
                "iataCode": flightSearch.get_iaticode()
            }
        }
        pprint(flight_data)
        # response = requests.put(f"{SHEET_ENDPOINT}/{id}", json=sheet_body)
        # pprint(response.json())

response = requests.get(SHEET_ENDPOINT)
# pprint(response.json())
