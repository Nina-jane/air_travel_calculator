# calculator page
# Note that you only want to include the libraries that you use on this page

import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import os

dash.register_page(__name__)

SQUARE_BUTTON_STYLE = {
    "width": "100px",
    "height": "100px",
    "margin": "5px",
    "textAlign": "center",
    "lineHeight": "90px", # Center text vertically
    "fontSize": "16px",
}

thisPath = os.path.abspath(os.path.dirname(__file__))
routes = pd.read_csv(os.path.join(thisPath, os.pardir,'nz_routes_and_emissions.csv'), encoding='cp1252')

layout = html.Div(
    [       
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             [
        #                 html.H5("Will your trip be one-way, return or multi-stage?", style={'color': '#ccc'}),
        #                 html.Br(),
        #                 dcc.RadioItems(
        #                     options=[' One-way', ' Return (same flight path there, same flight path back)', ' Multi-stage'],
        #                     style={'color': '#ccc'},
        #                     #value='One-way'
        #                 ),
        #                 html.Br(),
        #             ]#, xs=3, sm=3, md=4, lg=4, xl=4, xxl=4
        #         )
        #     ]
        # ),
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             [
        #                 html.H5("Will your trip be domestic or international", style={'color': '#ccc'}),
        #                 html.Br(),
        #                 dcc.RadioItems(
        #                     options=[' Domestic (within NZ only)',' International'],
        #                     style={'color': '#ccc'},
        #                     #value='Domestic'
        #                 ),
        #                 html.Br(),
        #             ]#, xs=3, sm=3, md=4, lg=4, xl=4, xxl=4
        #         )
        #     ]
        # ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Which country will you travel from?", style={'color': '#ccc'}),
                        html.Br(),
                        dcc.Dropdown(
                            id='dropdown-1',
                            options=routes['DepCountry'].unique(), #Change this
                            value=['New Zealand'],
                            placeholder='Select departing location...'
                        ),
                    ], xs=3, sm=3, md=4, lg=4, xl=4, xxl=4
                ),
                dbc.Col(
                    [
                        html.H5("Which airport will you travel from?", style={'color': '#ccc'}),
                        html.Br(),
                        dcc.Dropdown(
                            id='dropdown-3',
                            options=sorted(routes['DepAirport'].unique()), #Change this
                            value=['WLG'],
                            placeholder='Enter the three letter aiport code...'
                        ),
                    ], xs=3, sm=3, md=4, lg=4, xl=4, xxl=4
                ),
                
            ]
        ),
        dbc.Row(
            [
                html.Div(
                    style={'height': '50px'}
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Which country will you travel to?", style={'color': '#ccc'}),
                        html.Br(),
                        dcc.Dropdown(
                            id='dropdown-2',
                            options=sorted(routes['ArrCountry'].unique()), #Change this
                            value=['Australia'],
                            placeholder='Select destination...'
                        ),
                    ], xs=3, sm=3, md=4, lg=4, xl=4, xxl=4
                ),
                dbc.Col(
                    [
                        html.H5("Which airport will you travel to?", style={'color': '#ccc'}),
                        html.Br(),
                        dcc.Dropdown(
                            id='dropdown-4',
                            options=sorted(routes['ArrAirport'].unique()), #Change this
                            value=['AKL'],
                            placeholder='Enter the three letter aiport code...'
                        ),
                    ], xs=3, sm=3, md=4, lg=4, xl=4, xxl=4
                )
            ]
        ),
        dbc.Row(
            [
                html.Div(
                    style={'height': '50px'}
                ),
            ]
        ),
        # dbc.Row([
        #     dbc.Col([
        #         dbc.Row([
        #             html.Div([
        #                 #dcc.Input(id='my-input', type='text', value='Initial Text'),
        #                 #html.Div(id='my-output-text', children='This text will be updated.')
        #             ],
        #             #className="p-3 bg-light border"),
        #             ),
        #         ])
        #     ], width=4 #, style={'border': '1px solid'}
        #     ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(id='my-output-text', children='This text will be updated.', style={'color': '#ccc', 'textAlign': 'center'})
                    ], xs=6, sm=6, md=8, lg=8, xl=8, xxl=8 #, className="p-3 bg-light border"
                ),
            ]
        )
            # dbc.Col([
            #     dbc.Row([
            #         html.Div([
            #             #dcc.Input(id='my-input', type='text', value='Initial Text'),
            #             #html.Div(id='my-output-text', children='This text will be updated.')
            #         ],
            #         #className="p-3 bg-light border"),
            #         ),
            #     ])
            # ], width=4 #, style={'border': '1px solid'}
            # )
    ]
)

#################### The below was already commented out ####################

    # dbc.Row([
    #     dbc.Col([
    #         dbc.Row([
    #             html.Div([
    #                 html.H2("1. Will your trip be domestic or international?"),
    #                 dcc.RadioItems(
    #                     options=['Domestic (in NZ only)', 'International'],
    #                     value='Domestic (in NZ only)'
    #                 ),
    #             ],
    #             className="p-3 bg-light border")
    #         ])
    #     ], width=6, style={'border': '1px solid'}
    #     ),
    #     dbc.Col([
    #         dbc.Row([
    #             html.Div([
    #                 html.H2("2. Will your trip be one-way, return or multi-stage?"),
    #                     dcc.RadioItems(
    #                         options=['One-way', 'Return'],
    #                         value='Return'
    #                 ),
    #             ],
    #             className="p-3 bg-light border")
    #         ])
    #     ], width=6, style={'border': '1px solid'}
    #     ),
    # ]),

    #################### The above was already commented out ####################

################################# The below was already commented out

#html.H2("Your total CO2 emissions are:...",
#        id='emissions-output')
#style=dict(display='flex'))

# @app.callback(
#     Output('emissions-output','children'),
#     Input('dropdown-1','value'),
#     Input('dropdown-2','value')
# )
# def calculate_and_display_emissions(city1,city2):
#     emissions = calculate_emissions(city1, city2, emission_factors, 2025)
#     print(emissions)
#     return f'Output: {emissions}'

################################# The above was already commented out

# Making departure country restrict departure airport codes
@callback(
    Output('dropdown-3', 'options'),
    Input('dropdown-1','value')
)
def adjust_visible_departure_airport_codes(dep_country):
    df = routes[(routes['DepCountry'] == dep_country)]
    dep_airport_options = sorted(df['DepAirport'].unique())
    #print(dep_airport_options)
    return dep_airport_options

# Making departure country and departure airport restrict arrival countries
@callback(
    Output('dropdown-2', 'options'),
    Input('dropdown-1', 'value'),
    Input('dropdown-3', 'value')
)
def adjust_visible_arrival_country_names(dep_country, dep_airport_code):
    df = routes[((routes['DepCountry'] == dep_country) & (routes['DepAirport'] == dep_airport_code))]
    arrival_country_options = sorted(df['ArrCountry'].unique())
    #print(arrival_country_options)
    return arrival_country_options

# Making departure country, departure airport, and arrival country restrict arrival airport codes
@callback(
    Output('dropdown-4', 'options'),
    Input('dropdown-1','value'),
    Input('dropdown-3','value'),
    Input('dropdown-2','value'),
)
def adjust_visible_arrival_airport_codes(dep_country, dep_airport_code, arr_country):
    df = routes[((routes['DepCountry'] == dep_country) & (routes['DepAirport'] == dep_airport_code) & (routes['ArrCountry'] == arr_country))]
    arrival_airport_options = sorted(df['ArrAirport'].unique())
    #print(arrival_airport_options)
    return arrival_airport_options

# Calculating emissions based on chosen airports
@callback(
    Output('my-output-text','children'),
    Input('dropdown-3','value'),
    Input('dropdown-4','value')
)
def calculate_emissions_based_on_airports(dep_airport_choice, arr_airport_choice):
    df = routes
    df = df[((df['DepAirport'] == dep_airport_choice) & (df['ArrAirport'] == arr_airport_choice))]

    emissions_for_route = df['EmissionsKgsCO2e'] #Change this
    #emissions_for_route = emissions_for_route.astype(float)

    emissions = emissions_for_route.sum()/len(emissions_for_route)
    print(emissions)
    #emissions = 1
    return f"Emissions are: {emissions:.2f} in KgCO2e"


# html.H4("Air Travel Emissions Calculator"
    #         , className='h3'),
    # dbc.Row([
    #     html.Div(style={'height': '50px'}),
    # ]),
    # dbc.Row([
    #     dbc.Col([
    #         html.Div([
    #             html.Div(style={'height': '50px'}),
    #         ]), #className="p-3 bg-light border"),
    #     ], width=1), #, style={'border': '1px solid'}),
    # ]),
    # dbc.Row([
    #     html.Div([
    #         html.P("Welcome to AUT\'s air travel emissions calculator. As part of our commitment to sustainability, AUT has a target to reduce our overall greenhouse gas emissions by 50 percent beneath 2018 levels by 2030."
    #                 " Air travel is an essential part of our business. However, it has a substantial carbon footprint associated with it. This means that we need to consider alternative options and travel differently;"
    #                 " it is not simply about never travelling at all but rather evaluating and adjusting our travel habits and finding alternative ways for meeting and collaborating with our international partners and colleagues,"
    #                 " where we can. This calculator has been developed by AUT\'s Sustainability Team, to help AUT staff and students build a greater appreciation and understanding of the effect that carbon emissions from air travel have."
    #         )
    #     ], style={'color': '#ccc'})
    # ]),
    # dbc.Row([
    # html.H1("Info Icon Example"),
    #     html.Div([
    #         info_icon_fa,
    #         " This is some information."
    #     ], style={'color': '#ccc'}),
    #     html.Div([
    #         info_icon_bs,
    #         " More details here."
    #     ], style={'color': '#ccc'})
    # ]),


