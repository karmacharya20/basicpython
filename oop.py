from __future__ import print_function
import math

def circumference(radius):
	return math.pi * 2 * radius
	

circlename = "First Circle"
circleradius = 4.4

circle2name = "Second circle"
circle2radius = 3.7

circle3name = "Third circle"
circle3radius = 1

circumference1 = circumference(circleradius)
print(circumference1,circlename)
circumference2 = circumference(circle2radius)
print(circumference2,circle2name)
circumference3 = circumference(circle3radius)
print(circumference3,circle3name)
