#models to import

import click
import os
import pandas as pd
import pickle
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_validate
from sklearn.pipeline import make_pipeline

@click.command()
@click.option('--train-data', type=str, help="Path to the training CSV file")
@click.option('--test-data', type=str, help="Path to the testing CSV file")
@click.option('--preprocessor', type=str, help="Path to preprocessor object")
@click.option('--results-to', type=str, help="Path to directory where results will be saved")
@click.option('--seed', type=int, default=123, help="Random seed for reproducibility")
def main(train_data, test_data, preprocessor, results_to, seed):
    """
    Fits a Ridge regression model using a preprocessor pipeline,
    performs cross-validation, and evaluates the model on the test set.
    """
    # Set random seed
    import numpy as np
    np.random.seed(seed)

    # Load training and testing data
    train_df = pd.read_csv(train_data)
    test_df = pd.read_csv(test_data)

    # Separate features and target
    X_train = train_df.drop(columns=["assess_2022"])
    y_train = train_df["assess_2022"]
    X_test = test_df.drop(columns=["assess_2022"])
    y_test = test_df["assess_2022"]

    # Load preprocessor
    with open(preprocessor, 'rb') as f:
        preprocessor_obj = pickle.load(f)

    # Define Ridge regression pipeline
    pipeline = make_pipeline(preprocessor_obj, Ridge())

    # Perform cross-validation
    cross_val_results = pd.DataFrame(
        cross_validate(pipeline, X_train, y_train, cv=5, return_train_score=True)
    ).agg(['mean', 'std']).round(3).T

    # Save cross-validation results
    results_file = os.path.join(results_to, "cross_val_results.csv")
    cross_val_results.to_csv(results_file)

    # Fit the pipeline to the training data
    pipeline.fit(X_train, y_train)

    # Evaluate the pipeline on the test data
    test_score = pipeline.score(X_test, y_test)

    # Save the trained model
    model_file = os.path.join(results_to, "ridge_pipeline.pickle")
    with open(model_file, 'wb') as f:
        pickle.dump(pipeline, f)
        
if __name__ == '__main__':
    main()

