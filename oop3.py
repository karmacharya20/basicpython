from __future__ import print_function
import math
import random

class circle:
	def calcircumference(self):
		return math.pi * 2 * self.radius
	

circles = []
for i in range(0,10):
	c=circle()
	c.radius = random.uniform(1.1,9.5)
	#c.circumference = c.calcircumference(c.radius)
	circles.append(c)
	
for c in circles:
	print("Radius:",c.radius, "Circumference:",c.calcircumference())
	