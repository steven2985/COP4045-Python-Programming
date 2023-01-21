#Librarys

import csv
import pylab as plt
from tabulate import tabulate
import os


#Functions 
def option1(data2015):
    x= True
    while x==True:
        
        print('Enter the MPG interval you are interested in:')
        mini = int(input('Enter the minimun value: '))
        maxi = int(input('Enter the maximun value: '))
        
        if mini>maxi:
            print('Enter a valid interval')
        else:
            titles=['Make','Model']
            datafound =[]

            for i in range(1,len(data2015)-1):
                if ((int(data2015[i][9])>mini) and (int(data2015[i][9])<maxi)):
                    if((int(data2015[i][10])>mini) and (int(data2015[i][10])<maxi)):
                        if(int(data2015[i][11])>mini) and (int(data2015[i][11])<maxi):
                            datafound.append(data2015[i][2:4])
            x= False
            
    if len(datafound)==0:
        table="No found info"
    else:
        table= tabulate(datafound,titles,tablefmt='psql')
            
    return table


def plotfigure(data2020,col,a):
    x=[]
    y=[]

    for i in range(1,len(data2020)-1):
        x.append(float(data2020[i][0]))
        y.append(float(data2020[i][col]))
    
    if a.upper()=='D':
        plt.plot(x,y, 'r',label=data2020[0][col])
        plt.xlabel('Model Year')
        plt.legend(loc='upper right')
        plt.grid()
    elif a.upper()=='S':
        fig= plt.plot(x,y, 'r',label=data2020[0][col]) 
        plt.xlabel('Model Year')
        plt.legend(loc='upper right')
        plt.grid()
        plt.savefig('fig.png')
        plt.close()
        print('Plot Saved')
        
        
def option2 (data2020):
    option21= str(input("Enter an option: \n (H)ighway MPG \n (C)ity MPG\n (O)verall MPG\n"))

    if (option21.upper()=='H'):
        a= str(input("Enter: \n (D)isplay Plot \n (S)ave plot \n"))
        plotfigure(data2020,6,a)
    elif(option21.upper()=='C'):
        a= str(input("Enter: \n (D)isplay Plot \n (S)ave plot \n"))
        plotfigure(data2020,5,a)
    elif(option21.upper()=='O'):
        a= str(input("Enter: \n (D)isplay Plot \n (S)ave plot \n"))
        plotfigure(data2020,4,a)
        
        
data2015= []
data2020=[]

print('This application will allow you to know some data about the fuel economy in the US.\nThese data were obtained from THE US ENVIRONMENT PROTECTION (EPA).')
with open('epadata2015.csv', 'r') as file:
    reader = csv.reader(file)
    for rows in reader:
        data2015.append(rows)
        
with open('epadata2020.csv', 'r') as file:
    reader = csv.reader(file)
    for rows in reader:
        data2020.append(rows)

variable= True

while variable == True:
    option= int(input("Enter an option: \n (1) Mileage Info \n (2) Trend Plot\n"))
    if option==1:
        values = option1(data2015)
        print(values)
        variable= False
    elif option==2:
        option2(data2020)
        variable= False
    else:
        print('Enter a valid option')