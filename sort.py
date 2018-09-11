ef sort_list(list1):
	
	dictionary={} #initializing an empty dictionary
	charlist=[]  #initializing an empty list for characters
	evenlist=[]#initializing an empty list for even integers
	oddlist=[]  #initializing an empty list for odd integers
	if  not isinstance(list1,list):
		return "not a list"
	for i in list1:
		if isinstance (i,str):
			charlist.append(i)
		elif i % 2 == 0 and type(i)==int: # checking if a number is even 
			evenlist.append(i)
		elif i % 2 == 1 and type(i)==int: # checking if a number is odd
			oddlist.append(i)
	dictionary["evens"]=sorted(evenlist)
	dictionary["odds"]=sorted(oddlist)
	dictionary["chars"]=sorted(charlist)
	return dictionary
print(sort_list([2,0,6,5,1,7,'z','a']))