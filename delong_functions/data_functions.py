import pandas_datareader
from pandas import DataFrame, Series
import pandas as pd
import os
from urllib.request import urlretrieve

def data_FREDseries(seriesName, sourceURL,
    sourceDescription = "You need to add a source description", 
    sourceNotes = "You need to add source notes"):
    '''
    Use pandas to read in a data series previously downloaded as a csv
    file from FRED: http://fred.stlouisfed.org. 
    
    Parameters:
    ===========
    
    seriesName : string
        what the variable is called in the pandas dataframe to be created
    sourceURL : string
        location of downloaded FRED csv data on internet
    sourceDescription (optional): string
        please include for the sake of the relevant loser who will be trying
        to use this code in six months—that is, for the sake of your future self
    sourceNotes (optional): string
        please include for the sake of the relevant loser who will be trying
        to use this code in six months—that is, for the sake of your future self
       
    Returns:
    ========
    
    data_dict : pandas dictionary
        the actual series is then addressed as a series within the 
        dataframe: data_dict["df"] 
    '''
    
    data_df = pd.read_csv(sourceURL, parse_dates = True, index_col = "DATE")
    data_df.rename(columns = {data_df.columns[0]: seriesName}, inplace = True)
    data_dict = {}
    data_dict["sourceURL"] = sourceURL
    data_dict["sourceDescription"] = sourceDescription
    data_dict["sourceNotes"] = sourceNotes
    data_dict["df"] = data_df
    
    return data_dict

def getdata_read_or_download(filename, source_URL, force_download = False):
    '''Use pandas to read in data from a specified local file in the current
    working directory, or download data from a specified source URL if the 
    local file does not exist in the current working directory. Download
    can be forced if the local file is corrupt or simply needs to be updated.
    
    Parameters:
    ===========
    filename : string                  # location of already-dowloaded data in current working directory
    source_URL : string                # location of data on internet
    force_download: boolean (optional) # if True, force redownload of data
        
    Returns:
    ========
    datafame : pandas dataframe        # the data file for the analysis'''
    
    if ((force_download == True) or not os.path.exists(filename)):
        urlretrieve(source_URL,filename)
    dataframe = pd.read_csv(filename)
    return dataframe

    # Use: from delong_functions.data_functions import getdata_read_or_download # get or download data file

# ----
#
# These are statistics functions for Brad DeLong's jupyter notebooks. Should exist 
# in two copies, one each inside the delong_functions directories of Brad DeLong's
# private jupyter notebook backup github repository and of Brad DeLong's public
# weblog-support github repository.
#
# Use: from delong_functions.stat_functions import *


