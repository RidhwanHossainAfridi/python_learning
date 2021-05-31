# Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi #we could have done pi = 3.1416

radius= float(input("Enter the radius of the circle: "))
area = float(pi) * radius**2 
print("The area of the circle: " + str(area))
