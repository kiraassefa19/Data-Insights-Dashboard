import os
import pandas as pd

# Load the data
base_dir = os.path.dirname(__file__)
apollo_reviews_df = pd.read_excel(
    os.path.join(base_dir, "../../data/raw/Apollo android review data.xlsx")
)
banks_ad_data_df = pd.read_excel(
    os.path.join(base_dir, "../../data/raw/BANKS AD DATA.xlsx")
)
