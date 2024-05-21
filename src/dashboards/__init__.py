import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
import os

# Database Configuration
DB_USERNAME = "postgres"
DB_PASSWORD = "Root@123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "insights"

# Encode username and password
encoded_username = urllib.parse.quote_plus(DB_USERNAME)
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)

# PostgreSQL connection URL
DB_URL = (
    f"postgresql://{encoded_username}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
try:
    # Create SQLAlchemy engine
    engine = create_engine(DB_URL)

    # Test connection
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except Exception as e:
    print(f"An error occurred: {e}")
# Create SQLAlchemy engine
engine = create_engine(DB_URL)

# Define the base directory
base_dir = os.path.dirname(__file__)

# Load the datasets
apollo_reviews_df = pd.read_excel(
    os.path.join(base_dir, "../../data/raw/Apollo android review data.xlsx")
)
banks_ad_data_df = pd.read_excel(
    os.path.join(base_dir, "../../data/raw/BANKS AD DATA.xlsx")
)


# Write data to the database
apollo_reviews_df.to_sql(
    "apollo_android_review_data", con=engine, if_exists="replace", index=False
)
banks_ad_data_df.to_sql("banks_ad_data", con=engine, if_exists="replace", index=False)

print("Data loaded successfully.")
