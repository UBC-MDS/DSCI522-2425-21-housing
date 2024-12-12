# Preprocess the data

# preprocess_data.py
# author: Thamer Aldawood
# date: 2024-12-05

import pandas as pd
import click
import pickle
from src.preprocess_utils import create_preprocessor, validate_categorical_levels

@click.command()
@click.option('--train-data', type=str, help="Path to train data")
@click.option('--write-to', type=str, help="Path to directory where preprocessed data will be written to")
def main(train_data, write_to):
    """
    Preprocesses the data, performs validation, and saves the preprocessor to disk.
    """
    # Load the training data
    train_df = pd.read_csv(train_data)
    
    # Validate categorical levels
    invalid_values = validate_categorical_levels(train_df, ['garage', 'firepl', 'bsmt', 'bdevl'], {'Y', 'N'})
    if invalid_values:
        raise ValueError(f"Invalid values found in categorical columns: {invalid_values}")
    
    # Create the preprocessor
    preprocessor = create_preprocessor(['garage', 'firepl', 'bsmt', 'bdevl'], ['meters'])
    
    # Save the preprocessor to disk
    pickle.dump(preprocessor, open(f"{write_to}/preprocessor.pickle", "wb"))

if __name__ == '__main__':
    main()
