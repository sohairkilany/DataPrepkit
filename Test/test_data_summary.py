# DataPrepKit/tests/test_data_summary.py

import pandas as pd
import pytest
from Data import data_summary

# Sample data for testing
sample_data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 9]})


# Test generate_summary function
def test_generate_summary():
    summary = data_summary.generate_summary(sample_data)

    # Check if summary contains basic statistics
    assert 'mean' in summary.index
    assert 'std' in summary.index
    assert 'min' in summary.index
    assert 'max' in summary.index

    # Additional statistics
    assert 'median' in summary.index
    assert 'mode' in summary.index
    assert 'std_dev' in summary.index

    # Check if summary statistics are accurate
    assert summary.loc['mean', 'A'] == pytest.approx(3.0, abs=0.01)
    assert summary.loc['median', 'B'] == 7
    assert summary.loc['mode', 'A'] == 1

# dd=data_summary.generate_summary(sample_data)
# print(dd)


