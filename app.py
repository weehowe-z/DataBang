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
user_life_path = "./data/user_life.csv"
diet_basic_path = "./data/##ID##/diets.csv"
user_id = "0a80c1dd"


def getHeightWeightScatter(file):
	
	frame = read_csv(user_basic_path)
	#frame['身高/cm'].plot()
	male = []
	female = []
	for i in range(0,len(frame.index)):
		if frame['性别'][i]=='男':
			data = []
			data.append(frame['身高/cm'][i])
			data.append(frame['体重/kg'][i])
			male.append(data)
		elif frame['性别'][i]=='女':
			data = []
			data.append(frame['身高/cm'][i])
			data.append(frame['体重/kg'][i])
			female.append(data)
	file.write("##Height-Weight-Scatter##\n\n")
	file.write("Male\n" + str(male) + "\n\n")
	file.write("Female\n" + str(female)+"\n\n\n")


def getDailyEnergyType1(file,people_id):
	frame = read_csv(diet_basic_path.replace("##ID##",people_id))
	prevDate = ""
	dailyEnergy = []
	data = None
	for i in range(0,len(frame.index)):
		if frame['日期'][i] != prevDate:
			if data!=None:
				dailyEnergy.append(data)
			data = [0,0,0,0]
			prevDate = frame['日期'][i]
		if frame['类型'][i] == '早餐':
			data[0] = frame['热量/kcal'][i]
		elif frame['类型'][i] == '午餐':
			data[1] = frame['热量/kcal'][i]
		elif frame['类型'][i] == '晚餐':
			data[2] = frame['热量/kcal'][i]
		else:
			data[3] = frame['热量/kcal'][i]
	dailyEnergy.append(data)
	file.write("##DaliyEnergy1##ID"+people_id+"\n\n")
	file.write(str(dailyEnergy) + "\n\n")

def getDailyEnergyType2(file,people_id):
	frame = read_csv(diet_basic_path.replace("##ID##",people_id))
	dailyEnergy = []
	breakfast = [0,0,0,0,0,0,0]
	lunch = [0,0,0,0,0,0,0]
	dinner = [0,0,0,0,0,0,0]
	other = [0,0,0,0,0,0,0]
	data = None
	for i in range(0,len(frame.index)):
		date = int(frame['日期'][i][-1]) - 1
		if frame['类型'][i] == '早餐':
			breakfast[date] = frame['热量/kcal'][i]
		elif frame['类型'][i] == '午餐':
			lunch[date] = frame['热量/kcal'][i]
		elif frame['类型'][i] == '晚餐':
			dinner[date] = frame['热量/kcal'][i]
		else:
			other[date] = frame['热量/kcal'][i]

	file.write("##DaliyEnergy2##ID"+people_id+"\n\n")
	file.write(str(breakfast) + "\n")
	file.write(str(lunch) + "\n")
	file.write(str(dinner) + "\n")
	file.write(str(other) + "\n")

def getAverageSleepTime():
	frame = read_csv(user_life_path)
	#print frame.describe()
	num = 0
	for i in range(0,len(frame.index)):
		if frame['睡眠时长'][i]== '6h到7h' or frame['睡眠时长'][i] == '小于5小时' or frame['睡眠时长'][i]=="5h到6h":
			print 1
			num += 1
	print num/float(len(frame.index))

def main():
	file = open("./output.txt", 'a+')
	try:
		#getDailyEnergyType2(file,user_id)
		#getHeightWeightScatter(file)
		getAverageSleepTime()
	except Exception, e:
		raise
	finally:
		file.close()


if __name__ == '__main__':
	main()
