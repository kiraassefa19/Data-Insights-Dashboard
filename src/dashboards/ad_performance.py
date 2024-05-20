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

# Create SQLAlchemy engine
engine = create_engine(DB_URL)

# Load Apollo android review data
apollo_reviews = pd.read_sql("SELECT * FROM apollo_android_review_data", engine)

# Load Banks ad data
banks_ad_data = pd.read_sql("SELECT * FROM banks_ad_data", engine)

# Summarize Apollo reviews data
apollo_summary = apollo_reviews.describe()
print("Apollo Reviews Summary:\n", apollo_summary)

# Summarize Banks ad data
banks_ad_summary = banks_ad_data.describe()
print("Banks Ad Data Summary:\n", banks_ad_summary)

# Plot Apollo reviews rating distribution
fig1 = px.histogram(
    apollo_reviews, x="rating", title="Apollo Android Reviews Rating Distribution"
)
fig1.show()

# Plot Banks ad performance over time
fig2 = px.line(
    banks_ad_data,
    x="date",
    y="views",
    color="ad_campaign",
    title="Banks Ad Performance Over Time",
)
fig2.show()
