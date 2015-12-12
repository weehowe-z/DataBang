# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# # General syntax to import a library but no functions: 
# ##import (library) as (give the library a nickname/alias)
# import matplotlib.pyplot as plt
# import pandas as pd #this is how I usually import pandas
# import sys #only needed to determine Python version number
# import matplotlib #only needed to determine Matplotlib version number

# # Enable inline plotting
# %matplotlib inline

# The inital set of baby names and bith rates


user_basic_path = "./data/user_basic.csv"



names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names,births))
dataFrame = DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

print BabyDataSet
print dataFrame

dataFrame.to_csv('births1880.csv',index=False,header=False)