import pytest
import pandas as pd

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.load_data import load_csv

# load_csv should use pandas to read a CSV from a url then save the raw csv to a given path with a given filename

def test_load_csv():
    # Example csv url for testing purposes
    url = "https://gist.githubusercontent.com/dsternlicht/74020ebfdd91a686d71e785a79b318d4/raw/d3104389ba98a8605f8e641871b9ce71eff73f7e/chartsninja-data-1.csv"
    expected = pd.read_csv(url)
    write_to = "../data/raw"
    filename = "test_data.csv"

    # Running load_csv to let it write the csv from the url
    load_csv(url, write_to, filename)
    actual = pd.read_csv(os.path.join(write_to, filename))

    assert actual.equals(expected), "CSV file is not being loaded properly"