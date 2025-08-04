import argparse
import pandas as pd

def import_csv(file_path):
    return pd.read_csv(file_path)

def clean_duplicates(df):
    df.drop_duplicates()

def strip_spaces(df):
    return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)