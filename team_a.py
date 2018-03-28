import numpy as np
import pandas as pd


# Load in the data from a CSV file that is comma seperated.
antelope_data = pd.read_csv('data_set.csv', sep=',', names=cols, header=None, encoding='latin-1')
