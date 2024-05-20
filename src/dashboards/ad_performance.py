import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import urllib.parse

# Database Configuration
DB_USERNAME = "root"
DB_PASSWORD = "Root@123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "insights"

# Encode username and password
encoded_username = urllib.parse.quote_plus(DB_USERNAME)
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)

# MySQL connection URL
DB_URL = f"mysql://{encoded_username}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def plot_ad_performance(engine):
    query = "SELECT * FROM banks_ad_data"
    df = pd.read_sql(query, engine)
    fig = px.line(df, x="date", y="views", color="ad_campaign")
    fig.show()


if __name__ == "__main__":
    engine = create_engine(DB_URL)
    plot_ad_performance(engine)
