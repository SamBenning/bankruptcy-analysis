import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path
import pickle
import requests
import json
import sys

np.set_printoptions(threshold=sys.maxsize)

HERE = Path(__file__).parent

X_test = pickle.load(open(HERE / 'model_test_X_data.sav', 'rb'))

class Model:
    def __init__(self, input_values):
        self.input_values = input_values

        
        model = pickle.load(open(HERE / 'RF_model.sav', 'rb'))

        self.model = model

    def predict(self):
        size = len(self.input_values)
        reshaped = self.input_values.reshape(1,size)
        print(reshaped)
        print(size)
        return self.model.predict(reshaped)