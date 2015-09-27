def setup():
	import numpy as np
	import matplotlib.pyplot as plt
	import seaborn as sns
	import pandas as pd
	import scipy as sp
	from IPython.display import set_matplotlib_formats
	set_matplotlib_formats
	set_matplotlib_formats('svg')
  plt.rcParams['figure.figsize'] = (8, 6)
  plt.rcParams['font.size'] = 13
  plt.rcParams['font.family'] = 'Source Sans Pro'
  plt.rcParams['axes.labelsize'] = 1.1*plt.rcParams['font.size']
  plt.rcParams['axes.titlesize'] = 1.1*plt.rcParams['font.size']
  plt.rcParams['legend.fontsize'] = plt.rcParams['font.size']
  plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
  plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']

