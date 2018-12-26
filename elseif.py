#- If-else
#- Expression and statement
#- Logical operator
#- If else and elif
#- statement blocks via independent
#
#
#if <expression>:
#	<statement>:
#elif <expression>:
#elif <expression>:
#else:
#
#age<=19    not allowed for drink
#age>=20  allowed for drink



#import sys, os
from __future__ import print_function
age = int(input("Please enter your age:"))
if age<=19:
	print('Not allowed for drink')
elif age>=20:
	print('Allowed for drink')

