import json
import pandas as pd

"""
    read results.log
"""
def read_json_lines(fpath):
    obj_arr = []
    f = open(fpath, 'r')
    for line in f.readlines():
        obj = json.loads(line)
        obj_arr.append(obj)
    
    df = pd.DataFrame.from_records(obj_arr)
    # print(df)

    df['docket_judge_initials'] = df.title.str.split(' ').str[0].str.split('-').str[3].str.split('-')
    # the first judge's fml initial
    df['fml_initial'] = df.title.str.split(' ').str[0].str.split('-').str[3].str.split('-').str[0]


    # print(df)
    
    return df


df_cases = read_json_lines("result_full.log")



df= pd.from_csv("data/all_judges.csv")
cdf = pd.merge(df, df_cases, how='inner', on='fml_initial')
# cdf['district_name'] = cdf['district_name'].str.lower()
# cdf['docket_padded'] = cdf.apply(lambda l: pad_docket_by_year(l.docket), axis=1)

# print(cdf)

cdf.to_csv('idb_pacer_judges_matches.csv')