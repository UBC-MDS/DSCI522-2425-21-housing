

import os
import sys
import pandas as pd
import pickle
import tempfile
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model_fitting_util import perform_cross_validation_and_save

def test_perform_cross_validation_and_save():
    """
    Tests the `perform_cross_validation_and_save` function.
    """
    # Generate synthetic data
    from sklearn.datasets import make_regression
    X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a simple pipeline
    preprocessor = StandardScaler()
    pipeline = make_pipeline(preprocessor, Ridge())

    # Temporary directory for saving results
    with tempfile.TemporaryDirectory() as temp_dir:
        results_path = os.path.join(temp_dir, "cross_val_results.csv")

        # Perform cross-validation and save results
        cross_val_results = perform_cross_validation_and_save(pipeline, X_train, y_train, results_path, cv=5)

        # Verify results file exists
        assert os.path.exists(results_path), "Cross-validation results file was not created."

        # Verify contents of the results file
        saved_results = pd.read_csv(results_path, index_col=0)
        assert not saved_results.empty, "Cross-validation results file is empty."