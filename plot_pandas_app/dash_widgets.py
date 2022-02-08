import dash_bootstrap_components as dbc
from dash import dcc
from dash import html


# Return a dash_bootstrap_components Form for Numerical Input control
def InputGroup(id, label, value, min, max, step, **kw):
    style = kw.get('style') or {'display': 'block'}
    return html.Div([
        dbc.Label(label, html_for=id, size='sm'),  # style={'color': 'white'}
        dbc.Input(id=id, type='number', min=min, max=max, step=step, value=value, debounce=True,
                  persistence=id + '_value',
                  persistence_type='session')
    ])


# Return a dash_bootstrap_components Form for Dropdown control
def DropdownGroup(id, label, value, options, **kw):
    style = kw.get('style') or {'display': 'block'}
    return html.Div([
        dbc.Label(label, html_for=id, size='sm'),  # , style={'color': 'white'}
        dcc.Dropdown(id=id, options=options, value=value, persistence=id + '_value', persistence_type='session',
                     clearable=False)
    ])


# Return a dash_bootstrap_components Form for Radio control
def RadioGroup(id, label, value, options):
    if label is not None:
        radio_group = html.Div([
            dbc.Label(label, html_for=id, size='sm', style={'margin-right': '1rem'}),  # , 'color': 'white'
            dbc.RadioItems(id=id, options=options, value=value, persistence=id + '_value', persistence_type='session')
        ])
    else:
        radio_group = [
            dbc.RadioItems(id=id, options=options, value=value, persistence=id + '_value', persistence_type='session')
        ]
    return radio_group


# Return a dash_bootstrap_components Form for Upload File control
def UploadGroup(id, label, **kw):
    style = kw.get('style') or {'display': 'block'}
    return [
        # dbc.Label(label, html_for=id),
        dcc.Upload(
            id=id,
            children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
            style={
                'width': '100%',
                'height': '35px',
                'lineHeight': '35px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '5px',
                'color': 'white'
            })
    ]


# Return a dash_bootstrap_components Form for Slider control
def SliderGroup(id, label, value, min, max):
    return html.Div([
        dbc.Label(label, html_for=id, size='sm'),  # , style={'color': 'white', 'font-weight': 'bold'}),
        dcc.Slider(id=id, value=value, min=min, max=max, tooltip={'always_visible': True, 'placement': 'right'},
                   persistence=id + '_value', persistence_type='session'),
    ])
