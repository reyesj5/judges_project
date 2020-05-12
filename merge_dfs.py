# python 3

import pandas as pd


df = pd.DataFrame.from_csv('idb.csv')
dist_df = pd.DataFrame.from_csv('districts.csv')

# print(df.head())

"""
    year manipulation
"""
def pad_docket_by_year(y):
    x = str(y)
    if len(x) == 7:
        return x
    
    # this might be an ought's 2000's case
    if len(x) == 6:
        return "0" + x
    
    # this might be an exactly 2000 case?
    if len(x) <= 5:
        return "00" + x
    
    return x


cdf = pd.merge(df, dist_df, how='inner', on='district')
cdf['district_name'] = cdf['district_name'].str.lower()
cdf['docket_padded'] = cdf.apply(lambda l: pad_docket_by_year(l.docket), axis=1)

# pad up to seven docket digit numbers?

cdf.to_csv('idb_juriscraper_ready.csv')

