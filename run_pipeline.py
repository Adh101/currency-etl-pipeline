from pipeline.fetch_api import fetch_exchange_rates
from pipeline.validate_data import validate_exchange_data
from pipeline.transform_data import transform_exchange_data
from pipeline.load_to_db import load_to_db

def main():
    data = fetch_exchange_rates()

    if data:
        try:
            validate_exchange_data(data)
            df = transform_exchange_data(data)
            load_to_db(df)

            print("Data pipeline executed successfully!")
        
        except Exception as e:
            print(f"Pipeline execution failed: {e}")
    else:
        print("API Fetch Failed.")

if __name__ == "__main__":
    main()