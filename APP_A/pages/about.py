# about page
# Note that you only want to include the libraries that you use on this page

import dash
import os
from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
#import dash_mantine_components as dmc

dash.register_page(__name__)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("About this calculator"),
                        html.Br(),
                        html.P(
                            [
                                "This calculator includes domestic NZ flights only.",
                                html.Br(),
                                html.Br(),
                                " The emissions factors come from the Ministry for the Environment\'s 2025 ", html.Em("Calculating Emissions Factors")," report."
                            ]
                        ),
                    ], xs=6, sm=6, md=8, lg=8, xl=8, xxl=8
                ),
            ], style={'color': '#ccc'}
        )
    ]
)
    