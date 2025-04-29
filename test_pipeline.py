from pipeline.fetch_api import fetch_exchange_rates
from pipeline.validate_data import validate_exchange_data
from pipeline.transform_data import transform_exchange_data

def test_data_pipeline():
    data = fetch_exchange_rates()

    if data:
        try:
            validate_exchange_data(data)
            df = transform_exchange_data(data)
            print("API Fetch, Validation, and Transformation Successful!")
            print(df.head())  # Print a sample of the transformed data
        
        except Exception as e:
            print(f"Transformation failed: {e}")
    else:
        print(" API Fetch Failed.")

if __name__ == "__main__":
    test_data_pipeline()


