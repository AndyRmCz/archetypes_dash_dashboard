from re import X
import dash
import pandas as pd
import numpy as np

archetypes = ['REBOOT SUSTAINABLE GROWTH', 'DRIVE MULTI-CATEGORY FUTURE', 'ACCELERATE CATEGORY LEADERSHIP', 'TURNAROUND TRADITIONAL CATEGORIES', 'PROTECT PREMIUM PROFITABILITY ', 'ACCELERATE NEW CATEGORY GROWTH', 'WIN ORAL HEARTLAND', 'MULTI-CATEGORY GROWTH ENGINE']
archetypes_states = {'REBOOT SUSTAINABLE GROWTH' : ['DC', 'MA', 'CA'], 'DRIVE MULTI-CATEGORY FUTURE' : ['CO', 'MD', 'NJ', 'NY', 'OR', 'WA', 'PA'], 'ACCELERATE CATEGORY LEADERSHIP' : ['AK', 'CT', 'DE', 'HI', 'ME', 'MI', 'NH', 'RI', 'VT', 'GA', 'NC'], 'TURNAROUND TRADITIONAL CATEGORIES' : ['AL', 'AZ', 'IA', 'IL', 'KS', 'KY', 'LA', 'OK', 'SC', 'TN', 'VA', 'WI'], 'PROTECT PREMIUM PROFITABILITY ' : ['IN', 'OH', 'FL', 'PA'], 'ACCELERATE NEW CATEGORY GROWTH' : ['AR', 'MO', 'MS', 'WV', 'FL', 'GA', 'NC'], 'WIN ORAL HEARTLAND' : ['ID', 'MN', 'MT', 'ND', 'NE', 'NM', 'NV', 'SD', 'UT', 'WY'], 'MULTI-CATEGORY GROWTH ENGINE' : ['TX']}
political_disposition = {'REBOOT SUSTAINABLE GROWTH' : ['D'], 'DRIVE MULTI-CATEGORY FUTURE' : ['D'], 'ACCELERATE CATEGORY LEADERSHIP' : ['E', 'D'], 'TURNAROUND TRADITIONAL CATEGORIES' : ['E', 'D'], 'PROTECT PREMIUM PROFITABILITY ' : ['E', 'D'], 'ACCELERATE NEW CATEGORY GROWTH' : ['E'], 'WIN ORAL HEARTLAND' : ['E'], 'MULTI-CATEGORY GROWTH ENGINE' : ['E']}
joiners = {'REBOOT SUSTAINABLE GROWTH' : ['STREETWISE PIONEERS', 'TRENDY ASPIRATIONALS', 'SAVVY OPTIMIZERS'], 'DRIVE MULTI-CATEGORY FUTURE' : ['STATUS ACHIEVERS', 'STREETWISE PIONEERS', 'CONSCIOUS CONSIDERATES'], 'ACCELERATE CATEGORY LEADERSHIP' : ['STATUS ACHIEVERS', 'BOLD SOPHISTICATES', 'POPULAR APPROACHABLES'], 'TURNAROUND TRADITIONAL CATEGORIES' : ['POPULAR APPROACHABLES', 'RUGGED TRADITIONALISTS'], 'PROTECT PREMIUM PROFITABILITY ' : ['POPULAR APPROACHABLES', 'RUGGED TRADITIONALISTS'], 'ACCELERATE NEW CATEGORY GROWTH' : ['POPULAR APPROACHABLES', 'TRENDY ASPIRATIONALS', 'BOLD SOPHISTICATES'], 'WIN ORAL HEARTLAND' : ['POPULAR APPROACHABLES', 'STATUS ACHIEVERS', 'RUGGED TRADITIONALISTS'], 'MULTI-CATEGORY GROWTH ENGINE' : ['BOLD SOPHISTICATES', 'STREETWISE PIONEERS', 'TRENDY ASPIRATIONALS']}

df = pd.read_csv('data/archetypes_category_share.csv', dtype={'year':str,'archetype':str,'category':str,'share':np.float32})
pl_df = pd.read_csv('data/archetypes_pl_share.csv', dtype={'year':str,'archetype':str,'pl':str,'category':str,'share':np.float32})
# app = dash.Dash(
#     __name__,
#     suppress_callback_exceptions=True,
#     use_pages=True
# )

app = dash.Dash(
    'US Archetypes',
    use_pages=True,
    suppress_callback_exceptions=True
)

app.title = 'US Archetypes'

# def rise(x):
#     return x**x

# exes = [1,2,3,4]
# r = tuple([rise(x) for x in exes])
# print(r)