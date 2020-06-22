# python 3
import pandas as pd


def pad_docket_by_year(y):
    """
    year manipulation
    """
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


def merge_dbs(cases, districts):
    """
    Database merging
    """
    cdf = pd.merge(df, dist_df, how='inner', on='district')
    cdf['district_name'] = cdf['district_name'].str.lower()
    # pad up to seven docket digit numbers?
    cdf['docket_padded'] = cdf.apply(
        lambda l: pad_docket_by_year(l.docket), axis=1)
    cdf.to_csv('data/idb_juriscraper_ready.csv')


if __name__ == '__main__':
    dtype = {'district': "string",
             'docket': "string", 'district_name': "string", 'office': "string"}
    df = pd.read_csv('data/idb.csv', dtype=dtype)
    dist_df = pd.read_csv('data/districts.csv', dtype=dtype)
    merge_dbs(df, dist_df)
