from matplotlib import pyplot as plt
import pandas as pd

print ""
print "DataMining Project (Bailey, Jasmine, Shirin)"
print "     Enter the name of .csv to plot:",

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
	ts = pd.Series.rolling(new_df['stars'], window=75).mean()
	#print ts
	ts.plot(style='b-', x_compat=True)

	f1 = plt.figure(1)
	plt.title(bName + " (Smoothing)")
	f1.show()


	# Scatter Plot
	f2 = plt.figure(2)
	ts.plot(style='bo', x_compat=True)
	plt.title(bName + " (Scatter, Smoothing)")
	f2.show()

	# This keeps plots alive
	raw_input()

