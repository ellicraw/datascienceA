import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats, integrate
import statsmodels.api as sm

def make_linear_regression_plot(dataframe):
  x = dataframe['X1']
  y = dataframe['X4']

  fit = np.polyfit(x, y, 1)
  fit_fn = np.poly1d(fit)

  plt.plot(x, y, 'yo', x, fit_fn(x), '--k')
  plt.xlim(0, 5)
  plt.ylim(0, 12)
  plt.show()


def make_multiple_linear_regression_ploy(dataframe):
  X = dataframe[['X1', 'X2', 'X3']]  # chose three variables (one of which is a dummy variable)
  y = dataframe[['X4']]

  model = sm.OLS(y, X).fit()
  predictions = model.predict(X)
  plt.scatter(predictions, y, s=30, c='r', marker='+', zorder=10)
  plt.xlabel("Antelope Data")
  plt.ylabel("Predictions")
  plt.show()


# Load in the data from a CSV file that is comma seperated.
antelope_dataframe = pd.read_excel('mlr01.xls')
antelope_dataframe.describe()
# make_linear_regression_plot(antelope_dataframe)
make_multiple_linear_regression_ploy(antelope_dataframe)

plt.show()
