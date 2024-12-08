import pandas as pd
import pickle
import os
import altair as alt
import click

@click.command()
@click.option('--model-file', type=str, help="Path to the trained model file (pickle format)", required=True)
@click.option('--output-file', type=str, help="Path to save the predictions CSV file", required=True)
@click.option('--plot-to', type=str, help="Path to save the visualization", required=True)
def main(model_file, output_file, plot_to):
    """
    Predicts housing prices for a given dataset using a pre-trained pipeline model
    and saves visualizations of predictions.
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

    # Generate visualizations
    mtrs = alt.Chart(predictions_df).mark_line().encode(
        x=alt.X('meters', title="Property size"),
        y=alt.Y('Predicted_Values', title='Predicted Values'),
    ).properties(
        height=200,
        width=200,
        title="Property size (m^2) vs value"
    )

    grg2 = alt.Chart(predictions_df).mark_line().encode(
        x=alt.X('meters', title="Property size"),
        y=alt.Y('Predicted_Values', title='Predicted Values'),
        color=alt.Color('garage', title="Garage")
    ).properties(
        height=200,
        width=200,
        title="Garage"
    )

    frp2 = alt.Chart(predictions_df).mark_line().encode(
        x=alt.X('meters', title="Property size"),
        y=alt.Y('Predicted_Values', title='Predicted Values'),
        color=alt.Color('firepl', title="Fireplace")
    ).properties(
        height=200,
        width=200,
        title="Fireplace"
    )

    bst2 = alt.Chart(predictions_df).mark_line().encode(
        x=alt.X('meters', title="Property size"),
        y=alt.Y('Predicted_Values', title='Predicted Values'),
        color=alt.Color('bsmt', title="Basement")
    ).properties(
        height=200,
        width=200,
        title="Basement"
    )

    bdl2 = alt.Chart(predictions_df).mark_line().encode(
        x=alt.X('meters', title="Property size"),
        y=alt.Y('Predicted_Values', title='Predicted Values'),
        color=alt.Color('bdevl', title="Building evaluation")
    ).properties(
        height=200,
        width=200,
        title="Building evaluation"
    )

    combined_chart = (mtrs & (grg2 | frp2) & (bst2 | bdl2)).properties(
        title="Correlations between property size and house value, colored by different characteristics"
    )

    # Save the plot
    plot_dir = os.path.dirname(plot_to)
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    combined_chart.save(plot_to, scale_factor=2.0)
    print(f"Visualization saved to {plot_to}")

if __name__ == '__main__':
    main()
