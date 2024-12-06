import click
import os
import altair as alt
import pandas as pd

@click.command()
@click.option('--processed-data', type=str, help="Path to processed data file")
@click.option('--plot-to', type=str, help="Path to directory where the plots will be saved")
def main(processed_data, plot_to):
    """
    Creates bar charts, scatter plots, and distribution plots for categorical features 
    and saves the combined plots as separate files.
    """
    # Load the processed data
    housing_df = pd.read_csv(processed_data)
    
    # Create bar charts for categorical features
    grg0 = alt.Chart(housing_df).mark_bar().encode(
        x=alt.X('garage', title='Garage'),
        y=alt.Y('count()', scale=alt.Scale(domain=[0, 35000]), title='House value'),
    )

    frp0 = alt.Chart(housing_df).mark_bar().encode(
        x=alt.X('firepl', title='Fireplace'),
        y=alt.Y('count()', scale=alt.Scale(domain=[0, 35000]), title='House value'),
    )

    bst0 = alt.Chart(housing_df).mark_bar().encode(
        x=alt.X('bsmt', title='Basement'),
        y=alt.Y('count()', scale=alt.Scale(domain=[0, 35000]), title='House value'),
    )

    bdl0 = alt.Chart(housing_df).mark_bar().encode(
        x=alt.X('bdevl', title='Building evaluation'),
        y=alt.Y('count()', scale=alt.Scale(domain=[0, 35000]), title='House value'),
    )

    bar_chart_combined = (grg0 | frp0 | bst0 | bdl0).properties(
        title="Counts of Categorical Features"
    )
    
    # Create scatter plots for house value assessment per categorical feature
    grg = alt.Chart(housing_df).mark_point().encode(
        x=alt.X('garage', title='Garage'),
        y=alt.Y('assess_2022', title='House value'),
    )

    frp = alt.Chart(housing_df).mark_point().encode(
        x=alt.X('firepl', title='Fireplace'),
        y=alt.Y('assess_2022', title='House value'),
    )

    bst = alt.Chart(housing_df).mark_point().encode(
        x=alt.X('bsmt', title='Basement'),
        y=alt.Y('assess_2022', title='House value'),
    )

    bdl = alt.Chart(housing_df).mark_point().encode(
        x=alt.X('bdevl', title='Building evaluation'),
        y=alt.Y('assess_2022', title='House value'),
    )

    scatter_chart_combined = (grg | frp | bst | bdl).properties(
        title="House Value Assessment per Categorical Feature"
    )

    # Create a scatter plot for property size vs. assessment values
    scatter = alt.Chart(housing_df).mark_point().encode(
        y=alt.Y('meters', title="Property size (meters)"),
        x=alt.X('assess_2022', title="Assessment Value"),
        color=alt.Color('meters', title="Property size (meters)", scale=alt.Scale(scheme='viridis'))
    ).properties(
        title="Scatter Plot of Property Size and Assessment Values (2022)"
    )

    # Create a histogram and KDE plot for the 'assess_2022' column
    histogram = alt.Chart(housing_df).mark_bar().encode(
        alt.X("assess_2022:Q", bin=alt.Bin(maxbins=2000), title="Assessment Value").scale(domain=(0, 2000000), clamp=True),
        alt.Y("count():Q", title="Frequency"),
    ).properties(
        title="Distribution of House Assessment Values (2022)"
    )

    kde = alt.Chart(housing_df).transform_density(
        "assess_2022",
        as_=["assess_2022", "density"], 
        counts=True
    ).mark_line(color="red").encode(
        alt.X("assess_2022:Q", title="Assessment Value").scale(domain=(0, 2000000), clamp=True),
        alt.Y("density:Q", title="Density")
    ).properties(
        title="Line Plot of KDE House Assessment Values (2022)"
    )

    # Combine the histogram, KDE plot, and scatter plot
    combined_chart = histogram | kde | scatter

    # Save the plots
    bar_chart_file = os.path.join(plot_to, "categorical_features_counts.png")
    scatter_chart_file = os.path.join(plot_to, "categorical_features_scatter.png")
    distribution_chart_file = os.path.join(plot_to, "distribution_charts.png")

    bar_chart_combined.save(bar_chart_file, scale_factor=2.0)
    scatter_chart_combined.save(scatter_chart_file, scale_factor=2.0)
    combined_chart.save(distribution_chart_file, scale_factor=2.0)

if __name__ == '__main__':
    main()
