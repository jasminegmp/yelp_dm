from datetime import datetime
from BeautifulSoup import BeautifulSoup as soup
import json
import csv
import dicttoxml
from matplotlib import pyplot as plt



print ""
print "DataMining Project (Baily, Jasmine, Shirin)"
print "     Converting business.json to csv"
print "         extracting id,name,reviewCount ...",
csvFile= csv.writer(open("business.csv", "wb+"));
csvFile.writerow(["id", "name", "reviewCount"]);
counter=0;
#xml="";
#we want to extranct business id,name,review count
with open('../dataset/business.json') as f:
    for line in f:
        counter+=1;
        content = json.loads(line)
        #xml+=(dicttoxml.dicttoxml(content));
        csvFile.writerow([content["business_id"], content["name"].encode('utf-8'), content["review_count"]]);
        #print counter
print "done"

#############################################
#############################################

print "     Converting reviews to csv"
print "         extracting businessId,date,stars,text ...",
csvFile= csv.writer(open("reviews.csv", "wb+"));
csvFile.writerow(["id", "date", "stars","text"]);
counter=0;
#xml="";
#we want to extranct business id,date,stars and text
with open('../dataset/review.json') as f:
    for line in f:
        counter+=1;
        content = json.loads(line)
        #xml+=(dicttoxml.dicttoxml(content));
        csvFile.writerow([content["business_id"], content["date"], content["stars"],content["text"].encode('utf-8')]);
       # print counter
print "done"


############################################
############################################
print "     Now enter the business name intended:",
bName=raw_input();
csvFile=csv.writer(open(bName+".csv","wb+"));
csvFile.writerow(["id", "date", "stars","text"]);

idList=[];
print "         searching for ids related to that name ... ",
c=0
with open('business.csv') as bfile:
    reader = csv.reader(bfile);
    for row in reader:
        if row[1]==bName:
            idList.append(row[0])
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
            csvFile.writerow([rrow[0],rrow[1],rrow[2],rrow[3]]);
            dates.append(rrow[1]);
            stars.append(rrow[2]);
            count+=1

#dates=list(set(dates));
sorted(dates, key=lambda d: map(int, d.split('-')))

plt.scatter(dates, stars,label=“stars”)
plt.xlabel("time stamps")
plt.ylabel("stars")
plt.legend(loc=2)
plt.show()

