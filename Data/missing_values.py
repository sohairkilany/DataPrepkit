
import pandas as pd

def handle_missing_values(data, strategy='remove'):
    """
    Handle missing values in the dataset.

    Parameters:
    - data (DataFrame): Input dataset.
    - strategy (str): Strategy for handling missing values ('remove' or 'impute'). Default is 'remove'.

    Returns:
    - DataFrame: Dataset with missing values handled according to the specified strategy.
    """
    if strategy == 'remove':
        # Remove rows with missing values
        cleaned_data = data.dropna()
        return cleaned_data
    elif strategy == 'impute':
        # Impute missing values using mean
        imputed_data = data.fillna(data.mean())
        return imputed_data
    else:
        raise ValueError("Invalid strategy. Please choose either 'remove' or 'impute'.")

