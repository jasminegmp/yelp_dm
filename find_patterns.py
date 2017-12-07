import get_csv
import star_averager


############################################
gen_category = "healthy"
categories = ["Acai Bowls", "Farmers Market", "Honey", "Poke", "Kombucha"]

get_csv.create_csv(gen_category, categories)
star_averager.star_plotter(gen_category)