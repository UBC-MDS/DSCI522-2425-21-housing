# Download and extract data

# download_data.py
# author: Thamer Aldawood
# date: 2024-12-05

import pandas as pd
import click
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--url', type=str, help="URL of dataset to be downloaded")
@click.option('--write-to', type=str, help="Path to directory where raw data will be written to")

def main(url, write_to):
    """Downloads csv data from the web to a local filepath
    ----------------

    Example: main("https://hub.arcgis.com/api/v3/datasets/e3c5b04fccdc4ddd88059a8c0b6d8160_0/downloads/data?format=csv&spatialRefId=3776&where=1%3D1",
    "../data/")
    """

    try:
        housing_df = pd.read_csv(url)
        housing_df.to_csv(os.path.join(write_to, "Raw_2023_Property_Tax_Assessment.csv"), index=False)
    except:
        os.makedirs(write_to)
        housing_df = pd.read_csv(url)
        housing_df.to_csv(os.path.join(write_to, "Raw_2023_Property_Tax_Assessment.csv"), index=False)

if __name__ == '__main__':
    main()