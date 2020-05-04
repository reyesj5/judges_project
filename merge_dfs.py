# python 3

import pandas as pd

df = pd.DataFrame.from_csv('idb.csv')
dist_df = pd.DataFrame.from_csv('districts.csv')

# print(df.head())

# print(dist_df.head())

cdf = pd.merge(df, dist_df, how='inner', on='district')


print(cdf.tail())

