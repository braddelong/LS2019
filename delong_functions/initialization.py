# set up the environment by reading in libraries: 
# os... graphics... data manipulation... time... math... statistics...

import sys
import os
from urllib.request import urlretrieve

import matplotlib as mpl
import matplotlib.pyplot as plt
import PIL as pil
from IPython.display import Image

import pandas as pd
from pandas import DataFrame, Series
import pandas_datareader
from datetime import datetime

import scipy as sp
import numpy as np
import math
import random

import seaborn as sns
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf

# graphics setup: seaborn-darkgrid and figure size...

plt.style.use('seaborn-darkgrid')

figure_size = plt.rcParams["figure.figsize"]
figure_size[0] = 7
figure_size[1] = 7
plt.rcParams["figure.figsize"] = figure_size

# import delong functions

from delong_functions.data_functions import getdata_read_or_download # get or download data file
from delong_functions.stat_functions import initialize_basic_figure  # initialize graphics
from delong_functions.data_functions import data_FREDseries          # construct a useful dict with source
                                                                     # and notes info from a previously 
                                                                     # downloaded FRED csv file
# check to see if functions successfully created... 
# NOW COMMENTED OUT: getdata_read_or_download? initialize_basic_figure?