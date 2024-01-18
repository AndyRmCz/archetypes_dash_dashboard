from ctypes import alignment
from turtle import width
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from constants import archetypes_states, political_disposition, df, pl_df, joiners

dash.register_page(__name__, path='/summary')

def layout(archetype=None, department_id=None, **other_unknown_query_strings):
    return [html.Div([
        html.Header(html.H1([dcc.Link(html.H4('Summary '), href='/'), html.P(id='summary-title', style={'color':'#FFC000'})])),
        html.Br(),
        dcc.Dropdown(list(archetypes_states.keys()), archetype, id='archetype-dropdown', style={'width':'60%','color':'#A6A6A6'}),
        html.Div(
        [
           html.Div(
               [
                    html.Div(
                        [
                        html.Div(html.H4(id='a-header'), className='card-header'),
                        html.Div(
                            [
                            html.H5('7%'), html.Br(),  #Modify to archetype value
                            html.P('TTL Nic NTO', style={'font-size':'.9vw'})
                            ],
                            style={'margin':'10px auto','padding':'0px 5px', 'display':'block', 'text-align':'center', 'border-left': '1px dashed  whitesmoke', 'border-right': '1px dashed  whitesmoke'},
                        ),
                            html.Div(
                                [
                                    html.Div(html.H6('Reynolds Legal Nic 2022'), style={'text-align':'center', 'margin-bottom':'5px'}),
                                    html.Div(
                                        [
                                            html.Div([html.P('32%'), html.Br(), html.P('Vol Share %', style={'font-size':'1vw'})], style={'width':'50%', 'text-align':'center', 'background-color':'#071631', 'padding':'3px', 'margin':'3px'}), #Modify to archetype value
                                            html.Div([html.P('27%'), html.Br(), html.P('NTO Share %', style={'font-size':'0.9vw'})],style={'width':'50%', 'text-align':'center', 'background-color':'#071631', 'padding':'3px', 'margin':'3px'}) #Modify to archetype value
                                        ],
                                        style={'display':'flex'}
                                    ) 
                                ], 
                                className='card-header', style={'white-space':'nowrap'}
                            ),
                        ],
                        className='summary-header'
                    ),
                    html.Div(id='states-logo', className='summary-header'), #Modify to archetype value with callback dictionary / create dictionary
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Cluster Characteristics"), 
                                    html.P("(YTD  Aug’23 STR & Grail Est.)", style={'font-size':'1vw'})
                                ], 
                                className='div-centered card-header'
                            ),
                            html.Div(
                                [
                                    html.Div(dcc.Graph(id='shareOfCategory'), className='inline-child', style={'width':'55%', 'padding': '0px 5px'}),
                                    html.Div([html.H6("Consumer Disposition"), html.Div(id='political'), html.Div(id='joiners'),html.Div([html.H6('Retail contruct'), html.Div("EDLP + Base", style={'font-size':'.8vw'})], style={'margin-top':'30px'})], className='inline-child div-centered', style={'width':'45%','border-left': 'solid #5A6DC5 2px'})
                                ],
                                className='inline-container'
                            ),
                            html.Div(
                                html.Table(
                                    [
                                    html.Tr(
                                        [
                                        html.Td(
                                            [
                                                html.Div('YTD Aug’23 STR', className='div-centered', style={'font-size':'8px'}),
                                                html.Div('Vol % Share', className='div-centered', style={'font-size':'8px'}),
                                                html.Div('Indexed to National', className='div-centered', style={'font-size':'8px'})
                                            ],
                                        ),
                                        html.Td(html.Div('FMC', className='div-centered', style={'font-size':'10px', 'font-weight': 'bold'})),
                                        html.Td(html.Div('Trad Oral', className='div-centered', style={'font-size':'10px', 'font-weight': 'bold'})),
                                        html.Td(html.Div('NMO', className='div-centered', style={'font-size':'10px', 'font-weight': 'bold'})),
                                        html.Td(html.Div('Rechargables', className='div-centered', style={'font-size':'10px', 'font-weight': 'bold'})),   
                                        ]  
                                    ),
                                    html.Tr(
                                        [
                                        html.Td(html.Div('Category', className='div-centered', style={'font-size':'10px', 'font-weight': 'bold'})),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),   
                                        ]                                         
                                    ),
                                    html.Tr(children=
                                        [
                                        html.Td(html.Div('Price', className='div-centered', style={'font-size':'10px', 'font-weight': 'bold'})),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),   
                                        ]                                    
                                    ),
                                    html.Tr(
                                        [
                                        html.Td(html.Div('Menthol/Flavor', className='div-centered', style={'font-size':'10px', 'font-weight': 'bold'})),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),   
                                        ]                                         
                                    ),
                                    html.Tr(
                                        [
                                        html.Td(html.Div('Portfolio strength', className='div-centered', style={'font-size':'10px', 'font-weight': 'bold'})),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),
                                        html.Td(children='-', className='div-centered'),   
                                        ]                                         
                                    )
                                    ],
                                    style={'width':'100%'}
                                ), 
                                style={'border-top':'solid #5A6DC5 2px'}
                            )
                        ]
                    )
               ], 
               className='page-card'
               ,style={'width':'35%'}
            ),
           html.Div([html.Div("STR Vol Share of FMC", className='card-title'), html.Div("2019-YTD Aug’23", className='card-title', style={'margin-bottom':'30px'}), dcc.Graph(figure={}, id='fmc_chart', style={'height':'88%'}),], className='page-card div-centered'),
           html.Div([html.Div("STR Vol Share of", className='card-title'), html.Div("Rechargeables", className='card-title'), html.Div("2019-YTD Aug’23", className='card-title'), dcc.Graph(id='vpr_chart', style={'height':'85%'})], className='page-card div-centered'),
           html.Div([html.Div("STR Vol Share of", className='card-title'), html.Div("Trad Oral (Moist+Snus)", className='card-title'), html.Div("2019-YTD Aug’23", className='card-title'), dcc.Graph(id='to_chart', style={'height':'88%'})], className='page-card div-centered'),    
        ],
        className='page-content')
    ]),
    dcc.Location(id='url')]



@callback(
    Output('summary-title', 'children'),
    Output('a-header', 'children'),
    Output('states-logo', 'children'),
    Output('shareOfCategory', 'figure'),
    Output('political', 'children'),
    Output('joiners', 'children'),
    Output('fmc_chart', 'figure'),
    Output('vpr_chart', 'figure'),
    Output('to_chart', 'figure'),
    Input('archetype-dropdown', 'value')
)
def update_title(a):
    cat_df = df[(df['year'] == '22') & (df['archetype'] == a)]
    cat_fig = px.pie(cat_df, values='share', names='category', hole=.7)
    cat_fig.update_layout(height=280)
    cat_fig.update_layout(showlegend=False, margin=dict(l=15,r=15,b=15,t=10,pad=0),)
    cat_fig.update_yaxes(automargin=True)
    cat_fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})

    fmc_pls = ['60-FAMILY: NAS', '60-FAMILY: NEWPORT','60-FAMILY: CAMEL', '60-FAMILY: PALL MALL BOX', '60-FAMILY: LUCKYSTR']
    fmc_df = pl_df[(pl_df['archetype'] == a) & (pl_df['category'] == 'FMC') & (pl_df['pl'].isin(fmc_pls))]
    fmc_fig = px.bar(fmc_df, x='year', y='share', color='pl', text_auto='d', category_orders={"pl": fmc_pls}, color_discrete_sequence=["#FFC000", "#0F0", "#66CCFF", "#002060", "#F00"])
    fmc_fig.update_xaxes(type='category', showgrid=False, showticklabels=True, title="", color= '#FFF')
    fmc_fig.update_yaxes(showgrid=False, showticklabels=True, visible=False)
    fmc_fig.update_layout(legend_title_text='' , legend_font_color='#FFF', legend_font_size=8, legend_font_family='Montserrat', legend_xref='container', legend_yref='container', legend_x=.1, legend_y=-4, showlegend=True, margin=dict(l=3,r=3,b=0,t=0,pad=0))
    fmc_fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
    fmc_fig.update_traces(textfont_color='white')
    # fmc_fig.update_traces(marker_autocolorscale=True, marker_color=['#ABC','#F00','#0F0', '#00F','#123'])
    # fmc_fig.update_yaxes(automargin=True)
    fmc_gdf = pl_df[(pl_df['archetype'] == a) & (pl_df['category'] == 'FMC') & (pl_df['pl'] == "90-RECIPIE RAI OPCO'S CIG (Pro forma)")]
    fmc_fig.add_scatter(x=fmc_gdf['year'], y=fmc_gdf['share'], name="90-RECIPIE RAI OPCO'S CIG (Pro forma)", text=fmc_gdf['share'], textposition='top center', mode='lines+markers+text', textfont_color='white', marker_color="#4BA5FF")
    
    vpr_pls = ['60-FAMILY: VUSE (VAPOR)', '90-RECIPIE: JUUL CARTRIDGES','90-RECIPIE: NJOY CARTRIDGES', '90-RECIPIE: BLU CARTRIDGES', 'Others']
    vpr_df = pl_df[(pl_df['archetype'] == a) & (pl_df['category'] == 'Vapor')]
    vpr_fig = px.bar(vpr_df, x='year', y='share', color='pl', text_auto='d', category_orders={"pl": vpr_pls}, color_discrete_sequence=["#00FF99", "#7030A0", "#D918E8", "#0070C0", "#A6A6A6"])
    vpr_fig.update_xaxes(type='category', showgrid=False, showticklabels=True, title="", color= '#FFF')
    vpr_fig.update_yaxes(showgrid=False, showticklabels=True, visible=False)
    vpr_fig.update_layout(legend_title_text='' , legend_font_color='#FFF', legend_font_size=8, legend_font_family='Montserrat', legend_xref='container', legend_yref='container', legend_x=.1, legend_y=-10, showlegend=True, margin=dict(l=3,r=3,b=20,t=30,pad=5))
    vpr_fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
    vpr_fig.update_traces(textfont_color='white')
    # fmc_fig.update_traces(marker_autocolorscale=True, marker_color=['#ABC','#F00','#0F0', '#00F','#123'])
    # fmc_fig.update_yaxes(automargin=True)
    # vpr_gdf = pl_df[(pl_df['archetype'] == a) & (pl_df['category'] == 'Vapor') & (pl_df['pl'] == "90-RECIPIE RAI OPCO'S CIG (Pro forma)")]
    # vpr_fig.add_scatter(x=vpr_gdf['year'], y=vpr_gdf['share'], name="90-RECIPIE RAI OPCO'S CIG (Pro forma)", text=vpr_gdf['share'], textposition='top center', mode='lines+markers+text', textfont_color='white', marker_color="#4BA5FF")
    
    to_pls =["MOIST LOW END", "GRIZZLY", "KODIAK","CAMEL SNUS", "COUGAR", "COPENHAGEN"]
    to_df = pl_df[(pl_df['archetype'] == a) & (pl_df['category'] == 'Trad Oral')]
    to_fig=px.line(to_df, x='year', y='share', color='pl', text='share', category_orders={"pl": to_pls}, color_discrete_sequence=["#F00", "#00B050", "#66CCFF", "#9900CC", "#A6A6A6", "#FBBA00"],)
    to_fig.update_xaxes(type='category', showgrid=False, showticklabels=True, title="", color= '#FFF')
    to_fig.update_yaxes(showgrid=False, showticklabels=True, visible=False)
    to_fig.update_layout(legend_title_text='' , legend_font_color='#FFF', legend_font_size=8, legend_font_family='Montserrat', legend_xref='container', legend_yref='container', legend_x=.1, legend_y=-4, showlegend=True, margin=dict(l=10,r=10,b=20,t=35,pad=5))
    to_fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
    to_fig.update_traces(textfont_color='white')
    # to_fig.update_traces(textposition="top center")

    return (
        f'|  {a}',
        a, 
        [html.Img(src=f'assets/states/{state}.png', style={'width':'8%', 'height':'8%'}) for state in archetypes_states[a]],
        cat_fig,
        [html.Img(src=f'assets/political/{p}.png', style={'width':'30%', 'height':'30%'}) for p in political_disposition[a]],
        [html.Img(src=f'assets/{joiner}.png', style={'margin':'0px auto -10px auto', 'padding':'0px auto', 'display':'block','width':'80%', 'height':'10%'}) for joiner in joiners[a]],
        fmc_fig,
        vpr_fig,
        to_fig
    )