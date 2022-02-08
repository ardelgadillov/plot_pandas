import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px

from flask_caching import Cache
import uuid

import json
import base64
import pandas as pd
import numpy as np

from plot_pandas_app.layout import dashboard_page


# Create cache
def register_cache(dashapp):
    return Cache(dashapp.server, config={
        # try 'filesystem' if you don't want to setup redis
        'CACHE_TYPE': 'SimpleCache',  # 'FileSystemCache'
        'CACHE_DIR': 'cache-directory',
        'CACHE_THRESHOLD': 100,
        'CACHE_DEFAULT_TIMEOUT': 0  # 86400
    })


##############################
# APP Callbacks
##############################
def register_callbacks(dashapp, cache, df: pd.DataFrame):

    # Render Page set in Navigation Bar
    @dashapp.callback(Output('page-content', 'children'),
                      [Input('url', 'pathname')])
    def render_page_content(pathname):
        if pathname == '/':
            return dashboard_page
        elif pathname == '/other':
            return html.P('Oh cool, this is page 2!')
        # If the user tries to reach a different page, return a 404 message
        return html.Div(
            dbc.Container([
                html.H1('404: Not found', className='text-danger'),
                html.Hr(),
                html.P(f'The pathname {pathname} was not recognised...'),
            ]))

    # Define callback to update graph
    @dashapp.callback(
        Output('graph', 'figure'),
        [Input('chart_type_id', 'value'),
         Input('x_var_id', 'value'),
         Input('y_var_id', 'value')]
    )
    def update_figure(chart_type, x_var, y_var):
        if chart_type == 'scatter':
            fig = px.scatter(
                        df, x=x_var, y=y_var)
        else:
            fig = px.line(df, x=x_var, y=y_var)
        return fig

