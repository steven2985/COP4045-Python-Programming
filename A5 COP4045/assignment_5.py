# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:41:40 2021

"""
#Libraries

import csv
from tabulate import tabulate

#Design and implement a function that computes the averages.
def average (x):
    s= sum(x)
    a= s/len(x)
    return a

#Design and implement another function to handle the “pretty” printing for 
#this particular type of dictionary.
def printtable(dic):
    print('This python program computes the average of each attribute in Iris Dataset. \nTo compute the average, the program use all the samples for each attribute \nbased on their specie')
    a=tabulate(dic, headers="keys",tablefmt="rst")
    print(a)
    

SL_SE= []
SW_SE= []
PL_SE=[]
PW_SE=[]

SL_VE= []
SW_VE= []
PL_VE=[]
PW_VE=[]

SL_VI= []
SW_VI= []
PL_VI=[]
PW_VI=[]

# Keep the file handling functionality outside of the functions.

#Get all the values from the dataset and save each of them in a list based on their specie
with open('iris.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['species']=='setosa':
            SL_SE.append(float(row['sepal_length']))
            SW_SE.append(float(row['sepal_width']))
            PL_SE.append(float(row['petal_length']))
            PW_SE.append(float(row['petal_width']))
            
        elif row['species']=='versicolor':
            SL_VE.append(float(row['sepal_length']))
            SW_VE.append(float(row['sepal_width']))
            PL_VE.append(float(row['petal_length']))
            PW_VE.append(float(row['petal_width']))
            
        elif row['species']=='virginica':
            SL_VI.append(float(row['sepal_length']))
            SW_VI.append(float(row['sepal_width']))
            PL_VI.append(float(row['petal_length']))
            PW_VI.append(float(row['petal_width']))

"""
Create a dictionary with the key as the species name and the values as (placeholders for) 
the averages of each of the four attributes/features of each data point: 
petal length, petal width, sepal length, and sepal width.
"""            
dic= {}
dic= {'Species: ': ['Attributes (cm)','Avg. Sepal Length:','Avg. Sepal Width:','Avg. Petal Length:','Avg. Petal Width:'],
      'Setosa': ['',round(average(SL_SE),2),round(average(SW_SE),2),round(average(PL_SE),2), round(average(PW_SE),2)],
      'Versicolor':['', round(average(SL_VE),2),round(average(SW_VE),2), round(average(PL_VE),2), round(average(PW_VE),2)],
      'Virginica': ['',round(average(SL_VI),2), round(average(SW_VI),2), round(average(PL_VI),2), round(average(PW_VI),2)]}

#Print the dictionary using the pretty printing function
printtable(dic)