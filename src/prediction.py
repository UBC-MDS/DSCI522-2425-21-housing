# src/prediction.py
import pandas as pd
import pickle

def make_predictions(model_file, input_data):
    """
    Function to make predictions using a pre-trained model and input data.
    
    Args:
    - model_file (str): Path to the trained model (pickle format).
    - input_data (dict): Dictionary with the input features for prediction.
    
    Returns:
    - pd.DataFrame: DataFrame with predicted values.
    """
    # Create a DataFrame from the input data
    X_predict = pd.DataFrame(input_data)

    # Load the trained pipeline model
    with open(model_file, 'rb') as f:
        pipeline = pickle.load(f)

    # Perform predictions
    y_predict = pipeline.predict(X_predict)
    y_predict = pd.DataFrame(y_predict, columns=['Predicted_Values'])
    y_predict = round(y_predict, 2)

    # Combine input data with predictions
    predictions_df = pd.concat([X_predict, y_predict], axis=1)
    
    return predictions_df
