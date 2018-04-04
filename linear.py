
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

def make_linear_regression_plot(dataframe, x, y):
  x = dataframe[x]
  y = dataframe[y]

  fit = np.polyfit(x, y, 1)
  fit_fn = np.poly1d(fit)

  plt.plot(x, y, 'yo', x, fit_fn(x), '--k')
  plt.xlim(0, 5)
  plt.ylim(0, 12)
  plt.show()


antelope_dataframe = pd.read_excel('mlr01.xls')
antelope_dataframe.describe()
make_linear_regression_plot(antelope_dataframe, "X1", "X4")

plt.show()
