#used in order to see if someone is old enough to buy alcohol
#user inputs their age
age = 21

#if checks if the inputted age is greater than or equal to 21
if age >= 21:
    print("You are legally allowed to buy alcohol")
    print("What would you like?")

#this line is not part of the if statement. it will run regardless if the value is or is not greater than or equal to 21.
print("End Program")

# to see if someone is old enough to vote AND is a citizen
age = 18
citizen = "True"

if(age >= 18 and citizen == "True"):
    print("You are eligible to vote")