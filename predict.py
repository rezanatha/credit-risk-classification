import pandas as pd
import pickle
from collections import defaultdict
import numpy as np

'''
INPUT FORMAT
{
    "person_age":40, # Person age in years
    "person_income": 50000, # Annual Income in $
    "person_home_ownership":"RENT", # Home ownership: RENT, MORTGAGE, OWN
    "person_emp_length":2, # How long this person has been employed in years
    "loan_intent": "MEDICAL", # What the loan is for: valid values are EDUCATION, MEDICAL, VENTURE, PERSONAL, DEBTCONSOLIDATION, HOMEIMPROVEMENT
    "loan_grade":"B", # Loan grade: A, B, C,..., G
    "loan_amnt": 10000, # Loan amount in $
    "loan_int_rate": 8.7, # Annual loan interest rate in %
    "cb_person_default_on_file":"N", # Has this person been default before? Y, N
    "cb_person_cred_hist_length":"5" # Credit history length in years
}
'''

'''
TARGET
loan_status: 0 = non-default, 1 = default
'''

with open('models/PREPROCESS-OHE-OE-IMP-SC-1.0.0.pkl', 'rb') as f:
    preprocess = pickle.load(f)
    
with open('models/MODEL-XGB-1.0.0.pkl', 'rb') as f:
    model = pickle.load(f)
    
def format_data(input_data):
    """reformat incoming JSON data into dataframe"""
    out = pd.DataFrame.from_dict(input_data, orient='index').T.replace({None: np.nan, "null": np.nan, '':np.nan})
    return out
    
def preprocess_data(input_data):
    """preprocess into dataframe just like development's"""
    return preprocess.transform(input_data)
    
    
def predict_data(input_data):
    data_ready = preprocess_data(format_data(input_data))
    result = model.predict_proba(data_ready)
    return result