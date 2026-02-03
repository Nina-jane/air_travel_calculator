# faculty budgets page
# Note that you only want to include the libraries that you use on this page

import dash
import os
from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = html.Div(
     [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            [
                                "This calculator will be used as part of a carbon budget pilot.",
                            ]
                        )
                    ], xs=6, sm=6, md=8, lg=8, xl=8, xxl=8
                ),
            ], style={'color': '#ccc'}
        )
    ]
)