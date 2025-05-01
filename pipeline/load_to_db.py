import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

def load_to_db(df):
    """
    Load transformed DataFrame into Supabase-hosted PostgreSQL database.

    Args:
        df (DataFrame): Cleaned and transformed data ready for insertion.
    """

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")

    if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
        raise ValueError("Database connection details are not set in environment variables.")

    try:
        # Add sslmode=require for Supabase
        db_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require'

        # Create a SQLAlchemy engine
        engine = create_engine(db_url)

        # Append data to the 'exchange_rates' table
        df.to_sql('exchange_rates', engine, if_exists='append', index=False)

        print("✅ Data loaded to database successfully.")

    except Exception as e:
        print(f"❌ Error loading data to database: {e}")
