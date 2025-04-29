import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_to_db(df):
    """
    Load transformed DataFrame into PostgreSQL database.

    Args:
        df (DataFrame): Cleaned and transformed data ready for database insertion.
    """

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
        raise ValueError("Database connection details are not set in environment variables.")
    
    try:
        # Create a PostgreSQL connection URL
        db_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

        # Create a SQLAlchemy engine
        engine = create_engine(db_url)
        
        # Load the DataFrame into the database
        df.to_sql('exchange_rates', engine, if_exists='append', index=False) # Appends the new data, not replace
        
        print("Data loaded to database successfully.")
    
    except Exception as e:
        print(f"Error loading data to database: {e}")