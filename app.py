import dash
from dash import ALL, Input, Output, State, callback, ctx, dcc, html, no_update, Dash
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import dash_mantine_components as dmc
import plotly.express as px

# import pandas as pd
# import numpy as np

from constants import app

# server = app.server

# app = Dash(__name__, use_pages=True)
app.layout = html.Div(
    dash.page_container
)

if __name__ == '__main__':
    app.run(debug=True)