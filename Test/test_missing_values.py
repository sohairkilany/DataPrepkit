# DataPrepKit/tests/test_missing_values.py

import pandas as pd
import pytest
from Data import missing_values

# Sample data for testing
sample_data = pd.DataFrame({'A': [1, 2, None, 4, 5], 'B': [None, 6, 7, 8, 9]})


# Test handle_missing_values function
def test_handle_missing_values_remove():
    cleaned_data = missing_values.handle_missing_values(sample_data, strategy='remove')

    # Check if rows with missing values are removed
    assert cleaned_data.shape == (3, 2)
    assert cleaned_data.isnull().sum().sum() == 0


def test_handle_missing_values_impute():
    imputed_data = missing_values.handle_missing_values(sample_data, strategy='impute')

    # Check if missing values are imputed with mean
    assert imputed_data['A'].isnull().sum() == 0
    assert imputed_data['B'].isnull().sum() == 0
