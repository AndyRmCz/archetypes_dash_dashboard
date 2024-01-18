from pickle import FALSE
from tkinter.font import names
from turtle import title
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from constants import archetypes, archetypes_states

df = pd.read_csv('data/archetypes_category_share.csv', dtype={'year':str,'archetype':str,'category':str,'share':np.float32})
# df = px.data.tips()

# df = df[['year', 'archetype', 'category', 'share', 'volume']]
# df = df[df['archetype'] == archetypes[7]]
# # gdf = df.groupby(['category', 'year']).sum()
# # gdf = gdf.reset_index()
# # print(df)
# gdf = df.groupby(['year', 'archetype']).sum()
# gdf = gdf.reset_index()
# gdf['volume'] = round(gdf['volume'])
# print(gdf)

# fig = px.bar(df, x='year', y='volume', color='category')
# fig.update_xaxes(type='category', showgrid=False, showticklabels=True, title="")
# fig.update_yaxes(showgrid=False, showticklabels=False, visible=False)
# fig.update_layout(showlegend=False, margin=dict(l=0,r=0,b=0,t=50,pad=0))
# # line_fig = go.Scatter(gdf, x='year', y='volume')
# # fig.add_trace(line_fig)
# fig.add_scatter(x=gdf['year'], y=gdf['volume'])

# line = px.line(gdf, x='year', y='volume')
# # line.add_bar(x=df['year'], y=df['volume'])

cat_df = df[(df['year'] == '22') & (df['archetype'] == 'REBOOT SUSTAINABLE GROWTH')]
cat_fig = px.pie(cat_df, values='share', names='category', hole=.8, category_orders={'category':['CIG', 'MOIST', 'SNUS', 'NMO', 'VAPOR']})
cat_fig.show()
print(cat_df)



