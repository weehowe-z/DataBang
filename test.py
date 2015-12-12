import numpy
import csv

user_basic_path = "./data/user_basic.csv"

def getAverage(datas):
	total_height = 0
	total_weight = 0
	total_vital_capacity = 0
	total_num = 0
	for data in datas:
		if float(data[2]) < 100:
			total_height += float(data[2])*100
		else:
			total_height += float(data[2])
		total_weight += float(data[3])
		total_vital_capacity += float(data[8])
		total_num += 1

	average_height = total_height/total_num
	average_weight = total_weight/total_num
	average_capacity = total_vital_capacity/total_num
	return average_height,average_weight,average_capacity



def main():
	readdata = csv.reader(open(user_basic_path))
	datas = []

	for row in readdata:
	    datas.append(row)

	print datas

	total_height = 0
	num = 0
	datas.pop(0)
	print getAverage(datas)




if __name__ == '__main__':
	main()