import pandas as pd

def load_company_data(file_path):
    df = pd.read_excel(file_path)
    return df