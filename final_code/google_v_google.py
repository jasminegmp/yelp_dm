from matplotlib import pyplot as plt
import pandas as pd
import os

import numpy as np
from scipy.spatial.distance import euclidean

from fastdtw import fastdtw
from sklearn.preprocessing import MinMaxScaler

#for file1 in os.listdir():

name = raw_input("What is the name of the data you want to compare? ")

folder_name = name + "/"

bName_1 = "Google_" + name
#bName_2 = "Google_Puppy"

bName1_csv = bName_1 + ".csv"
#bName2_csv = bName_2 + ".csv"

comparisons = []

bData_1 = pd.read_csv(folder_name + bName1_csv)
for file in os.listdir(folder_name):
    if(file != bName1_csv and file.endswith(".csv")):
        bName2_csv = file
        bData_2 = pd.read_csv(folder_name + bName2_csv)

        # Create pandas data frame from csv
        df_1 = pd.DataFrame(bData_1, columns=['date', 'stars'])
        df_2 = pd.DataFrame(bData_2, columns=['date', 'stars'])

        # https://stackoverflow.com/questions/44128600/how-should-i-handle-duplicate-times-in-time-series-data-with-pandas

        # Data frame one for time series 1
        df_1['date'] = pd.to_datetime(df_1['date'], format='%m/%d/%Y')
        df_1['date'] = df_1['date'] + pd.to_timedelta(df_1.groupby('date').cumcount(), unit='d')
        df_1 = df_1.sort_values(by=['date'])
        new_df_1 = df_1.set_index('date')
        #new_df_1 = new_df_1.ix['1/1/2013':'5/1/2017']
        print new_df_1
        ts_1 = new_df_1#pd.Series.rolling(new_df_1['stars'], window=100).mean()
        ts_1 = ts_1.dropna()

        # Data frame two for time series 2
        df_2['date'] = pd.to_datetime(df_2['date'], format='%m/%d/%Y')
        df_2['date'] = df_2['date'] + pd.to_timedelta(df_2.groupby('date').cumcount(), unit='d')
        df_2 = df_2.sort_values(by=['date'])
        new_df_2 = df_2.set_index('date')
        #new_df_2 = new_df_2.ix['1/1/2013':'5/1/2017']
        # print new_df_2['stars']
        print new_df_2
        ts_2 = new_df_2#pd.Series.rolling(new_df_2['stars'], window=100).mean()
        ts_2 = ts_2.dropna()

        # Following is done because DTW requires same length time series
        compare_len = min(len(ts_1), len(ts_2))

        dist = np.linalg.norm(ts_1.iloc[-compare_len:].values - ts_2.iloc[-compare_len:].values)
        # print dist

        x = ts_1.iloc[-compare_len:].values
        y = ts_2.iloc[-compare_len:].values
        # print x
        # print y
        dtw_dist, path = fastdtw(x, y, dist=euclidean)
        comparisons.append([bName2_csv, dtw_dist])
output_name = folder_name + bName_1 + ".txt"
f = open(output_name, 'w')
f.write(str(comparisons))
f.close()
print comparisons