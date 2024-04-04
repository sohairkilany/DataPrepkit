
import pandas as pd

def encode_categorical(data):
    """
    Encode categorical variables in the dataset.

    Parameters:
    - data (DataFrame): Input dataset.

    Returns:
    - DataFrame: Dataset with categorical variables encoded.
    """
    # Select categorical columns
    categorical_columns = data.select_dtypes(include=['object']).columns

    # One-hot encoding for categorical variables
    encoded_data = pd.get_dummies(data, columns=categorical_columns)

    return encoded_data
