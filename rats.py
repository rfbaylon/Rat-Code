# formatting
from pandasgui import show
import pandas as pd
import numpy as np
import os

# visualizers
import matplotlib.pyplot as plt 
import seaborn as sns


'''
Todo List
==========
[] Read in data
[] Clean data
[] Create buffer area for proxies
[] Count 311s within buffers
[] Statistical Analysis
[] Make vis mapping all proxies and 311s per year
[] Make reg prlot for each  proxy per year
[] clean up the code
'''

RYAN = "C://Desktop//Code//ds2500//RatCode//Rat-Code//Sources"

def read_data():
    
    main_path = os.path.dirname(__file__)
    file_path = os.path.join(main_path, 'Sources')
    f = open(file_path)
    for i in f:
        print(i)
    # df = pd.read_csv(f)
    # print(df)
 

    return

def read_data():
    import glob
    main_path = os.path.dirname(__file__)
    file_path = os.path.join(main_path, 'Sources\*.csv')
    
    for fname in glob.glob(file_path):
        print(fname)

def main():
    # read_data("2023 Rat Calls.csv")
    # read_data()
    test()
    return

if __name__ == "__main__":
    main()