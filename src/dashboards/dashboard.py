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
        "https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap"
    ],
)

# Define the layout of the dashboard
app.layout = html.Div(
    style={
        "fontFamily": "Roboto",
        "display": "flex",
        "height": "100vh",
        "backgroundColor": "#f8f9ea",
    },
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(
            style={
                "width": "20%",
                "backgroundColor": "#343a40",
                "padding": "20px",
                "color": "white",
                "boxShadow": "2px 0 5px rgba(0,0,0,0.1)",
            },
            children=[
                html.H2(
                    "Dashboard", style={"textAlign": "center", "marginBottom": "40px"}
                ),
                html.Ul(
                    [
                        html.Li(
                            dcc.Link(
                                "Ad Performance",
                                href="/ad-performance",
                                style={
                                    "textDecoration": "none",
                                    "color": "white",
                                    "padding": "10px",
                                    "display": "block",
                                    "borderRadius": "5px",
                                    "transition": "background-color 0.3s",
                                },
                                className="nav-link",
                            ),
                            style={"marginBottom": "10px"},
                        ),
                        html.Li(
                            dcc.Link(
                                "Play Store Reviews",
                                href="/play-store-reviews",
                                style={
                                    "textDecoration": "none",
                                    "color": "white",
                                    "padding": "10px",
                                    "display": "block",
                                    "borderRadius": "5px",
                                    "transition": "background-color 0.3s",
                                },
                                className="nav-link",
                            ),
                            style={"marginBottom": "10px"},
                        ),
                        html.Li(
                            dcc.Link(
                                "Tikvah Ad Impact",
                                href="/tikvah-ad-impact",
                                style={
                                    "textDecoration": "none",
                                    "color": "white",
                                    "padding": "10px",
                                    "display": "block",
                                    "borderRadius": "5px",
                                    "transition": "background-color 0.3s",
                                },
                                className="nav-link",
                            ),
                            style={"marginBottom": "10px"},
                        ),
                        html.Li(
                            dcc.Link(
                                "Telegram Subscription Growth",
                                href="/telegram-subscription-growth",
                                style={
                                    "textDecoration": "none",
                                    "color": "white",
                                    "padding": "10px",
                                    "display": "block",
                                    "borderRadius": "5px",
                                    "transition": "background-color 0.3s",
                                },
                                className="nav-link",
                            ),
                            # style={"marginBottom": "10px"},
                        ),
                    ],
                    style={"listStyleType": "none", "padding": 0, "margin": 0},
                    className="nav-links",  # Added class name for CSS targeting
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
                html.H3(
                    "Welcome to the Data Insights Dashboard!",
                    style={
                        "textAlign": "center",
                        "marginTop": "50px",
                        "color": "#495057",
                    },
                ),
                html.P(
                    "Please select a section from the navigation menu.",
                    style={"textAlign": "center", "color": "#495057"},
                ),
            ]
        )


# Add custom CSS
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body { margin: 0; }
            .nav-link:hover {
                background-color: #495057;
                transition: background-color 0.3s;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""

# Run the Dash application
if __name__ == "__main__":
    app.run_server(debug=True)
