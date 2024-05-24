# src/dashboards/telegram_subscription_growth.py
from dash import dcc, html
import plotly.express as px
import dashboard_utils as du

# Use the loaded data from dashboard_utils
data = du.telegram_subscription_data_df

# Create the plot
fig = px.line(
    data, x="Date", y="Subscribers", title="Telegram Subscription Growth Over Time"
)

# Define the layout
layout = html.Div(
    [html.H3("Telegram Subscription Growth Over Time"), dcc.Graph(figure=fig)]
)
