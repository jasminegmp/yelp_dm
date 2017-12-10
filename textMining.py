from nltk.corpus import stopwords
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from datetime import datetime
import pickle
date_format = "%Y-%m-%d"

cachedStopWords =  set(stopwords.words('english'))

print "     Enter the Start Date(yyyy-mm-dd):",
startdate=datetime.strptime(raw_input(),date_format);
print "     Enter the End Date:(yyyy-mm-dd):",
enddate=datetime.strptime(raw_input(),date_format);
print "     Enter the name of the first file:",
file=raw_input();
print "     Enter the name of the second file:",
file2=raw_input();
csvFile=csv.writer(open("words.csv","wb+"));
csvFile.writerow(["id", "date", "stars","text"]);

wholeText="";
textArray=[]

print "         searching for reviews in that period of time ... ",

f1 = pd.read_csv(file+".csv")
#df = pd.DataFrame(f1, columns=['date'])
#df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
#df['date'] = df['date'] + pd.to_timedelta(df.groupby('date').cumcount(), unit='h')

with open(file+'.csv') as f1:
    reader = csv.reader(f1);
    c=0;
    for row in reader :
        if c!=0:
            d=datetime.strptime(row[2],date_format);
            if startdate <= d <= enddate:
                for word in row[4].split():
                    word=word.lower();
                    if word not in cachedStopWords:
                        textArray.append(word)
                        wholeText += word+ " ";

        c=1
with open(file2+'.csv') as f1:
    reader = csv.reader(f1);
    c=0;
    for row in reader :
        if c!=0:
            d=datetime.strptime(row[2],date_format);
            if startdate <= d <= enddate:
                for word in row[4].split():
                    word=word.lower();
                    if word not in cachedStopWords:
                        textArray.append(word)
                        wholeText += word + " ";

        c=1

wholeText= ' '.join([word for word in wholeText.split() if word not in cachedStopWords])

thefile = open('array.txt', 'w')
counts=Counter(textArray)
print counts



# Generate a word cloud image
wordcloud = WordCloud().generate(wholeText)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(wholeText)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
