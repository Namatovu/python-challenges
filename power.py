def power(a,b):
	if(b==1):
		return b
	if(b !=1):
		return (a*pow(a,b-1))
print(power(3,4))
print(power(2,3))

