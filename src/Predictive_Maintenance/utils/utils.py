import pandas as pd
import os
from Predictive_Maintenance import logger

# creating type of failure column
def type_of_failure(row_name,df):
    if df.loc[row_name, 'TWF'] == 1:
        df.loc[row_name, 'type_of_failure'] = 'TWF'
    elif df.loc[row_name, 'HDF'] == 1:
        df.loc[row_name, 'type_of_failure'] = 'HDF'
    elif df.loc[row_name, 'PWF'] == 1:
        df.loc[row_name, 'type_of_failure'] = 'PWF'
    elif df.loc[row_name, 'OSF'] == 1:
        df.loc[row_name, 'type_of_failure'] = 'OSF'
    elif df.loc[row_name, 'RNF'] == 1:
        df.loc[row_name, 'type_of_failure'] = 'RNF'
    else:
        df.loc[row_name, 'type_of_failure'] = 'no failure'
    

def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")