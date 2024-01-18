import dash
from dash import ALL, Input, Output, State, callback, ctx, dcc, html, no_update, Dash
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import dash_mantine_components as dmc
import plotly.express as px

# import pandas as pd
# import numpy as np

from constants import df, archetypes_states

dash.register_page(__name__, path='/')
layout = html.Div([
    html.Header(html.H1("US Archetypes")),
    html.Div([
    html.Br(),
    dbc.RadioItems(['share', 'volume'], 'share', id='metric-dropdown', inline=True, label_checked_style={'color':'darkgrey', 'text-decoration':'underline dotted'}),
    html.Div(
        [
            html.Div([dcc.Link(href='/summary?archetype=REBOOT SUSTAINABLE GROWTH', children=[html.Div(children="REBOOT SUSTAINABLE GROWTH", className='archetype-title'), html.Img(src='assets/a1_map.png')], id='a1Link', title='REBOOT SUSTAINABLE GROWTH'), dcc.Graph(figure={}, id='a1-chart')], className='archetype-container one'),
            html.Div([html.Div(children="DRIVE MULTI-CATEGORY FUTURE", className='archetype-title'), html.Img(src='assets/a2_map.png'), dcc.Graph(figure={}, id='a2-chart')], className='archetype-container two'),
            html.Div([html.Div(children="ACCELERATE CATEGORY LEADERSHIP", className='archetype-title'), html.Img(src='assets/a3_map.png'), dcc.Graph(figure={}, id='a3-chart')], className='archetype-container three'),
            html.Div([html.Div(children="TURNAROUND TRADITIONAL CATEGORIES", className='archetype-title'), html.Img(src='assets/a4_map.png'), dcc.Graph(figure={}, id='a4-chart')], className='archetype-container four'),
            html.Div([html.Div(children="PROTECT PREMIUM PROFITABILITY ", className='archetype-title'), html.Img(src='assets/a5_map.png'), dcc.Graph(figure={}, id='a5-chart')], className='archetype-container five'),
            html.Div([html.Div(children="ACCELERATE NEW CATEGORY GROWTH", className='archetype-title'), html.Img(src='assets/a6_map.png'), dcc.Graph(figure={}, id='a6-chart')], className='archetype-container six'),
            html.Div([html.Div(children="WIN ORAL HEARTLAND", className='archetype-title'), html.Img(src='assets/a7_map.png'), dcc.Graph(figure={}, id='a7-chart')], className='archetype-container seven'),
            html.Div([html.Div(children="MULTI CATEGORY GROWTH ENGINE", className='archetype-title'), html.Img(src='assets/a8_map.png'), dcc.Graph(figure={}, id='a8-chart')], className='archetype-container eight'),
            # html.Div(id='test')
        ],
        className='page-content'),
    ],
    # className='content'
    ),
    html.Div(html.Img(src='assets/cats.svg', style={'width':'20%', 'color':'red'}), style={'text-align':'center'})
])


def create_figs(archetype, metric):
    fig = px.bar(df[df['archetype'] == archetype], x='year', y=metric, color='category', text_auto='d')
    fig.update_xaxes(type='category', showgrid=False, showticklabels=True, title="", color= '#FFF')
    fig.update_yaxes(showgrid=False, showticklabels=False, visible=False)
    fig.update_layout(showlegend=False, margin=dict(l=3,r=3,b=30,t=0,pad=15))
    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
    fig.update_traces(textfont_color='white')
    gdf = df[df['archetype'] == archetype].groupby(['year', 'archetype']).sum()
    gdf = gdf.reset_index()
    gdf['volume'] = round(gdf['volume'])
    if metric == 'volume':
        fig.add_scatter(x=gdf['year'], y=gdf['volume'], name='Total Volume', text=gdf['volume'], textposition='top center', mode='lines+markers+text', textfont_color='white') #Check color and size for labels (make them bold)
    return fig

@callback(
    Output("a1-chart", "figure"),
    Output("a2-chart", "figure"),
    Output("a3-chart", "figure"),
    Output("a4-chart", "figure"),
    Output("a5-chart", "figure"),
    Output("a6-chart", "figure"),
    Output("a7-chart", "figure"),
    Output("a8-chart", "figure"),
    Input("metric-dropdown", "value"),
    )

def create_fig(metric):
    return tuple([create_figs(archetype, metric) for archetype in archetypes_states.keys()])

