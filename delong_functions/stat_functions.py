import matplotlib as mpl
import matplotlib.pyplot as plt

def initialize_basic_figure(x, y, xtitle, ytitle, figure_title, title_size = 25, series_color = "black", 
	tick_range = 4, zero_range_flag = False):
    '''Function to save typing time by setting up a basic landscape-orientation figure
    using the seaborn-whitegrid aesthetic. 
    
    Parameters
    ==========

    x : one-dimensional
        x-axis variable
    y : one-dimensional
        y-axis variable
    xtitle : string
        x-axis label
    ytitle : string
        y-axis label
    figure_title : string
        Upper centered figure title
    title_size : int (optional) 
        size of title; default 25
    series_color : string (optional)
        color of line drawn; default "black"
    tick_range : integer (optional)
        spacing of x-axis ticks; default 4
    zero_range_flag : boolean
        if true, include zero as the lower y-axis limit    
    '''

    plt.style.use('seaborn-whitegrid')
    figure_size = plt.rcParams["figure.figsize"]
    figure_size[0] = 11
    figure_size[1] = 7
    plt.rcParams["figure.figsize"] = figure_size
    plt.plot(x, y, series_color)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    if zero_range_flag:
    	plt.ylim(0, )
    plt.title(figure_title, size = title_size)
    plt.xticks(np.arange(min(x), max(x)+1, tick_range))

    return plt.gcf()

    # Use; from delong_functions.stat_functions import initialize_basic_figure



# ----
#
# These are statistics functions for Brad DeLong's jupyter notebooks. Should exist 
# in two copies, one each inside the delong_functions directories of Brad DeLong's
# private jupyter notebook backup github repository and of Brad DeLong's public
# weblog-support github repository.
#
# Use: from delong_functions.stat_functions import *