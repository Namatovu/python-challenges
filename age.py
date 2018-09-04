Year_of_birth=input("Which year were you born?")
currentDate=2018
age=currentDate-int(Year_of_birth)
if age<18:
    print("You are a minor.")

if age>=18 and age<36:
    print("You are a youth.")


if age>=36: 
    print("You are an elder")
