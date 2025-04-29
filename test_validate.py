from pipeline.validate_data import validate_exchange_data
from pipeline.fetch_api import fetch_exchange_rates

def test_validate():
    data = fetch_exchange_rates()

    try:
        validate_exchange_data(data)
        print("Data validation successful.")
    except ValueError as e:
        print(f"Data validation failed: {e}")

if __name__ == "__main__":
    test_validate()