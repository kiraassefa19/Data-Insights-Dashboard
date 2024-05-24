import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# Database Configuration
DB_USERNAME = "postgres"
DB_PASSWORD = "Root@123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "insights"

# Encode username and password
encoded_username = urllib.parse.quote_plus(DB_USERNAME)
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)



def load_data_to_postgres():
    
    # PostgreSQL connection URL
    DB_URL = (
    f"postgresql://{encoded_username}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    
    # Load Apollo android review data
    apollo_reviews = pd.read_excel("data/raw/Apollo android review data.xlsx")

    # Load BANKS AD data
    banks_ad_data = pd.read_excel("data/raw/BANKS AD DATA.xlsx")

    # Create a PostgreSQL engine
    engine = create_engine(DB_URL)

    # Load data into PostgreSQL
    apollo_reviews.to_sql("apollo_reviews", engine, if_exists="replace", index=False)
    banks_ad_data.to_sql("banks_ad_data", engine, if_exists="replace", index=False)


if __name__ == "__main__":
    load_data_to_postgres()
