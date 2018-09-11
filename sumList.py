numberList=[] #initializing an empty list
def sumlist(numberList):
	total=0 # initializing total=0
	for i in numberList:
		if isinstance(i,list): # checking if there is a nested list
			total +=sumlist(i)
		else:
			total+=i
			
	return total
print(sumlist([2,4,6,[5,6,0],0]))
	


		
		
		
		
			



