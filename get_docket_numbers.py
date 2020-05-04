"""
    Get docket numbers of cases from juriscraper case internal API
"""

import pandas as pd
from time import sleep

g_casefile = "idb_juriscraper_ready.csv"
g_progress_logfile = "progress.log"

f = open(g_progress_logfile, 'w+')


df = pd.DataFrame.from_csv(g_casefile)



for index, row in df.iterrows():
    docket_num = row['docket_padded']
    subdomain = row['district_name'] + "d"
    print(docket_num, subdomain)
    # sleep about 150ms
    sleep(0.150)

f.close()