#if else statements
score = 9001
highscore = 9000

#remember if TRUE it will run the if clause, if False it'll run the else clause.
if score > highscore:
    print("You have beaten the high score! Well done!")

# we will only see this, if it runs the else clause.
else:
     print("oh no, you didn't beat the high score. Better luck next time!")
     print("Try again!")

#e.g. if grade greater than or equal to 90 results A, if less than or equal to 60 results F
grade = 55
if grade >= 90:
    letterGrade = "A"
elif grade >= 80:
    letterGrade = "B"
elif grade >= 70:
    letterGrade = "C"
elif grade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"
print(letterGrade)