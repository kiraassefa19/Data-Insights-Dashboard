from dash import dcc, html
import plotly.express as px
import pandas as pd
import os

# Load the data
base_dir = os.path.dirname(__file__)
banks_ad_data_df = pd.read_excel(
    os.path.join(base_dir, "../../data/raw/BANKS AD DATA.xlsx")
)

# Create the plot
fig = px.line(
    banks_ad_data_df,
    x="Date",
    y="View",
    color="Bank",
    title="Banks Ad Performance Over Time",
)

# Define the layout
layout = html.Div(
    [
        # html.H3("Banks Ad Performance Over Time"), 
        dcc.Graph(figure=fig)
    ]
    )
