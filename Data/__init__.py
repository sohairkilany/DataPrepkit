# Importing modules for easy access
from .data_reader import read_csv, read_excel, read_json
from .data_summary import generate_summary
from .missing_values import handle_missing_values
from .categorical_encoding import encode_categorical

# Specifying the version of the package
__version__ = "1.0.0"

# Specifying package metadata
__author__ = "Sk"
__email__ = "Sohairalikilany@gmail.com"
__description__ = "Python package named DataPrepKit This package aims to be a comprehensive toolkit for preprocessing datasets"