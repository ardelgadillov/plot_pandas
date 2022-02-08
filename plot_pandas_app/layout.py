import datetime
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc
from dash import html

from plot_pandas_app.dash_widgets import RadioGroup, SliderGroup, DropdownGroup

# from recharge.beam.layout_settings import settings_page

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '18rem',
    'padding': '1rem 1rem',
    'overflow-y': 'scroll',
    'rc-slider-track': {'background-color': 'red'}
}

# the styles for the main content position it to the right of the sidebar and add some padding.
CONTENT_STYLE = {
    'margin-left': '18rem',
    'margin-right': '0rem',
    'padding': '3rem 3rem',
}


def initialize_layout(df: pd.DataFrame):
    ##############################
    # Main settings widgets - Sidebar
    ##############################
    col = [{'label': col, 'value': col} for col in df.columns]

    # Chart type
    chart_type = DropdownGroup('chart_type_id', 'Chart Type', 'scatter',
                               [{'label': 'Scatter Plot', 'value': 'scatter'},
                                {'label': 'Line Plot', 'value': 'line'}])

    # X values
    x_var = DropdownGroup('x_var_id', 'x', df.columns[0], col)
    # Y values
    y_var = DropdownGroup('y_var_id', 'y', df.columns[0], col)

    # Sidebar layout
    sidebar = html.Div(
        [
            html.H4('PLOT PANDAS'),  # className='display-5'),
            html.Hr(),
            # Navigation bar
            dbc.Nav(
                [
                    dbc.NavLink('Dashboard', href='/', active='exact'),
                    dbc.NavLink('Other', href='/other', active='exact'),
                ],
                vertical=True,
                pills=True,
            ),

            html.Hr(),
            html.H5('Chart'),
            # Main settings widgets
            dbc.Form([chart_type, x_var, y_var])

        ],
        style=SIDEBAR_STYLE,
    )

    # Content Layout
    content = html.Div(id='page-content', style=CONTENT_STYLE, )

    #def initialize_layout():
    return html.Div([dcc.Location(id='url'), sidebar, content])


# Home page layout
dashboard_page = html.Div([html.H1("Chart"),
                           dcc.Graph(id='graph')])

# APP Layout: Sidebar + Content
# app_layout = initialize_layout
