import test_lib
import ts_lib
import preprocessing
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
	preprocessing.jsn_to_csv_cleanup('../yelp_ds/business.json', '../yelp_ds/review.json')

	print ""
	# Specify parent category you're interested in
	# In this case, restaurants
	preprocessing.find_relevant_categories('restaurants', "restaurants_category")

#test_lib.run_test(1, "restaurants_category")
#test_lib.run_test(2, "restaurants_category")
test_lib.run_test(3, "Starbucks", "restaurants_category")