Year_of_birth=input("Which year were you born?:") # prompting the user to enter the year they were born
currentDate=2018 # variable holding the current date to calculate age

def age():
	age=currentDate-int(Year_of_birth)  #formula to determine age
	if age<18:
		print("You are a minor.")
		
	if age>=18 and age<36:
		print("You are a youth.")
		
	if age>=36:
		print("You are an elder")
		
age()
	
    


	
    


 
    
	
	









	
    


	
    


 
    
	
	







