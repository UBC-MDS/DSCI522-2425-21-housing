
import pandas as pd
from sklearn.model_selection import cross_validate

def perform_cross_validation_and_save(pipeline, X_train, y_train, results_path, cv=5):
    """
    Performs cross-validation on a given pipeline and training data,
    and saves the results to a specified path.

    Parameters:
        pipeline: sklearn.pipeline.Pipeline
            The pipeline to be evaluated.
        X_train: pd.DataFrame
            Training features.
        y_train: pd.Series
            Training target.
        results_path: str
            Path to save the cross-validation results.
        cv: int
            Number of cross-validation folds.

    Returns:
        pd.DataFrame: Cross-validation results with mean and standard deviation.
    """
    # Perform cross-validation
    cross_val_results = pd.DataFrame(
        cross_validate(pipeline, X_train, y_train, cv=cv, return_train_score=True)
    ).agg(['mean', 'std']).round(3).T

    # Save results to CSV
    cross_val_results.to_csv(results_path)

    return cross_val_results