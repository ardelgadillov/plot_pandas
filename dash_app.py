import dash
import dash_bootstrap_components as dbc
import pandas as pd
from jupyter_dash import JupyterDash
from plot_pandas_app.layout import initialize_layout
from plot_pandas_app.callbacks import register_cache, register_callbacks


def plot_pandas(df: pd.DataFrame, mode='inline'):

    # dash_app_1 = dash.Dash(
    dash_app_1 = JupyterDash(
        __name__,
        suppress_callback_exceptions=True,
        external_stylesheets=[dbc.themes.FLATLY],
        # url_base_pathname='/app/',
        # update_title=None
    )

    # server = dash_app_1.server

    # with app.app_context():
    dash_app_1.title = 'Pandas Visualizer'
    dash_app_1.layout = initialize_layout(df)
    cache = register_cache(dash_app_1)
    register_callbacks(dash_app_1, cache, df)

    # Run server
    # if __name__ == '__main__':
    #    # dash_app_1.run_server(port=8050, debug=True)
    dash_app_1.run_server(port=8050, debug=True, mode=mode)


