# Try Except: Apples

I made this programme when first learning Try Except. Try Except lets me as the programmer try out the code for errors. Try, lets me do the test. Except, lets me handle any errors that may come up in my way instead of a generic fail message.

Exception handling here allows me to write an error message. As you can see if the user inputs the number 0, it will ask the user to try again as you can not divide a number by 0.

In this code, the programme asks "How many ways do you want to divide apples?". It then (if the value inputted is not 0) takes the inputted number and divides it by 10.

***
# Keyboard Inputs

Being able to handle keyboard inputs is incredibly important. Being able to ask the user to input multiple pieces of information alongside returning information to them is fundamental.

This code asks the user to input their name, then it asks for their age. After this, it automatically replies with what their age will be in 5+ years. Finally, it asks the user to input their GPA (Grade Point Average). It returns their grade in a floating point number.

***
# If, Elif and Else

If, elif and else statements are used to help automate the decision-making process in programming. They are conditional statements, and for these statements to run their respective corresponding conditions must be met.

Here I have made a high score checker and a grade checker. For the high score of 9000 to be beaten, the user must input a number greater than 9000. Else they will not have beaten the high score.

For the grade checker, the user must input their int value. The programme will then run through each condition from Grade A to Grade F. The programme will stop when it has met the correct condition via the elif statements.

***
# Nested If

Nested If's is where we nest an if statement inside of another if statement without the need for an else statement. However, you can still include an else statement, like how I have done here.

Nesting an if statement makes the programme flow in a semantic order and it also makes the code easier to understand and follow.

***
# Computer Parts: Dictionary

In this programme I utilise the dictionary method to create a "shopping basket". The user simply inputs the corresponding number to what they want off the available_parts "menu".

The programme will add the selected items to a list and will continue to do this until the user quits. If the user wishes to remove something they have added to the list, all they need to do is simply input the correct number again and it will be removed from the list. This is done by using the .pop() method. If the user enters a number that is not on the list, they will be asked to try again by re-inputting the number.

***
# Candidates

In a list, we have the required skills needed for a job role. The candidates MUST have all 3 of the required skills to be accepted. Using a dictionary, we can see each candidate's name and with each candidate, they have a corresponding nested dictionary that holds all of their skills. 

I utilise the set() function to create a new object. A for loop will take the candidate, and their skills and see if they have ALL the required skills. If they do, they get added to the new interviewee's dictionary. I do this by utilising the .add() method. If they do not have all the required skills they will be ignored. Finally, the programme will return a dictionary to the user with all the candidates who have the required skills.
