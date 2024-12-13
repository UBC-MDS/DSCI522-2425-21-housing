# load_data.py
# author: Thamer Aldawood
# date: 2024-12-12

import pandas as pd
import click
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.load_data_util import load_csv

@click.command()
@click.option('--url', type=str, help="URL of dataset to be downloaded")
@click.option('--write-to', type=str, help="Path to directory where raw data will be written to")
@click.option('--filename', type=str, help="File name for csv to be created")

def main(url, write_to, filename):
    load_csv(url, write_to, filename)

if __name__ == '__main__':
    main()