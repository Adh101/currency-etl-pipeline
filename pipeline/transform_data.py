import pandas as pd 

def transform_exchange_data(data):
    """
    Transform API data into a clean Pandas DataFrame.

    Args:
        data (dict): Validated API response.

    Returns:
        pd.DataFrame: Flattened data ready for database insertion.
    """
    #Extract relevant fields from the API response
    base = data['base']
    date = data['date']
    rates = data['rates']

    # Create a DataFrame from the rates dictionary
    df = pd.DataFrame(list(rates.items()), columns =['target_currency', 'exchange_rate'])

    # Add base currency and date columns
    df['base_currency'] = base
    df['date'] = date

    # Reorder and rename columns
    df = df[['date','base_currency', 'target_currency', 'exchange_rate']]

    df['date'] = pd.to_datetime(df['date'])  # Convert date to datetime format
    df['exchange_rate'] = df['exchange_rate'].astype(float)  # Ensure exchange_rate is float
    df['base_currency'] = df['base_currency'].astype(str)  # Ensure base_currency is string
    df['target_currency'] = df['target_currency'].astype(str)  # Ensure target_currency is string

    print("Data Transformation Successful.")
    return df
