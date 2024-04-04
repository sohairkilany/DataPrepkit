# to read data with different format, this code defines three functions read_csv, read_excel, and read_json,
import pandas as pd

def read_csv(file_path):
    """
    Read data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - DataFrame: Pandas DataFrame containing the data.
    """
    return pd.read_csv(file_path)

def read_excel(file_path, sheet_name=0):
    """
    Read data from an Excel file.

    Parameters:
    - file_path (str): Path to the Excel file.
    - sheet_name (str or int): Name or index of the sheet to read (default is 0).

    Returns:
    - DataFrame: Pandas DataFrame containing the data.
    """
    return pd.read_excel(file_path, sheet_name=sheet_name)

def read_json(file_path):
    """
    Read data from a JSON file.

    Parameters:
    - file_path (str): Path to the JSON file.

    Returns:
    - DataFrame: Pandas DataFrame containing the data.
    """
    return pd.read_json(file_path)
