"""
Assignment 7: Color addition and subtraction

Name: Avigail Martinez & Steven Fernandez| Date: July 16, 2021 | Course: 4045-002, COP 4045-001: Python Programming 
"""
from tabulate import tabulate

class Color(object):
    
    """
    1. An initializer (“constructor”) that should also include code to coerce the 
    r,g,b values into required range (by clipping values below 0 or above 1)
    """
    def __init__(self,r,g,b):
        
        if r < 0: r = 0
        if r > 1: r = 1
        
        if g < 0: g = 0
        if g > 1: g = 1
        
        if b < 0: b = 0
        if b > 1: b = 1
        
        self.red = float(r)
        self.green = float(g)
        self.blue = float(b)
    """
    3. Overloaded addition operator.
    """
    def __add__(self,x):
        red= self.red + x.red
        green = self.green + x.green
        blue= self.blue + x.blue
        result1= Color(red, green, blue)
        return result1
    
    """
    4. Overloaded subtraction operator.
    """
    def __sub__(self,x):
        red= self.red - x.red
        green = self.green - x.green
        blue= self.blue - x.blue
        result2= Color(red, green, blue)
        return result2
    """
    2. A string representation method, for “pretty printing” the contents of a 
    Color object.
    """
    def __str__(self):
        if self.red ==1 and self.green==0 and self.blue==1:
            self.a= "Magenta"
        elif self.red ==1 and self.green==0 and self.blue==0:
            self.a= "Red"
        elif self.red ==0 and self.green==0 and self.blue==1:
            self.a= "Blue"
        elif self.red ==0 and self.green==1 and self.blue==1:
            self.a= "Cyan"
        elif self.red ==1 and self.green==1 and self.blue==0:
            self.a= "Yellow"
        elif self.red ==0 and self.green==0 and self.blue==0:
            self.a= "Black"
        elif self.red ==1 and self.green==1 and self.blue==1:
            self.a= "White"
        elif self.red ==0 and self.green==1 and self.blue==0:
            self.a= "Green"
        else:
            self.a= [round(self.red,1), round(self.green,1), round(self.blue,1)]
        return f'{self.a}'
    
    def __repr__(self):
        self.red= round(self.red,1)
        self.green= round(self.green,1)
        self.blue= round(self.blue,1)
        return f'{self.red} {self.green} {self.blue}'
            

"""
Because we use the class methods at least 2 times (if you insert color names or color values)
we decided to call the class in a function to be recursive.
"""

def call_class(color1, color2):
    COLOR1= Color(color1[0],color1[1],color1[2]) #insert the values to the class
    COLOR2= Color(color2[0],color2[1],color2[2]) ##insert the values to the class
    
    result1= COLOR1.__add__(COLOR2) #addition
    result2= COLOR1.__sub__(COLOR2) #subtraction
    
    print(" ")
    print("-----The results are-----")
    print("COLOR NAMES")
    print(COLOR1.__str__()," + ",COLOR2.__str__(), "= ",result1.__str__()) #pretty print the results using the method __str__
    print(COLOR1.__str__()," - ",COLOR2.__str__(), "= ",result2.__str__()) ##pretty print the results using the method __str__
    print("COLOR RGB VALUES")
    print(COLOR1.__repr__()," + ",COLOR2.__repr__(), "= ",result1.__repr__()) #pretty print the results using the method __repr__
    print(COLOR1.__repr__()," - ",COLOR2.__repr__(), "= ",result2.__repr__()) #pretty print the results using the method __repr__

#You should also create a dictionary with the color name as key and the values as the associated RGB tuples.       
dic_colors= {}
dic_colors= {'RGB ': ['R:','G:', 'B:'],
           'RED':  [1,0,0],
           'GREEN': [0,1,0],
           'BLUE': [0,0,1], 
           'CYAN': [0,1,1],
           'MAGENTA': [1,0,1],
           'YELLOW': [1,1,0],
           'BLACK': [0,0,0],
           'WHITE': [1,1,1]}

print("This program performs addition and subtraction using colors.")

T=tabulate(dic_colors, headers="keys",tablefmt="rst", colalign=("center")) #pretty print the dictionary
print(T)

#Ask the user the way they want to insert the colors (By color name or by color values)
e= input("Enter (C) to input the name of the color.\nEnter (V) to input the values of the color.\n")

if e.upper()== "C":
    c1_str=input("Enter color 1 name: ")
    c2_str=input("Enter color 2 name: ")
    
    #check if the color name is in the dictionary
    if (c1_str.upper() in dic_colors) and (c2_str.upper() in dic_colors):
        color1= dic_colors[c1_str.upper()]
        color2= dic_colors[c2_str.upper()]
        
        call_class(color1, color2) 
     
    else:
        print("Enter a valid color name")
        
elif e.upper()== "V":
    color1 = list(map(float,input("Enter the values of COLOR 1: ").strip().split()))[:3]
    color2 = list(map(float,input("Enter the values of COLOR 2: ").strip().split()))[:3]
    
    #Check if is a RGB lenght
    if (len(color1)==3) and (len(color2)==3):
        call_class(color1, color2)
    else:
        print("The colors MUST have 3 values, try again")
else:
    print("Enter a valid option")