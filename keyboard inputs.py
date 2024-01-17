#prompt for the user.
name = input("What is your name?: ")

#what it is you want the user to see.
print("Welcome to Python", name)
age = input("How old are you?: ")
print("You are", age, "years old")
age = int(age)

#remember! they're different, strings & intergers
age = age + 5 
print("In 5 years you will be:", age)

#float converts the interger into a floating point number
gpa = input("What is your GPA?: ")
print("Your GPA is", gpa)
gpa = float(gpa)
gpa = gpa + 10