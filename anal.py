#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import numpy as np
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
matplotlib.style.use('ggplot')

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

user_basic_path = "./data/user_basic.csv"
diet_basic_path = "./data/##ID##/diets.csv"
user_id = "0a80c1dd"


def main():
	#user_basic_frame = read_csv(user_basic_path)
	user_diets_frame = read_csv(diet_basic_path.replace("##ID##",user_id))
	num = 0
	daily_energy = []
	energy = []
	prevDate = ""

	for diets in user_diets_frame	:
		print user_diets_frame.head()
	# for diets in user_diets_frame['热量/kcal']:
	# 	if 
	# 	daily_energy.append(float(diets))
		
	# 	if num%3 == 2:
	# 		energy.append(daily_energy)
	# 		daily_energy = []
	# 	num += 1


	# print energy
	# df2 = DataFrame(energy, columns=['breakfast','lunch','dinner'])
	# df2.plot(kind='barh', stacked=True);
	# plt.show()




# def main():
# 	user_basic_frame = read_csv(user_basic_path)
# 	#user_basic_frame['身高/cm'].plot()
# 	user_basic_frame.info()
# 	print user_basic_frame['身高/cm'].describe()

# 	Sorted = user_basic_frame.sort_values(['身高/cm'], ascending=False)
# 	#Sorted['身高/cm'].plot()

# 	Sorted.to_csv('births1880.csv',index=False,header=False)
# 	user_basic_frame['身高/cm'].plot()

# 	plt.show()






if __name__ == '__main__':
	main()
