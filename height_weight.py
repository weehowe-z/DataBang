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


def getHeightWeight():
	
	user_basic_frame = read_csv(user_basic_path)
	#user_basic_frame['身高/cm'].plot()
	male = []
	female = []
	for i in range(0,len(user_basic_frame.index)):
		if user_basic_frame['性别'][i]=='男':
			data = []
			data.append(user_basic_frame['身高/cm'][i])
			data.append(user_basic_frame['体重/kg'][i])
			male.append(data)
		elif user_basic_frame['性别'][i]=='女':
			data = []
			data.append(user_basic_frame['身高/cm'][i])
			data.append(user_basic_frame['体重/kg'][i])
			female.append(data)
	return male,female



def main():
	male,female = getHeightWeight()
	print male
	print female


if __name__ == '__main__':
	main()
