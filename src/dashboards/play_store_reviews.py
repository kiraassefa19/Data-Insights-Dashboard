from dash import dcc, html
import plotly.express as px
import pandas as pd
import dashboard_utils as du

# Load the data
data = du.apollo_reviews_df
preprocessed_data = data

# Create the plot
fig = px.histogram(
    data, x="score", 
     title="Apollo Android Reviews Rating Distribution"
)

# Define the layout
layout = html.Div(
    [
        # html.H3("Apollo Android Reviews Rating Distribution"), 
        dcc.Graph(figure=fig)
     ]
)
