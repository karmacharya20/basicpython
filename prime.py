#from __future__ import print_function
#num=90
#Prime = True
#for text in range(2,num):
#	if(num%text ==0 and num!=text):
#		print(num,"equal",text,"*",num/text)
#		Prime=False
#	if Prime:
#		print(num,"is a Prime number")
#	else:
#		print(num,"is not a prime number")
		
		
#from __future__ import print_function
#num=7
#Prime = True
#for text in range(2,num):
#	if(num%text ==0 and num!=text):
#		print(num,"equal",text,"*",num/text)
#		break
#else:
#	print(num,"is a prime number")
	
from __future__ import print_function
num=7
text=2
Prime = True
while text<num:
	if(num%text ==0 and num!=text):
		print(num,"equal",text,"*",num/text)
		break
	text = text+1
else:
	print(num,"is a prime number")