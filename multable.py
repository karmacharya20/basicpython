#multiple table

def mul_table(x,y):
	for line in range(1,y+1):
		for table in range(1,x+1):
			print (line * table ,"\t",end=""),
		print ("\n")

		

x=5
y=5
mul_table(x,y)
		
#for line in range(1,6):
#	for table in range(1,6):
#		print (line * table,'\t')
#	print 

#HW
#y=mx+c
#(a+b)^2