# src/dashboards/play_store_reviews.py
from dash import dcc, html
import plotly.express as px
import dashboard_utils as du

# Use the loaded data from dashboard_utils
data = du.apollo_reviews_df
preprocessed_data = du.preprocess_data(data)

# Create the plot
fig = px.histogram(
    preprocessed_data, x="score", title="Apollo Android Reviews Rating Distribution"
)

# Define the layout
layout = html.Div(
    [html.H3("Apollo Android Reviews Rating Distribution"), dcc.Graph(figure=fig)]
)
