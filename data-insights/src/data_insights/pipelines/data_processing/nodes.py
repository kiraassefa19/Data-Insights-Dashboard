import pandas as pd
from sqlalchemy import create_engine


# Load Excel file into a DataFrame
excel_data = pd.read_excel("data/01_raw/telegram_data.xlsx")

# Now excel_data contains the contents of the Excel file as a DataFrame


def process_telegram_stats(raw_data: pd.DataFrame) -> pd.DataFrame:
    raw_data["engagement_rate"] = (raw_data["likes"] + raw_data["comments"]) / raw_data[
        "views"
    ]
    return raw_data


def process_playstore_reviews(raw_data: pd.DataFrame) -> pd.DataFrame:
    # Add any processing steps for playstore reviews
    return raw_data


def process_app_downloads(raw_data: pd.DataFrame) -> pd.DataFrame:
    # Add any processing steps for app downloads
    return raw_data


def process_telegram_growth(raw_data: pd.DataFrame) -> pd.DataFrame:
    # Add any processing steps for telegram growth
    return raw_data


def load_data():
    # Load Excel files into pandas DataFrames
    telegram_data = pd.read_excel("data/01_raw/telegram_data.xlsx")
    banks_ad_data = pd.read_excel("data/01_raw/BANKS AD DATA.xlsx")
    apollo_reviews = pd.read_excel("data/01_raw/Apollo android review data.xlsx")

    return telegram_data, banks_ad_data, apollo_reviews

def load_data_to_postgresql(data: pd.DataFrame) -> None:
    # Create a connection to your PostgreSQL database
    engine = create_engine("postgresql://postgres:Root@123@localhost:5432/insights")

    # Load the data into PostgreSQL database
    data.to_sql("processed_data", engine, if_exists="replace", index=False)
