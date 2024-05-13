import pandas as pd
import numpy as np

def clean_dtypes(df):

    for col in df.columns:
        try:
            if (df[col].dtypes == "int64") & ("_id" not in col):
                df[col].fillna(df[col].mean(), inplace=True)
            elif df[col].dtypes == "float64":
                df[col].fillna(df[col].mean().round(2), inplace=True)
            elif (df[col].dtypes == "O") & ("Variation" not in col):
                df[col].fillna(df[col].mode()[0], inplace=True)
        except Exception as e:
            print(f"{e} during {col}")
    
<<<<<<< HEAD
    df.drop(columns=["Unnamed: 0"], axis=1,inplace=True)
=======
    df.drop(columns=["Unnamed: 0"], axis=1, inplace=True)
>>>>>>> 79e3852f3cca57ed2c048c8cfb40253df9d02ede
    df["date_time"] = pd.to_datetime(df["date_time"])
    df["clnt_tenure_yr"] = df["clnt_tenure_yr"].astype(int)
    df["clnt_tenure_mnth"] = df["clnt_tenure_mnth"].astype(int)
    df["clnt_age"] = df["clnt_age"].apply(np.ceil).astype(int)
    df["gendr"] = df["gendr"].apply(lambda x: "U" if "X" in x else x)
    df["calls_6_mnth"] = df["calls_6_mnth"].astype(int)
    df["logons_6_mnth"] = df["logons_6_mnth"].astype(int)
    df['num_account'] = df['num_account'].replace(2.26, 2)
    return df

def rename_columns(df):
    
<<<<<<< HEAD
    df.rename(columns={"clnt_tenure_yr": "client_years",
                            "clnt_tenure_mnth": "client_month",
=======
    df.rename(columns={"clnt_tenure_yr":"client_years",
                            "clnt_tenure_mnth":"client_month",
>>>>>>> 79e3852f3cca57ed2c048c8cfb40253df9d02ede
                            "clnt_age":"client_age",
                            "gendr":"gender",
                            "num_accts":"num_accounts",
                            "bal":"balance",
                            "calls_6_mnth":"calls_6_months",
                            "logons_6_mnth":"logins_6"},inplace= True)
    return df
