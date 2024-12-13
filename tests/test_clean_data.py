import pytest
import pandas as pd
import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.clean_data import drop_outliers

# Load csv should use pandas to read a CSV from a secure url then save the raw csv to a given path

def test_drop_outliers():

    # Set threshold for number of allowed outliers
    threshold = 2

    # Set the random seed for reproducibility
    np.random.seed(42)

    # Generate random data
    data = {
        'Feature1': np.random.normal(loc=50, scale=10, size=100),  # Normal distribution with mean 50 and std deviation 10
        'Feature2': np.random.normal(loc=30, scale=5, size=100)    # Normal distribution with mean 30 and std deviation 5
    }

    # Introduce outliers
    outliers = {
        'Feature1': [150, -10, 200],
        'Feature2': [80, -20, 100]
    }

    # Combine data and outliers
    data['Feature1'] = np.concatenate([data['Feature1'], outliers['Feature1']])
    data['Feature2'] = np.concatenate([data['Feature2'], outliers['Feature2']])

    # Create a DataFrame
    df_outliers = pd.DataFrame(data)

    # Running load_csv to let it write the csv from the url
    df = drop_outliers(df_outliers, 2)

    assert not df.equals(df_outliers), "Outliers are not being dropped"