import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess_utils import create_preprocessor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def test_create_preprocessor():
    categorical_features = ['garage', 'firepl']
    numeric_features = ['meters']
    preprocessor = create_preprocessor(categorical_features, numeric_features)
    
    assert isinstance(preprocessor, ColumnTransformer), "Expected a ColumnTransformer object."
    assert len(preprocessor.transformers) == 2, "Expected two transformers (categorical and numeric)."
    assert isinstance(preprocessor.transformers[0][1], OneHotEncoder), "First transformer should be OneHotEncoder."
    assert isinstance(preprocessor.transformers[1][1], StandardScaler), "Second transformer should be StandardScaler."


import pandas as pd
from src.preprocess_utils import validate_categorical_levels

def test_validate_categorical_levels():
    df = pd.DataFrame({'garage': ['Y', 'N', 'Y', 'Z']})
    invalid_values = validate_categorical_levels(df, ['garage'], {'Y', 'N'})
    
    assert 'garage' in invalid_values, "Expected 'garage' to have invalid values."
    assert invalid_values['garage'] == {'Z'}, "Expected 'Z' to be flagged as invalid."

