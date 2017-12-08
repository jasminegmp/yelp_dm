import json
import dicttoxml
import get_csv
import star_averager
import re
import string
import numpy as np

def plotter(category_1):
	star_averager.star_plotter(category_1)
	#star_averager.star_plotter(category_2)

def run_test(first_time):
	counter=0;
	category_list = []

	category_list = json.load(open('categories.json'))
	#print category_list[1]['parents']
	"""
	############################################
	"""
	if first_time:
		fileobj  = open("categories.txt", "w")
		for i in range(len(category_list)):
			#print category_list[i]["parents"]
			if category_list[i]['parents'] == ['restaurants']:
				#s = re.sub('[^0-9a-zA-Z]+', '*', category_list[i]['title'])
				s = category_list[i]['title']
				title_csv = string.replace(s, '/', '_')
				output = get_csv.create_csv(title_csv,[s])
				if output:
					fileobj.write(s + "\n")
				print category_list[i]['title']
		fileobj.close()
	n = 0
	for i in range(len(category_list)):
		if category_list[i]['parents'] == ['restaurants']:
			n = n + 1
	found_category_list = []

	fileobj = open("categories.txt")
	for line in iter(fileobj):
		line = string.replace(line, '\n', '')
		found_category_list.append(line)
	fileobj.close()
	
	print found_category_list

	fileobj = open("output.txt", "w")

	for i in range(len(found_category_list)):
		gen_category_1 = found_category_list[i]
		for j in range(len(found_category_list)):
			gen_category_2 = found_category_list[j]
			print gen_category_1
			print gen_category_2
			dtw_dist = star_averager.pattern_finder(gen_category_1, gen_category_2)
			comparison = gen_category_1 + "\t" + gen_category_2 + "\t" + str(dtw_dist)
			fileobj.write(comparison + "\n")
	fileobj.close()

run_test(1)
plotter("cafe")

