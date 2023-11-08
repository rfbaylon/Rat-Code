# formatting
import pandas as pd
import numpy as np
import os

# visualizers
import matplotlib.pyplot as plt 
import seaborn as sns

import os

'''
Todo List
==========
[x] Read in data
[] Clean data
[] Create buffer area for proxies
[] Count 311s within buffers
[] Statistical Analysis
[] Make vis mapping all proxies and 311s per year
[] Make reg prlot for each  proxy per year
[] clean up the code
'''

def read_data(file_name):
    '''
    Given a file name, reads the corresponding CSV file from the "Sources" directory and returns a Pandas DataFrame.
    '''
    main_path = os.path.dirname(__file__)
    file_path = os.path.join(main_path, f'Sources/{file_name}')
    df = pd.read_csv(file_path)
    return df

        
def main():
    CATCH_DATA = read_data("Somerville Catch Data simple.csv")
    BIG_BELLY_LOCATIONS = read_data("Big Belly Locations 2021.csv")
    BURROW_TICKETING = read_data("Burrow Ticketing 2023.csv")
    COMMON_TRASH_TICKETS = read_data("Comm Trash Tickets 2023.csv")
    HEATMAP = read_data("Commonwealth_Connect_Service_Requests_-_Rodent_Sightings_Heat_Map.csv")
    RAP_REQ = read_data("RAP Requests 2015-2023.csv")
    TRASH_VIOLATIONS = read_data("Res Trash Violations 2023.csv")
    RAT_CALLS = read_data("2023 Rat Calls.csv")

    print(RAT_CALLS)

if __name__ == "__main__":
    main()