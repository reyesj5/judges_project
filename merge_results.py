import json
import pandas as pd


def read_json_lines(fpath):
    """
        read results.log
    """
    obj_arr = []
    f = open(fpath, 'r')
    for line in f.readlines():
        obj = json.loads(line)
        obj_arr.append(obj)

    df = pd.DataFrame.from_records(obj_arr)

    # df['docket_judge_initials'] = df.title.str.split(
    #     ' ').str[0].str.split('-').str[3].str.split('-')
    # the first judge's fml initial
    df['fml_initial'] = df.title.str.split(
        ' ').str[0].str.split('-').str[3].str.split('-').str[0]
    df = df.rename(columns={"query_district": "district_name", "query_docket_number_padded": "docket_padded", "query_docket_number_raw": "docket"})
    return df


def no_match_csv():
    # Getting results from the log file
    with open('results/progress_full.log', 'r') as log:
        lines = log.readlines()
        no_matches = ['result,docket_padded,docket,district_name\n']
        for line in lines:
            if line.split(',')[0] == 'NONE':
                no_matches.append(line[:-2] + '\n')
        with open('results/no_match_dockets.csv', 'w') as no_match:
            no_match.writelines(no_matches)


if __name__ == '__main__':
    df_cases = read_json_lines("result_full.log")
    df = pd.read_csv("data/all_judges.csv")
    cdf = pd.merge(df, df_cases, how='inner', on='fml_initial')
    cdf = cdf.drop(columns=['Unnamed: 0'])
    cdf.to_csv('results/idb_pacer_judges_matches.csv')
    df_cases.to_csv("results/results_full.csv")

    # Checking which dockets DID NOT produce a result
    no_match_csv()
    dtype = {'district': "string",
             'docket': "string", 'district_name': "string", 'office': "string"}
    cases_df = pd.read_csv('data/idb_juriscraper_ready.csv', dtype=dtype)
    no_match_df = pd.read_csv('results/no_match_dockets.csv', dtype=dtype)
    no_match_cases = pd.merge(cases_df, no_match_df, how='inner', on=['docket','district_name'])
    no_match_cases = no_match_cases.drop(columns=['Unnamed: 0'])
    no_match_cases.to_csv('results/no_match_cases.csv')

    # Checking which dockets DID produce a result
    match_cases = pd.merge(cases_df, df_cases, how='inner', on=['docket','district_name'])
    match_cases = match_cases.drop(columns=['Unnamed: 0','docket_padded_x','docket_padded_y'])
    match_cases.to_csv('results/match_cases.csv')
