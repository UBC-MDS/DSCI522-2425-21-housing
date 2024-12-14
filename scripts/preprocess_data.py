# Preprocess the data

# preprocess_data.py
# author: Thamer Aldawood
# date: 2024-12-05

import click
import os
import pickle
import pandas as pd
from src.preprocess_utils import create_preprocessor, validate_categorical_levels
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--train-data', type=str, help="Path to train data")
@click.option('--write-to', type=str, help="Path to directory where preprocessed data will be written to")
def main(train_data, write_to):
    """
    Preprocesses and validates data, then writes preprocessor to disk using Pickle.
    """
    # Load the training data
    train_df = pd.read_csv(train_data)

    # Define feature categories
    categorical_features = ['garage', 'firepl', 'bsmt', 'bdevl']
    numeric_features = ['meters']

    # Validate categorical feature levels
    validate_categorical_levels(train_df, categorical_features, expected_values={'Y', 'N'})

    # Create the preprocessor
    preprocessor = create_preprocessor(categorical_features, numeric_features)

    # Fit the preprocessor to the training data (necessary for saving)
    preprocessor.fit(train_df)

    # Save the preprocessor to a pickle file
    os.makedirs(write_to, exist_ok=True)
    preprocessor_path = os.path.join(write_to, "preprocessor.pickle")
    with open(preprocessor_path, "wb") as f:
        pickle.dump(preprocessor, f)

    print(f"✅ Preprocessor saved to {preprocessor_path}")

if __name__ == '__main__':
    main()

