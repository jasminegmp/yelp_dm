import csv
from matplotlib import pyplot as plt
import pandas as pd

print ""
print "DataMining Project (Bailey, Jasmine, Shirin)"
print "     Enter the name of .csv to plot:",

# Read in csv file for Pandas
bName = raw_input();
bName = bName + ".csv"
#bName = "KFC.csv"
bData = pd.read_csv(bName)

# Create pandas data frame from csv
df = pd.DataFrame(bData, columns = ['id', 'date', 'stars', 'text'])

# Prep to plot time series
# Convert date time
# Read this Stack Overflow for converting date into index for plotting
# https://stackoverflow.com/questions/25416955/plot-pandas-dates-in-matplotlib
date =  pd.to_datetime(df['date'], format='%Y-%m-%d')
df.set_index(date,inplace=True)

# Was using this to debug
#for line in df.index:
#    print line

# Time series
ts = pd.Series(df['stars'], index = df.index) 
f1 = plt.figure(1)
ts.plot()
f1.show()

# Scatter Plot
f2 = plt.figure(2)
plt.scatter(df.index, df.stars)
f2.show()

# This keeps plots alive
raw_input()

