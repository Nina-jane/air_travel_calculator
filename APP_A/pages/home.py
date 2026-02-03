# home page
# Note that you only want to include the libraries that you use on this page

import dash
import os
from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, path='/')

#external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]

#pages_folder=os.path.join(os.path.dirname(__name__), "pages")

#app = Dash(__name__, use_pages=True, pages_folder=pages_folder, external_stylesheets = external_stylesheets)

#airport_code_dictionary = pd.read_csv('C:/Users/em14576/OneDrive - AUT University/3. Projects/5. Air travel emissions calculator/airport_code_dictionary.csv', encoding='cp1252')

# Function to calculate emissions

info_icon_fa = html.I(className="fa-solid fa-circle-info")
info_icon_bs = html.I(className="bi bi-info-circle")

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        #html.H3("Welcome!!"),
                        html.P(
                            [
                                "Welcome to this air travel emissions calculator.",
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                            ]
                        )
                    ], xs=6, sm=6, md=8, lg=8, xl=8, xxl=8
                ),
            ], style={'color': '#ccc'}
        )
    ]
)
    

