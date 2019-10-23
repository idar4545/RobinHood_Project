import numpy as np
import pandas as pd


def main():
    features_data = pd.read_csv('features_data_with_chunked.csv')
    for col in features_data.columns:
        a = set(features_data[col])
        print(a)
        print('________________________________________________________')

    any_dict = {
        'risk_tolerance' : {
            'low_risk_tolerance' : -1,
            'med_risk_tolerance' : 0,
            'high_risk_tolerance' : 1
        },
        'invensement_experience' : {
            'no_invensement_exp' : 0,
            'limited_invensement' : 2,
            'experience_invensement_exp' : 3
        },
        'liquidity_needs' : {
            'not_important_liq_need' : 1
            'very_important_liq_need' : 2
        },
        'platform' : {
            'Androied' : -1,
            'both' : 0,
            'iOS' : 1
        },
        'instrument_type_first_traded' : {
            '0' : 0,
            'wrt' : 1,
            'stock' : 2,
            'mlp' : 3,
            'tracking' : 4,
            'etp' : 5,
            'rlt' : 6,
            'adr' : 7,
            'reit' : 8,
            'lp' : 9,
            'cef' : 10
        },
        'time_horizon' : {
            'short_time_horizon' : 0,
            'med_time_horizon' : 1,
            'long_time_horizon' : 2
        }}
    print(any_dict)
    headers = features_data.columns
    for line in range(len(fatures_data['user_id'])):
        print(line)
        for header in headers:
            if header in any_dict:
                key = features_data[header][line] = any_dict[header][key]
    features_data.to_csv(r"features_data_with_numbers.csv")
if __name__ == '__main__':
    main()