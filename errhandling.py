#Error handling
#-Why handling errors?
#-Basic try-Except statement
#-Exception specific types of errors
#-else and finally clause

#from __future__ import print_function
#print("let is solve the eqn(x/2)/(x-y)")
#x=float(input("Please Enter a value for x:"))
#y=float(input("Please Enter a value for y:"))
#z=(x/2)/(x-y)
#print ("Solving(x/2)/(x-y) for value x = ' ',x 	and y",y,"we get the result:",z)

#1-zerodivisionerror
#from __future__ import print_function
#while True:
#	try:
#		print("let is solve the eqn(x/2)/(x-y)")
#		x=float(input("Please Enter a value for x:"))
#		y=float(input("Please Enter a value for y:"))
#		if x==0 or y==0:
#			break
#		z=(x/2)/(x-y)
#		print ("Solving(x/2)/(x-y) for value x = ",x ,	"and y",y,"we get the result:",z)
#	except:
#		print ("Error")

#2.nameerror
#from __future__ import print_function
#while True:
#	try:
#		print("let is solve the eqn(x/2)/(x-y)")
#		x=float(input("Please Enter a value for x:"))
#		y=float(input("Please Enter a value for y:"))
#		if x==0 or y==0:
#			break
#		z=(x/2)/(x-y)
#		print ("Solving(x/2)/(x-y) for value x = ",x ,	"and y",y,"we get the result:",z)
#	except Exception as e:
#		print ("There was an unknown error with the code")
#		print("Error message:",str(e))
		

#3.error 3
from __future__ import print_function
while True:
	try:
		print("let is solve the eqn(x/2)/(x-y)")
		x=float(input("Please Enter a value for x:"))
		y=float(input("Please Enter a value for y:"))
		if x==0 or y==0:
			break
		z=(x/2)/(x-y)
		print ("Solving(x/2)/(x-y) for value x = ",x ,	"and y",y,"we get the result:",z)
	except zeroDivisionError as e:
		print("There was an error with the code")
		print("You     in a calue that caused a division by zero")
		
