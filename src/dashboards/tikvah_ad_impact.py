# src/dashboards/tikvah_ad_impact.py
from dash import dcc, html
import plotly.express as px
import dashboard_utils as du

# Use the loaded data from dashboard_utils
data = du.ad_performance_data_df

# Create the plot
fig = px.line(data, x="Date", y="Views", title="Tikvah Ad Impact Over Time")

# Define the layout
layout = html.Div([html.H3("Tikvah Ad Impact Over Time"), dcc.Graph(figure=fig)])
