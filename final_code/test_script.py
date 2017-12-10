import test_lib
import ts_lib
import preprocessing
import textMining
import review_plotter
print ""
print "Data Mining Project: 'YTrend: Why did you review me like that?'" 
print "Jasmine Kim, Shirin Haji Amin Shirazi, Bailey Herms"
print "Fall 2017 Quarter" 
print "CS 235"
print ""

print "Performing data pre-processing..." 

# set this flag if this if the first time you're running through the script
first_time_flag = 0

if first_time_flag:
	print ""
	# JSON -> CSV and business ID mapping data pre-processing
#preprocessing.jsn_to_csv_cleanup('../yelp_ds/business.json', '../yelp_ds/review.json')

	print ""
	# Specify parent category you're interested in
	# In this case, restaurants
	preprocessing.find_relevant_categories('restaurants', "restaurants_category")

# Note, third arg is NOP
#test_lib.run_test(1, "restaurants_category", 0)
#test_lib.run_test(2, "restaurants_category", 0)
#test_lib.run_test(3, "El Pollo Loco", "restaurants_category")
test_lib.run_test(4, "FastFood", 0)


#review_plotter.review_plotter("Barbeque")
#for i in range(6,12):
	#textMining.text_mine("Chipotle Mexican Grill", "Chipotle Mexican Grill", "2015-"+str(i)+"-1", "2015-"+str(i)+"-30")
#textMining.text_mine("Chipotle Mexican Grill", "Steakhouses", "2016-6-1", "2016-9-30")