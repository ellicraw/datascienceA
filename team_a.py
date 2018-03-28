from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def make_scatter_plot(dataframe, x_axis, y_axis):
  #Creates a scatter plot of x_axis vs y_axis along with model names.

  # Generate the scatter plot
  x = dataframe[x_axis]
  y = dataframe[y_axis]
  plt.ylabel(y_axis)
  plt.xlabel(x_axis)
  plt.scatter(x, y, color='black', label="")

def make_histogram(param):
  plt.figure(figsize=(20, 5))
  plt.subplot(1, 3, 1)
  plt.title(param)
  histogram = antelope_dataframe[param].hist(bins=50)

def make_cumulative_trend_plot():
  print("nothing yet")

# Load in the data from a CSV file that is comma seperated.
antelope_dataframe = pd.read_csv('data_set.csv', sep=',')
antelope_dataframe.describe()
print('Spring Fawn Count vs Winter Severity')
make_scatter_plot(antelope_dataframe, 'X1', 'X4')
make_histogram("X1")
make_cumulative_trend_plot()
plt.show()
