"""
    Get docket numbers of cases from juriscraper case internal API
"""


from juriscraper.pacer.http import PacerSession
from juriscraper.pacer.hidden_api import PossibleCaseNumberApi

import pandas as pd
from time import sleep

import json
import six

# Set up
USERNAME = ""
PWD = ""
SLEEP_TIME = 0.15  # 150ms
docket_type_param = "cv"

# File names
cases_file = "data/idb_juriscraper_ready.csv"
progress_logfile = "results/progress_full.log"
result_log = "results/result_full.log"

docket_num_begin_after = ""
district_name_begin_after = ""
RECORD_ON = False
START_OVER = True


def open_session(username, password):
    pacer_sess = PacerSession(username=username, password=password)
    return pacer_sess


def get_juriscraper(pacer_sess, court_id, docket_id, office_id_param, docket_type_param):
    api = PossibleCaseNumberApi(court_id=court_id, pacer_session=pacer_sess)
    api.query(docket_id)
    return api.data(office_number=office_id_param, docket_number_letters=docket_type_param)


if __name__ == '__main__':
    plog = open(progress_logfile, 'a+')
    rlog = open(result_log, 'a+')
    pacer_sess = open_session(USERNAME, PWD)
    dtype = {'district': "string",
             'docket': "string", 'district_name': "string", 'docket_padded': "string"}
    df = pd.read_csv(cases_file)

    for index, row in df.iterrows():
        docket_raw = row['docket'] if isinstance(
            row['docket'], six.string_types) else str(row['docket'])
        docket_num = row['docket_padded'] if isinstance(
            row['docket_padded'], six.string_types) else str(row['docket_padded'])
        district = row['district_name']
        subdomain = district + "d"

        office_id_param = str(row['office'])

        if START_OVER:
            RECORD_ON = True

        if RECORD_ON:
            print(docket_num, subdomain)

            plog.write("BEGIN,"+docket_num+","+subdomain+"\n")

            single_res_case = {}

            try:
                # juriscraper stuff
                single_res_case = get_juriscraper(
                    pacer_sess, subdomain, docket_num, office_id_param, docket_type_param)
            except Exception as e:
                single_res_case = {'error': 'query_err', 'docket_tried': docket_num,
                                   'docket_raw': docket_raw, 'district_tried': subdomain, 'district_raw': district}
                print("error with case: ", single_res_case, e)

            if single_res_case == None:
                single_res_case_str = json.dumps({'error': 'result_none', 'docket_tried': docket_num,
                                                  'docket_raw': docket_raw, 'district_tried': subdomain, 'district_raw': district})
                print("none result with case: ", single_res_case)
                plog.write("NONE,"+docket_num+"," +
                           docket_raw+","+subdomain+"\n")
            elif 'error' in single_res_case:
                plog.write("ERR,"+docket_num+","+docket_raw+","+subdomain+"\n")
            else:
                # write to result log the json string if got one case
                single_res_case['query_docket_number_padded'] = docket_num
                single_res_case['query_docket_number_raw'] = docket_raw
                single_res_case['query_district'] = district
                single_res_case['query_district_code'] = subdomain
                single_res_case_str = json.dumps(single_res_case)
                rlog.write(single_res_case_str+"\n")

            plog.write("END,"+docket_num+","+docket_raw+","+subdomain+"\n")

            # sleep about 150ms
            sleep(SLEEP_TIME)
        elif (docket_num == docket_num_begin_after) and (subdomain == district_name_begin_after):
            RECORD_ON = True

        if index%100 == 0:
          print('#################################################################')
          print('Case {}'.format(index))
    plog.close()
    rlog.close()
