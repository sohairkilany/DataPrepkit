# DataPrepKit/tests/test_categorical_encoding.py

import pandas as pd
import pytest
from Data import categorical_encoding

# Sample data for testing
sample_data = pd.DataFrame({'A': ['cat', 'dog', 'cat', 'bird', 'dog'], 'B': ['red', 'blue', 'green', 'red', 'blue']})


# Test encode_categorical function
def test_encode_categorical():
    encoded_data = categorical_encoding.encode_categorical(sample_data)

    # Check if categorical variables are encoded
    assert 'A_cat' in encoded_data.columns
    assert 'A_dog' in encoded_data.columns
    assert 'A_bird' in encoded_data.columns
    assert 'B_red' in encoded_data.columns
    assert 'B_blue' in encoded_data.columns
    assert 'B_green' in encoded_data.columns

    # Check if encoding is done correctly
    assert encoded_data['A_cat'].equals(pd.Series([1, 0, 1, 0, 0], name='A_cat'))
    assert encoded_data['B_red'].equals(pd.Series([1, 0, 0, 1, 0], name='B_red'))
