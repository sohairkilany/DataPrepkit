import pytest
import pandas as pd
from Data import data_reader

# Sample data for testing
sample_csv_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
sample_excel_data = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})
sample_json_data = pd.DataFrame({'P': [13, 14, 15], 'Q': [16, 17, 18]})

# Test read_csv function
def test_read_csv(tmp_path):
    file_path = "test.csv"
    sample_csv_data.to_csv(file_path, index=False)
    data = data_reader.read_csv(file_path)
    assert data.equals(sample_csv_data)

# Test read_excel function
def test_read_excel(tmp_path):
    file_path =  "test.xlsx"
    sample_excel_data.to_excel(file_path, index=False)
    data = data_reader.read_excel(file_path)
    assert data.equals(sample_excel_data)

# Test read_json function
def test_read_json(tmp_path):
    file_path =  "test.json"
    sample_json_data.to_json(file_path)
    data = data_reader.read_json(file_path)
    assert data.equals(sample_json_data)
