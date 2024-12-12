import click
import os
import pandas as pd
from src.eda_utils import create_combined_bar_chart

@click.command()
@click.option('--processed-data', type=str, help="Path to processed data file", required=True)
@click.option('--plot-to', type=str, help="Path to directory where the plots will be saved", required=True)
def main(processed_data, plot_to):
    """
    Generates a combined bar chart for categorical features in the housing dataset 
    and saves the plot to a specified location.

    Parameters:
    ----------
    processed_data : str
        Path to the processed data CSV file.
    plot_to : str
        Path to the directory where the plot will be saved.
    """
    # Load the processed data
    housing_df = pd.read_csv(processed_data)

    # Define the y-axis domain and chart title
    domain = [0, 35000]
    chart_title = "Counts of Categorical Features"

    # Generate the combined bar chart
    combined_chart = create_combined_bar_chart(housing_df, domain, chart_title)

    # Ensure output directory exists
    os.makedirs(plot_to, exist_ok=True)

    # Save the chart
    output_path = os.path.join(plot_to, "combined_bar_chart.png")
    combined_chart.save(output_path, scale_factor=2.0)
    print(f"Combined bar chart saved to {output_path}")

if __name__ == '__main__':
    main()
