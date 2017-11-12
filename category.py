from datetime import datetime
from bs4 import BeautifulSoup as soup
import json
import csv
import dicttoxml
from matplotlib import pyplot as plt

print ""
print "This is a modified version of code.py"
print "This includes pulling out category from business.json"
print ""

print ""
print "DataMining Project (Baily, Jasmine, Shirin)"
print "     Converting business.json to csv"
print "         extracting id,name,reviewCount ...",
csvFile= csv.writer(open("business.csv", "wb+"));
csvFile.writerow(["id", "name", "category", "reviewCount"]);
counter=0;
#xml="";
#we want to extranct business id,name,review count
with open('../yelp_ds/business.json') as f:
    for line in f:
        counter+=1;
        content = json.loads(line)
        #xml+=(dicttoxml.dicttoxml(content));
        csvFile.writerow([content["business_id"], content["name"].encode('utf-8'), content["categories"], content["review_count"]]);
        #print counter
print "done"

#############################################
#############################################

print "     Converting reviews to csv"
print "         extracting businessId,date,stars,text ...",
csvFile= csv.writer(open("reviews.csv", "wb+"));
csvFile.writerow(["id", "name", "date", "stars","text"]);
counter=0;
#xml="";
#we want to extranct business id,date,stars and text
with open('../yelp_ds/review.json') as f:
    for line in f:
        counter+=1;
        content = json.loads(line)
        #xml+=(dicttoxml.dicttoxml(content));
        csvFile.writerow([content["business_id"], content["date"], content["stars"],content["text"].encode('utf-8')]);
       # print counter
print "done"


