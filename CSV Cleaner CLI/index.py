import argparse
import pandas as pd

def import_csv(file_path):
    return pd.read_csv(file_path)

def clean_duplicates(df):
    df.drop_duplicates()

def strip_spaces(df):
    return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

def save_file(df, path):
    df.to_csv(path, index=False)
    print(f'File save in: {path}')

def main():
    parser = argparse.ArgumentParser(description="CSV file cleaner")

    parser.add_argument("--file_path", type=str, required=True, help="Original path of the CSV file.")
    parser.add_argument("--output", type=str, required=True, help="Path to save the clean file.")
    parser.add_argument("--clean_duplicates", action="store_true", help='Removes duplicate rows.')
    parser.add_argument("--remove_spaces", action="store_true", help='Remove white spaces from text.')

    args = parser.parse_args()

    df = import_csv(args.file_path)

    if args.clean_duplicates:
        df = clean_duplicates(df)

    if args.remove_spaces:
        df = strip_spaces(df)

    save_file(df, args.output)

if __name__ == "__main__":
    main()