# src/dashboard_utils.py
import os
import pandas as pd

# Define the base directory
base_dir = os.path.dirname(__file__)

# Load the datasets
apollo_reviews_df = pd.read_excel(
    os.path.join(base_dir, "../../data/raw/Apollo android review data.xlsx")
)
banks_ad_data_df = pd.read_excel(
    os.path.join(base_dir, "../../data/raw/BANKS AD DATA.xlsx")
)
telegram_subscription_data_path = os.path.join(
    base_dir, "../../data/processed/telegram_subscription_data.csv"
)
ad_performance_data_path = os.path.join(
    base_dir, "../../data/processed/ad_performance_data.csv"
)

# Load processed data if available
if os.path.exists(telegram_subscription_data_path):
    telegram_subscription_data_df = pd.read_csv(telegram_subscription_data_path)
else:
    telegram_subscription_data_df = pd.DataFrame()

if os.path.exists(ad_performance_data_path):
    ad_performance_data_df = pd.read_csv(ad_performance_data_path)
else:
    ad_performance_data_df = pd.DataFrame()


def preprocess_data(df):
    # Example preprocessing steps
    df = df.dropna()
    return df


print("Data loaded successfully.")
