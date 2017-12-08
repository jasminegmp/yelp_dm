from matplotlib import pyplot as plt
import pandas as pd
import math
import numpy as np

# had to download this https://pypi.python.org/pypi/fastdtw
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

print ""
print "DataMining Project (Bailey, Jasmine, Shirin)\n"
#print "     Enter the name of .csv to plot:",

def star_plotter(bName):

	# Read in csv file for Pandas
	#bName = raw_input();
	bName_csv = bName + ".csv"
	#bName = "healthy.csv"
	bData = pd.read_csv(bName_csv)

	# Create pandas data frame from csv
	df = pd.DataFrame(bData, columns = ['id', 'date', 'stars', 'text'])

	# Prep to plot time series
	# Convert date time
	# Read this Stack Overflow for converting date into index for plotting
	# https://stackoverflow.com/questions/25416955/plot-pandas-dates-in-matplotlib
	#date =  pd.to_datetime(df['date'], format='%Y-%m-%d')
	#date =  date.sort_values()
	#df.set_index(date,inplace=True)
	# at this point date is sorted in date
	#print df.date[1]

	# https://stackoverflow.com/questions/44128600/how-should-i-handle-duplicate-times-in-time-series-data-with-pandas

	df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
	df['date'] = df['date'] + pd.to_timedelta(df.groupby('date').cumcount(), unit='h')

	df =  df.sort_values(by=['date'])
	new_df = df.set_index('date')
	#print df.ix
	new_df = new_df.ix['2012-6-1':'2017-5-1']
	print new_df
	# Time series
	#ts=pd.Series(new_df['stars'])
	ts = pd.Series.rolling(new_df['stars'], window=100).mean()
	#print ts
	ts.plot(style='b-', x_compat=True)

	f1 = plt.figure()
	plt.title(bName + " (Smoothing)")
	f1.show()
	plt.savefig(bName+"1.png")

	# Scatter Plot
	f2 = plt.figure()
	ts.plot(style='bo', x_compat=True)
	plt.title(bName + "(Scatter, Smoothing)")
	f2.show()
	plt.savefig(bName+"2.png")
	# This keeps plots alive
	#raw_input()

def pattern_finder(bName_1, bName_2):

	bName1_csv = bName_1 + ".csv"
	bName2_csv = bName_2 + ".csv"

	bData_1 = pd.read_csv(bName1_csv)
	bData_2 = pd.read_csv(bName2_csv)

	# Create pandas data frame from csv
	df_1 = pd.DataFrame(bData_1, columns = ['id', 'date', 'stars', 'text'])
	df_2 = pd.DataFrame(bData_2, columns = ['id', 'date', 'stars', 'text'])

	# https://stackoverflow.com/questions/44128600/how-should-i-handle-duplicate-times-in-time-series-data-with-pandas

	# Data frame one for time series 1
	df_1['date'] = pd.to_datetime(df_1['date'], format='%Y-%m-%d')
	df_1['date'] = df_1['date'] + pd.to_timedelta(df_1.groupby('date').cumcount(), unit='h')
	df_1 =  df_1.sort_values(by=['date'])
	new_df_1 = df_1.set_index('date')
	new_df_1 = new_df_1.ix['2012-6-1':'2017-5-1']
	#print new_df_1
	ts_1 = pd.Series.rolling(new_df_1['stars'], window=100).mean()
	ts_1 = ts_1.dropna()

	# Data frame two for time series 2
	df_2['date'] = pd.to_datetime(df_2['date'], format='%Y-%m-%d')
	df_2['date'] = df_2['date'] + pd.to_timedelta(df_2.groupby('date').cumcount(), unit='h')
	df_2 =  df_2.sort_values(by=['date'])
	new_df_2 = df_2.set_index('date')
	new_df_2 = new_df_2.ix['2012-6-1':'2017-5-1']
	#print new_df_2['stars']
	#print new_df_2

	ts_2 = pd.Series.rolling(new_df_2['stars'], window=100).mean()
	ts_2 = ts_2.dropna()

	# Following is done because DTW requires same length time series
	compare_len = min(len(ts_1),len(ts_2))

	dist = np.linalg.norm(ts_1.iloc[-compare_len:].values-ts_2.iloc[-compare_len:].values)
	#print dist

	x = ts_1.iloc[-compare_len:].values
	y = ts_2.iloc[-compare_len:].values
	#print x
	#print y
	dtw_dist, path = fastdtw(x,y, dist=euclidean)
	print dtw_dist
	return dtw_dist








