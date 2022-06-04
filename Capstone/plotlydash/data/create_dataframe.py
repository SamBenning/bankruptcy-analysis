import pandas as pd
from pathlib import Path


HERE = Path(__file__).parent

class DataSet:

    def create_dataframe():
        df = pd.read_csv(str(HERE) + '/data.csv')
        return df