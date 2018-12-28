from __future__ import print_function
import math
import random

class circle:
	def __int__(self):
		self.radius = random.uniform(1.1,9.5)
	def calcircumference(self):
		return math.pi * 2 * self.radius
	def caldiameter(self):
		return self.radius*2
	def calarea(self):
		return math.pi * ( self.radius**2)

circles = []
for i in range(0,10):
	c=circle()
	#c.radius = random.uniform(1.1,9.5)
	#c.circumference = c.calcircumference(c.radius)
	circles.append(c)
	
for c in circles:
	print("Circumference:",c.calcircumference(),"Diameter :",c.caldiameter(),"Area:",c.calarea())
	