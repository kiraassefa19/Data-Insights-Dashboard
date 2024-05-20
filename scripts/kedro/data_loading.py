import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine("postgresql://user:password@localhost:5432/mydatabase")

# Load raw data
apollo_reviews = pd.read_excel("data/raw/Apollo_android_review_data.xlsx")
banks_ad_data = pd.read_excel("data/raw/BANKS_AD_DATA.xlsx")

# Example processing steps
# For Apollo reviews, remove nulls and process dates
apollo_reviews = apollo_reviews.dropna(subset=["review"])
apollo_reviews["review_date"] = pd.to_datetime(apollo_reviews["review_date"])

# For Banks ad data, standardize column names
banks_ad_data.columns = [col.lower().replace(" ", "_") for col in banks_ad_data.columns]

# Save processed data to PostgreSQL
apollo_reviews.to_sql("apollo_reviews", engine, if_exists="replace", index=False)
banks_ad_data.to_sql("banks_ad_data", engine, if_exists="replace", index=False)
