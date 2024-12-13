# load_data_util.py
# author: Thamer Aldawood
# date: 2024-12-05

import pandas as pd
import os

def load_csv(url, write_to, filename):
    """Downloads csv data from the web to a local filepath
    ----------------

    Example: load_csv(
    "https://hub.arcgis.com/api/v3/datasets/e3c5b04fccdc4ddd88059a8c0b6d8160_0/downloads/data?format=csv&spatialRefId=3776&where=1%3D1",
    "../data/raw",
    "Raw_2023_Property_Tax_Assessment.csv"
    )
    """
    try:
        housing_df = pd.read_csv(url)
        housing_df.to_csv(os.path.join(write_to, filename), index=False)
    except:
        os.makedirs(write_to)
        housing_df = pd.read_csv(url)
        housing_df.to_csv(os.path.join(write_to, filename), index=False)