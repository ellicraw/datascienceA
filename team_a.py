from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def make_scatter_plot(dataframe, x_axis, y_axis):
  #Creates a scatter plot of x_axis vs y_axis along with model names.
  x_label = ""
  y_label = ""
  if (x_axis == "X1"):
      x_label = "spring fawn count/100"
  elif (x_axis == "X2"):
      x_label = "size of adult antelope population/100"
  elif (x_axis == "X3"):
      x_label = "annual precipitation"
  else:
      x_label = "winter severity index"

  if (y_axis == "X1"):
      y_label = "spring fawn count/100"
  elif (y_axis == "X2"):
      y_label = "size of adult antelope population/100"
  elif (y_axis == "X3"):
      y_label = "annual precipitation"
  else:
      y_label = "winter severity index"

  # Generate the scatter plot
  chart_label = x_label + " vs. " + y_label
  print(chart_label)
  x = dataframe[x_axis]
  y = dataframe[y_axis]
  plt.ylabel(y_axis)
  plt.xlabel(x_axis)
  plt.scatter(x, y, color='black', label=chart_label)

  # calc the trendline (it is simply a linear fitting)
  z = np.polyfit(x, y, 1)
  p = np.poly1d(z)
  plt.plot(x, p(x))
  # the line equation:
  print( "y=%.6fx+(%.6f)"%(z[0],z[1]) )

def make_histogram(param1, param2, param3, param4):
  plt.figure(figsize=(20, 5))
  plt.subplot(1, 4, 1)
  plt.title(param1)
  histogram = antelope_dataframe[param1].hist(bins=50)

  plt.subplot(1, 4, 2)
  plt.title(param2)
  histogram = antelope_dataframe[param2].hist(bins=50)

  plt.subplot(1, 4, 3)
  plt.title(param3)
  histogram = antelope_dataframe[param3].hist(bins=50)

  plt.subplot(1, 4, 4)
  plt.title(param4)
  histogram = antelope_dataframe[param4].hist(bins=50)

def make_cumulative_trend_plot():
  print("nothing yet")

# Load in the data from a CSV file that is comma seperated.
antelope_dataframe = pd.read_csv('data_set.csv', sep=',')
antelope_dataframe.describe()
make_scatter_plot(antelope_dataframe, "X1", "X4")
make_histogram("X1", "X2", "X3", "X4")
#make_cumulative_trend_plot()

plt.show()
