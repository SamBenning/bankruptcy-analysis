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

model = pickle.load(open(HERE / 'bankruptcy_model_new_random.sav', 'rb'))
X_test = pickle.load(open(HERE / 'model_test_X_data.sav', 'rb'))

print(X_test)