def validate_exchange_data(data):

    """
    Validate the structure and contents of exchange rates API response.

    Args:
        data (dict): API response as Python dictionary.

    Raises:
        ValueError: If required keys are missing or response is unsuccessful.
        TypeError: If 'rates' field is not a dictionary or rates contain invalid types.
    """
    
    if not data:
        raise ValueError("Empty data received from API.") # Check if data is None or empty
    
    if not data.get('success', False):
        raise ValueError("API call unsuccessful.") # Check if the API call was successful
    
    required_keys = ['timestamp', 'base', 'date', 'rates'] # List of required keys

    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing the requred key in API response: {key}") # Check if all required keys are present
        
    rates = data['rates']
    if not isinstance(rates, dict):
        raise ValueError('Rates should be mapped to dictionary.') # Check if rates is a dictionary
    
    for currency, rate in rates.items():
        if not isinstance(rate, (int, float)):
            raise ValueError(f" Invalid rate for currency: {currency}. {rate} (type: {type(rate).__name__})") # Check if each rate is a number
    
    print("Data Validation Successful.")
    return True