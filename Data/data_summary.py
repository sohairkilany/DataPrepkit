# to show
import pandas as pd

def generate_summary(data):
    """
    Generate summary statistics for the dataset.

    Parameters:
    - data (DataFrame): Input dataset.

    Returns:
    - DataFrame: Summary statistics DataFrame.
    """
    # Calculate basic summary statistics using Pandas
    summary = data.describe()

    # Additional summary statistics
    summary.loc['median'] = data.median()  # Median
    summary.loc['mode'] = data.mode().iloc[0]  # Mode
    summary.loc['std_dev'] = data.std()  # Standard Deviation

    return summary
