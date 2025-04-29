from pipeline.fetch_api import fetch_exchange_rates

def test_fetch():
    data = fetch_exchange_rates()
    if data:
        print("Data fetched successfully:")
        print("Sample Output:", data)  # Print a sample of the output
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    test_fetch()