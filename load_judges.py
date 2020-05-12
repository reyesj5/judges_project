"""
    walk the judges directory and build all judge jsons into a data frame
"""

import os
import json
import pandas as pd

dirname = "./judges_data/"
output_path_all_judges = "all_judges.test.csv"

# get all judge jsons
items_in_dir =  next(os.walk(dirname))[2]
items_in_dir = [f for f in items_in_dir if ".json" in f and f != "info.json"]

keep_fields = ['id', 'fjc_id', 'name_first', 'name_middle', 'name_last', 'date_dob']

all_judge_records = []

for json_file in items_in_dir:
    f = open(dirname + '/' + json_file)
    judge_obj = json.loads(f.read())
    
    # print(judge_obj)
    save_judge_obj = {}
    for fld in keep_fields:
        save_judge_obj[fld] = judge_obj[fld]
    
    # make fl initial
    try:
        save_judge_obj['fl_initial'] = (save_judge_obj['name_first'][0] + save_judge_obj['name_last'][0]).upper()
    except:
        print("create FL initial failed on judge: ", judge_obj)

    # make fml initial
    try:
        if len(save_judge_obj['name_middle']) > 0:
            save_judge_obj['fml_initial'] = (save_judge_obj['name_first'][0] + save_judge_obj['name_middle'][0] + save_judge_obj['name_last'][0]).upper()
        else:
            save_judge_obj['fml_initial'] = save_judge_obj['fl_initial']
    except:
        print("create FML initial failed on judge: ", judge_obj)
    
    all_judge_records.append(save_judge_obj)

    f.close()

df = pd.DataFrame.from_records(all_judge_records)
df.to_csv(output_path_all_judges)


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




cdf = pd.merge(df, df_cases, how='inner', on='fml_initial')
# cdf['district_name'] = cdf['district_name'].str.lower()
# cdf['docket_padded'] = cdf.apply(lambda l: pad_docket_by_year(l.docket), axis=1)

# print(cdf)

cdf.to_csv('idb_pacer_judges_matches.csv')