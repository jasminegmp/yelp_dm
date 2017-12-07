import get_csv
import star_averager


############################################
gen_category = "restaurants"
categories = ["Restaurants"]
## NOTE:
# First time, you have to run category.py to get the categories.

get_csv.create_csv(gen_category, categories)
star_averager.star_plotter(gen_category)