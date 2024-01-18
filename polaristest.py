import pandas as pd
def pr(df):
    print(df.index)
    return df
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

gdf = df.groupby('duration').apply(lambda idx: pr(idx))
print(gdf)

