from datetime import datetime
from bs4 import BeautifulSoup as soup
import json
import csv
import dicttoxml
from matplotlib import pyplot as plt


############################################
gen_category = "Drinks"
#categories = "Breweries"
categories = ["Wineries", "Breweries"]

############################################
############################################

csvFile=csv.writer(open(gen_category+".csv","wb+"));
csvFile.writerow(["name", "id", "date", "stars","text"]);

idList=[];
name = [];
print "         searching for ids related to that category ... ",
c=0

for cat in categories:
	with open('business.csv') as bfile:
		reader = csv.reader(bfile);
		for row in reader:
			#print cat
			if cat in row[2]:
				idList.append(row[0])
				name.append(row[1])

print len(name), "matches found"
print name
############################################
############################################

dates=[]
stars=[]
count=0

with open('reviews.csv') as rfile:
    rreader=csv.reader(rfile)
    for rrow in rreader:
    	#print rrow
        if rrow[0] in idList:
			if count < len(name):
				csvFile.writerow([name[count], rrow[0],rrow[1],rrow[2],rrow[3]]);
				dates.append(rrow[1]);
				stars.append(rrow[2]);
				count+=1
			else:
				break














