from datetime import datetime
from bs4 import BeautifulSoup as soup
import json
import csv
import dicttoxml
from matplotlib import pyplot as plt

def create_category_csv(gen_category, categories):
	min_reviews = 1000
	idList=[];
	name = [];
	#print "         searching for ids related to "+ gen_category 
	c=0
	#print categories
	for cat in categories:
		with open('business.csv') as bfile:
			reader = csv.reader(bfile);
			for row in reader:
				#print cat
				if (cat in row[2]):
					idList.append(row[0])
					name.append(row[1])

	if len(name) > min_reviews:
		print "         " + gen_category + " " + str(len(name)) + " matches found"
		csvFile=csv.writer(open(gen_category+".csv","wb+"));
		csvFile.writerow(["name", "id", "date", "stars","text"]);

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
		return 1
	else:
		return 0


def create_csv_company(bName):
	csvFile=csv.writer(open(bName+".csv","wb+"));
	csvFile.writerow(["name", "id", "date", "stars","text"]);

	idList=[];
	name = [];
	print "         searching for ids related to that name ... ",
	c=0
	with open('business.csv') as bfile:
	    reader = csv.reader(bfile);
	    for row in reader:
	    	#print row[1]
	        if row[1]==bName:
	            idList.append(row[0])
	            name.append(row[1])
	            c+=1
	print c,"ids found."

	dates=[]
	stars=[]
	count=0
	with open('reviews.csv') as rfile:
	    rreader=csv.reader(rfile)
	    for rrow in rreader:
	        #print rrow[0]
	        if rrow[0] in idList:
				if count < len(name):
					csvFile.writerow([name[count], rrow[0],rrow[1],rrow[2],rrow[3]]);
					dates.append(rrow[1]);
					stars.append(rrow[2]);
					count+=1
				else:
					break












