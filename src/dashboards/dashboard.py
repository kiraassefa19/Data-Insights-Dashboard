import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, ".."))

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dashboards.ad_performance as ad_performance
import dashboards.play_store_reviews as play_store_reviews
import dashboards.tikvah_ad_impact as tikvah_ad_impact
import dashboards.telegram_subscription_growth as telegram_subscription_growth

# Initialize the Dash application
app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Roboto&display=swap"
    ],
)

# Define the layout of the dashboard
app.layout = html.Div(
    style={"fontFamily": "Roboto", "display": "flex", "height": "100vh"},
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(
            style={"width": "20%", "backgroundColor": "#f8f9fa", "padding": "20px"},
            children=[
                html.H2("Dashboard", style={"textAlign": "center"}),
                html.Ul(
                    [
                        html.Li(
                            dcc.Link(
                                "Ad Performance",
                                href="/ad-performance",
                                style={
                                    "textDecoration": "none",
                                    "color": "inherit",
                                },
                            ),
                            style={"marginBottom": "10px", "marginLeft": "20px"},
                        ),
                        html.Li(
                            dcc.Link(
                                "Play Store Reviews",
                                href="/play-store-reviews",
                                style={"textDecoration": "none", "color": "inherit"},
                            ),
                            style={"marginBottom": "10px", "marginLeft": "20px"},
                        ),
                        html.Li(
                            dcc.Link(
                                "Tikvah Ad Impact",
                                href="/tikvah-ad-impact",
                                style={"textDecoration": "none", "color": "inherit"},
                            ),
                            style={"marginBottom": "10px", "marginLeft": "20px"},
                        ),
                        html.Li(
                            dcc.Link(
                                "Telegram Subscription Growth",
                                href="/telegram-subscription-growth",
                                style={"textDecoration": "none", "color": "inherit"},
                            ),
                            style={"marginBottom": "10px", "marginLeft": "20px"},
                        ),
                    ],
                    style={"listStyleType": "none", "padding": 0, "margin": 0},
                ),
            ],
        ),
        html.Div(
            id="page-content",
            style={"width": "80%", "padding": "20px"},
        ),
    ],
)


# Update the content based on the URL
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/ad-performance":
        return ad_performance.layout
    elif pathname == "/play-store-reviews":
        return play_store_reviews.layout
    elif pathname == "/tikvah-ad-impact":
        return tikvah_ad_impact.layout
    elif pathname == "/telegram-subscription-growth":
        return telegram_subscription_growth.layout
    else:
        return html.Div(
            [
                html.H3("Welcome to the Data Insights Dashboard!"),
                html.P("Please select a section from the navigation menu."),
            ]
        )


# Run the Dash application
if __name__ == "__main__":
    app.run_server(debug=True)
