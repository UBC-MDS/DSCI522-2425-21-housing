# Preprocess the data

# preprocess_data.py
# author: Thamer Aldawood
# date: 2024-12-05

import pandas as pd
import os
import click
import sys
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pickle

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--train-data', type=str, help="Path to train data")
@click.option('--write-to', type=str, help="Path to directory where preprocessed data will be written to")

def main(train_data, write_to):
    """Preprocesses and validates data then writes preprocessor to disk using Pickle
    ----------------

    Example: main("../data/train.csv",
    "522",
    "../results/models/")
    """

    # Lists of feature names
    categorical_features = ['garage', 'firepl', 'bsmt', 'bdevl']
    numeric_features = ['meters']
    train_df = pd.read_csv(train_data)

    # Create the column transformer
    preprocessor = make_column_transformer(
        (OneHotEncoder(), categorical_features),  # One-hot encode categorical columns
        (StandardScaler(), numeric_features),  # Standardize numeric columns
    )

    ### Validation step
    # Define the categorical features and their expected values
    expected_values = {'Y', 'N'}

    # Initialize a flag to track validation status
    all_categories_valid = True

    # Validate each categorical feature in the train_df
    for feature in categorical_features:
        unique_values = set(train_df[feature].dropna().unique())  # Get unique values excluding NaNs
        unexpected_values = unique_values - expected_values  # Find unexpected values

        if unexpected_values:
            print(f"❌ Unexpected values in column '{feature}' in train_df: {unexpected_values}")
            all_categories_valid = False
        else:
            print(f"✅ Category levels validation passed for column '{feature}' in train_df.")

    # Final message
    if all_categories_valid:
        print("✅ All categorical columns in train_df have the expected levels ('Y' and 'N').")
    else:
        print("❌ Some categorical columns in train_df have unexpected values. Please review.")

    #### Check for anomalous correlations between target and features
    # Apply preprocessing to train_df
    transformed_train = preprocessor.fit_transform(train_df)

    # Add the target variable back to the DataFrame
    transformed_train_df = pd.DataFrame(transformed_train)
    transformed_train_df.columns = ['Garage_Y', 'Garage_N', 'Fireplace_Y', 'Fireplace_N','Basement_Y', 'Basement_N',
                                    'BuildingEva_Y', 'BuildingEva_N','meters']
    # Add the target column back (assess_2022) to the transformed DataFrame
    transformed_train_df['assess_2022'] = train_df['assess_2022']

    # Compute correlation with the target variable
    correlation_with_target = transformed_train_df.corr()["assess_2022"].drop("assess_2022")

    # Identify features with anomalous correlations (correlation > 0.9 or < -0.9)
    threshold = 0.9
    anomalous_features = correlation_with_target[
        (correlation_with_target.abs() > threshold)
    ]

    if anomalous_features.empty:
        print("✅ No anomalous correlations found between target and features.")
    else:
        print("❌ Anomalous correlations detected:")
        print(anomalous_features)

    #### Check for anomalous correlations between features
    correlation_matrix = transformed_train_df.corr()
    threshold = 0.9

    # Define pairs of features that are binary inverses of each other (which are expected to be highly correlated)
    exclude_pairs = [
        ('Garage_Y', 'Garage_N'),
        ('Fireplace_Y', 'Fireplace_N'),
        ('Basement_Y', 'Basement_N'),
        ('BuildingEva_Y', 'BuildingEva_N')
    ]

    # Flag to check if any anomalous correlations were found
    anomalous_correlations_found = False

    # Iterate over the correlation matrix to check for high correlations
    for col1 in correlation_matrix.columns:
        for col2 in correlation_matrix.columns:
            if col1 != col2:
                # Skip pairs that are binary inverses
                if (col1, col2) in exclude_pairs or (col2, col1) in exclude_pairs:
                    continue
                # Check if correlation is above threshold
                if abs(correlation_matrix[col1][col2]) > threshold:
                    print(f"Warning: High correlation detected between {col1} and {col2}.")
                    anomalous_correlations_found = True

    # If no anomalous correlations are found, print the confirmation message
    if not anomalous_correlations_found:
        print("✅ No anomalous correlations found between target and features.")

    # Write validated preprocessor to disk using pickle
    pickle.dump(preprocessor, open(os.path.join(write_to, "preprocessor.pickle"), "wb"))

if __name__ == '__main__':
    main()