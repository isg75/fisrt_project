def rename_client_columns(df):
    return df.rename(columns={
        "client_id": "id",
        "clnt_tenure_yr": "tenure_years",
        "clnt_tenure_mnth": "tenure_months",
        "clnt_age": "age",
        "gendr": "gender",
        "num_accts": "num_accounts",
        "bal": "balance",
        "calls_6_mnth": "calls_6_months",
        "logons_6_mnth": "logons_6_months",
    })

def rename_experiment_columns(df):
    df_copy = df.copy()
    df_copy.columns = df.columns.str.lower()
    return df_copy