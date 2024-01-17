#question
print("We have 10 pounds of apples.")

#input from the user
number = input("How many ways are we dividing the apples? ") 

#assigned to number which is cast as an interger
number = int(number) 
try:
    #we then divide 10 by the inputted number
    poundsEach = 10/number
    print("Each person gets", poundsEach, "pounds of apples.")

#this stops an error if someone trys to input the number 0
except ZeroDivisionError: 
    #exits
    print("No, You cannot divide by 0. Try again please.") 