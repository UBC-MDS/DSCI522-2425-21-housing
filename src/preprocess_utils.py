from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def create_preprocessor(categorical_features, numeric_features):
    """
    Creates a preprocessor with OneHotEncoder for categorical features
    and StandardScaler for numeric features.

    Parameters:
    - categorical_features (list): List of categorical feature names.
    - numeric_features (list): List of numeric feature names.

    Returns:
    - ColumnTransformer: Preprocessor object.
    """
    return make_column_transformer(
        (OneHotEncoder(), categorical_features),
        (StandardScaler(), numeric_features)
    )


def validate_categorical_levels(df, categorical_features, expected_values):
    """
    Validates that the categorical features have only expected levels.

    Parameters:
    - df (pd.DataFrame): Input dataframe.
    - categorical_features (list): List of categorical feature names.
    - expected_values (set): Expected set of values for each categorical feature.

    Returns:
    - dict: Dictionary with feature names as keys and unexpected values as values.
    """
    invalid_values = {}
    for feature in categorical_features:
        unique_values = set(df[feature].dropna().unique())
        unexpected_values = unique_values - expected_values
        if unexpected_values:
            invalid_values[feature] = unexpected_values
    return invalid_values
