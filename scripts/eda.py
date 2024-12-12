# eda.py
import click
import os
import pandas as pd
from src.eda_utils import create_combined_bar_chart

@click.command()
@click.option('--processed-data', type=str, help="Path to processed data file")
@click.option('--plot-to', type=str, help="Path to directory where the plots will be saved")
def main(processed_data, plot_to):
    """
    Creates combined bar charts for categorical features
    and saves the plot as a file.
    """
    # Load the processed data
    housing_df = pd.read_csv(processed_data)

    # Generate the combined bar chart
    combined_chart = create_combined_bar_chart(
        df=housing_df,
        chart_title="Counts of categorical features"
    )

    # Save the combined plot
    output_file = os.path.join(plot_to, "categorical_features_combined_chart.png")
    combined_chart.save(output_file, scale_factor=2.0)
    print(f"Combined bar chart saved to {output_file}")

if __name__ == '__main__':
    main()

