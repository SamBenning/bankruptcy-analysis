import pandas as pd
from pathlib import Path
from dash import dcc


HERE = Path(__file__).parent

def create_dataframe(filename):
    path_string = str(HERE) + '/' + filename
    df = pd.read_csv(path_string, index_col=0)
    return df


class Figures:

    def __init__(self):
        self.df = create_dataframe('data.csv')
        self.df_test = create_dataframe('test_data_with_preds.csv')

    def create_grouped_bar(self):
        my_df = self.df


