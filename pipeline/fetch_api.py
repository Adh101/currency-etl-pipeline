import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

def fetch_exchange_rates():
    API_KEY = os.getenv('API_KEY') # Fetch the API key from environment variables
    url = f"https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base=EUR" # Construct the URL with the API key

    try:
        response = requests.get(url, timeout = 10) # Set a timeout for the request
        response.raise_for_status()  # Raise an error if response status is not 200
        data = response.json() # Parse the JSON response
        return data # Return the parsed data

    except Exception as e:
        print(f"Error fetching exchange rates: {e}") # Print the error message
        return None
