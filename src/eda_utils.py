import altair as alt

def create_combined_bar_chart(df, chart_title):
    """
    Creates a combined bar chart for categorical features in the dataframe.

    Parameters:
        df (pd.DataFrame): The dataframe containing the categorical data.
        chart_title (str): The title for the combined chart.

    Returns:
        alt.Chart: The combined Altair bar chart.
    """
    grg0 = alt.Chart(df).mark_bar().encode(
        x=alt.X('garage', title='Garage'),
        y=alt.Y('count()', title='House value')
    )

    frp0 = alt.Chart(df).mark_bar().encode(
        x=alt.X('firepl', title='Fireplace'),
        y=alt.Y('count()', title='House value')
    )

    bst0 = alt.Chart(df).mark_bar().encode(
        x=alt.X('bsmt', title='Basement'),
        y=alt.Y('count()', title='House value')
    )

    bdl0 = alt.Chart(df).mark_bar().encode(
        x=alt.X('bdevl', title='Building evaluation'),
        y=alt.Y('count()', title='House value')
    )

    combined_chart = alt.vconcat(grg0, frp0, bst0, bdl0).properties(
        title=chart_title
    )

    return combined_chart
