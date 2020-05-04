"""
    Get docket numbers of cases from juriscraper case internal API
"""

import pandas as pd
from time import sleep

import json

g_casefile = "idb_juriscraper_ready.csv"
g_progress_logfile = "progress.log"
g_result_log = "result.log"

f = open(g_progress_logfile, 'a+')
rf = open(g_result_log, 'a+')



df = pd.DataFrame.from_csv(g_casefile)



for index, row in df.iterrows():
    docket_raw = row['docket']
    docket_num = row['docket_padded']
    district = row['district_name']
    subdomain = district + "d"
    print(docket_num, subdomain)
    
    f.write("BEGIN,"+docket_num+","+subdomain+"\n")

    single_res_case = {}

    try:
        # juriscraper stuff
        single_res_case = {}
    except:
        single_res_case = {'error': 'query_err', 'docket_tried': docket_num, 'docket_raw': docket_raw, 'district_tried': subdomain, 'district_raw': district }
        print("error with case: ", single_res_case)

    ### write to result log the json string if got one case
    single_res_case_str = json.dumps(single_res_case_str)
    rf.write(single_res_case_str+"\n")

    f.write("END,"+docket_num+","+subdomain+"\n")
    # sleep about 150ms
    sleep(0.150)

f.close()
rf.close()