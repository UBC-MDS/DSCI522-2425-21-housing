import sys
import os
import pandas as pd
import altair as alt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.eda_utils import create_combined_bar_chart

def test_create_combined_bar_chart():
    # Test Data
    df = pd.DataFrame({
        'garage': ['Y', 'N', 'Y', 'N', 'Y'],
        'firepl': ['Y', 'N', 'N', 'Y', 'Y'],
        'bsmt': ['Y', 'Y', 'N', 'N', 'Y'],
        'bdevl': ['N', 'Y', 'N', 'Y', 'N']
    })

    # Generate Combined Chart
    combined_chart = create_combined_bar_chart(
        df,
        chart_title="Counts of categorical features"
    )

    # Check the combined chart title
    assert combined_chart.title == "Counts of categorical features", "Combined chart should have the correct title."

    # Check the number of subplots
    assert len(combined_chart.hconcat) == 4, "Combined chart should contain 4 subplots."

    # Test the first subplot (e.g., 'garage')
    first_chart = combined_chart.hconcat[0]
    assert first_chart.encoding.x.shorthand == 'garage', "First chart x-axis should be mapped to 'garage'."

    # Test the second subplot (e.g., 'firepl')
    second_chart = combined_chart.hconcat[1]
    assert second_chart.encoding.x.shorthand == 'firepl', "Second chart x-axis should be mapped to 'firepl'."
