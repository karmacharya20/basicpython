from __future__ import print_function
import math

def circumference(radius):
	return math.pi * 2 * radius
	

circles = [["First circle",4.4,2],["Second circle",3.7,3],["Third circle",8.4,4]]
circles[0][2] = circumference(circles[1][1])
print (circles[0][2])
