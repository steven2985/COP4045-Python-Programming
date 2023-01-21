# calculate the area and circunference of a circle from its radius
# step 1: prompt user for a radius 
# step 2: apply the area formula 
# step 3: print out the results 

import math # math library for python

radius_str = input ("Enter the radius of your circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print ("The circumference is: ", circumference, \
    " and the area is: ", area)