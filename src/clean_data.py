# Clean and transform the data

# clean_data.py
# author: Thamer Aldawood
# date: 2024-12-05

import pandas as pd
import os
import click
from sklearn.model_selection import train_test_split
import sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--raw-data', type=str, help="Path to raw data")
@click.option('--seed', type=int, help="Seed to be used to randomly split train and test data")
@click.option('--write-to', type=str, help="Path to directory where cleaned data will be written to")

def main(raw_data, seed, write_to):
    """Cleans raw data and splits it into train and test data based on a given seed
    ----------------

    Example: main("../data/2023_Property_Tax_Assessment.csv",
    "522",
    "../data/")
    """
    np.random.seed(seed)
    ## Validation for correct data file format
    file_path = raw_data

    if not file_path.endswith(".csv"):
        raise ValueError("File format not supported.")
    else: 
        print("✅ File format validation passed: File is a CSV.")

    housing_df = pd.read_csv(raw_data)
    housing_df = housing_df[['meters','garage','firepl','bsmt','bdevl','assess_2022']]   

    ## Validation for correct column names
    expected_cols = {"meters", "garage", "firepl", "bsmt", "bdevl", "assess_2022"}
    actual_cols = set(housing_df.columns)

    if actual_cols == expected_cols:
        print("✅ Column name validation passed: All expected columns are present.")
    else:
        missing = expected_cols - actual_cols
        extra = actual_cols - expected_cols
        print("Column names validation failed:")
        if missing:
            print(f" Missing columns: {missing}")
        if extra:
            print(f" Extra columns: {extra}")

    ## Validation for No Empty Observations
    empty = housing_df.isna().all(axis = 1).sum()

    if empty == 0:
        print("✅ Empty observations validation passed: No empty rows.")
    else:
        print(f" Empty observations validation failed: Found {empty} empty rows.")

    ## Validation for missingness not beyond expected threshold
    expected_threshold = 0
    missing = housing_df.isna().mean()

    all_cols_passed = True

    for col, percentage in missing.items():
        if percentage > expected_threshold:
            all_cols_passed = False
            print(f"Column '{col}' exceeds the missingness expected threshold ({percentage:.2%} missing).")
    if all_cols_passed:
        print(f"✅ Missingness validation passed for all columns.")

    ## Validation for correct data types in each column 

    expected_dtypes = { "meters": "float64","garage": "object","firepl": "object","bsmt": "object", "bdevl": "object","assess_2022": "int64"}

    dtype_passed = True

    for col, dtype in expected_dtypes.items():
        if housing_df[col].dtypes != dtype:
            dtype_passed = False
            print(f"Data type validation failed: Column '{col}' is of type {housing_df[col].dtypes}, expected {dtype}.")
    if dtype_passed:
        print("✅ Data type validation passed for all columns.")

    ## Validation for no duplicate observations
    duplicates = housing_df.duplicated().sum()

    if duplicates == 0:
        print("✅ Duplicate observation validation passed: No duplicate rows found.")
    else:
        print(f"Duplicate observation validation failed: Found {duplicates} duplicate rows.")
        # Dropping duplicates
        housing_df = housing_df.drop_duplicates()
        print("✅ Duplicates have been removed from the DataFrame.")

    ## Validation for no outliers or anomalous values
    housing_df = drop_outliers(housing_df, 5000)

    # Splitting our cleaned and validated data into training and test data
    train_df, test_df = train_test_split(housing_df, test_size=0.3, random_state=seed)

    # Define the categorical features and their expected values
    categorical_features = ['garage', 'firepl', 'bsmt', 'bdevl']
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

    # Writing results to disk
    housing_df.to_csv(os.path.join(write_to, "Clean_2023_Property_Tax_Assessment.csv"), index=False)
    train_df.to_csv(os.path.join(write_to, "train.csv"), index=False)
    test_df.to_csv(os.path.join(write_to, "test.csv"), index=False)

if __name__ == '__main__':
    main()

def drop_outliers(df, threshold):
    """Identify and drop outliers if the threshold is exceeded
    ----------------

    Example: drop_outliers(
    df,
    5000,
    )
    """

    outliers_detected = False

    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        num_outliers = len(outliers)
        
        if num_outliers > threshold:
            outliers_detected = True
            print(f"Outlier validation failed: Column '{col}' has {num_outliers} outliers (threshold: {threshold}).")
            # Dropping the outliers
            df = df[~((df[col] < lower_bound) | (df[col] > upper_bound))]
            print(f"✅ Outliers in column '{col}' have been removed from the DataFrame.")
        elif num_outliers > 0:
            print(f"Warning: Column '{col}' has {num_outliers} outliers, within acceptable threshold ({threshold}).")

    if not outliers_detected:
        print("✅ Outlier validation passed: No columns exceed the outlier threshold.")
    else:
        print("✅ Outliers exceeding the threshold have been removed.")

    return df