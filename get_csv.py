from datetime import datetime
from bs4 import BeautifulSoup as soup
import json
import csv
import dicttoxml
from matplotlib import pyplot as plt



############################################
############################################
def create_csv(gen_category, categories):


	idList=[];
	name = [];
	print "         searching for ids related to that category ... \n",
	c=0
	print categories
	for cat in categories:
		with open('business.csv') as bfile:
			reader = csv.reader(bfile);
			for row in reader:
				#print cat
				if (cat in row[2]):
					idList.append(row[0])
					name.append(row[1])

	print len(name), "matches found"
	if len(name) > 500:
		csvFile=csv.writer(open(gen_category+".csv","wb+"));
		csvFile.writerow(["name", "id", "date", "stars","text"]);
		#print name
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
		return 1
	else:
		print "Not enough data points. Won't create csv."
		return 0














