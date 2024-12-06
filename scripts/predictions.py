import pandas as pd
import pickle
import os
import click

@click.command()
@click.option('--model-file', type=str, help="Path to the trained model file (pickle format)", required=True)
@click.option('--output-file', type=str, help="Path to save the predictions CSV file", required=True)
def main(model_file, output_file):
    """
    Predicts housing prices for a given dataset using a pre-trained pipeline model.
    """
    # Input data
    ten_houses = {
        'meters': [174.23, 132.76, 90.82, 68.54, 221.30, 145.03, 102.96, 164.28, 142.79, 115.94],
        'garage': ['Y', 'Y', 'Y', 'N', 'Y', 'N', 'N', 'Y', 'N', 'Y'],
        'firepl': ['Y', 'N', 'N', 'N', 'Y', 'N', 'N', 'Y', 'Y', 'N'],
        'bsmt': ['Y', 'Y', 'N', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'Y'],
        'bdevl': ['N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'Y']
    }

    # Create a DataFrame from the input data
    X_predict = pd.DataFrame(ten_houses)

    # Load the trained pipeline
    with open(model_file, 'rb') as f:
        pipeline = pickle.load(f)

    # Perform predictions
    y_predict = pipeline.predict(X_predict)
    y_predict = pd.DataFrame(y_predict, columns=['Predicted_Values'])
    y_predict = round(y_predict, 2)

    # Combine input data with predictions
    predictions_df = pd.concat([X_predict, y_predict], axis=1)

    # Save the predictions to a CSV file
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    predictions_df.to_csv(output_file, index=False)

    print(f"Predictions saved to {output_file}")
    print(predictions_df)

if __name__ == '__main__':
    main()
