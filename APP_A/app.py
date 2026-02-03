import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash (__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP]) #suppress_callback_exceptions=True)

#external_stylesheets = [dbc.themes.SIMPLEX, dbc.icons.FONT_AWESOME]

app.layout = html.Div(
    [
        dbc.Row(
            [
                html.Div(style={'height': '50px'}),
            ]
        ),
        dbc.Row(
            [
            dbc.Col(
                [
                html.Div(
                    [
                    html.Div(style={'height': '50px'}),
                    ]
                ),
                ], xs=3, sm=3, md=2, lg=2, xl=2, xxl=2),
            dbc.Col(
                [                                
                html.H4("Air Travel Emissions Calculator", className='h1'),
                ], xs=9, sm=9, md=10, lg=10, xl=10, xxl=10),
            ]
        ),
        dbc.Row(
            [
            html.Div(style={'height': '50px'}),
            ]
        ),
        dbc.Row(
            [
            dbc.Col(
                [
                html.Div(style={'height': '50px'}),
                ], xs=3, sm=3, md=2, lg=2, xl=2, xxl=2),
            dbc.Col(
                [
                html.Div(
                    [
                    html.Div(
                        dcc.Link(f"{page['name']}", href=page["relative_path"])
                    ) for page in dash.page_registry.values()
                    ]
                ),
                ], xs=3, sm=3, md=2, lg=2, xl=2, xxl=2),
            dbc.Col(
                [
                    dash.page_container
                ], xs=6, sm=6, md=8, lg=8, xl=8, xxl=8),
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)

# sidebar = dbc.Nav(
#             [
#                 dbc.NavLink(
#                     [
#                         html.Div(page["name"],className="ms-2"),
#                     ],
#                     href=page["path"],
#                     active="exact",
#                 )
#                 for page in dash.page_registry.values()
#             ],
#             vertical=True,
#             pills=True,
#             className="bg-light",
# )

#     dbc.Row(
#         [
#             # dbc.Col(
#             #     [
#             #         sidebar
#             #     ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
#             dbc.Col(
#                 [
#                     dash.page_container
#                 ], xs=4, sm=8, lg=10, xl=10, xxl=10)
#         ]
#     )
# ], fluid=True)

