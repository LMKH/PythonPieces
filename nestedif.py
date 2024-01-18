#store the value here.
value = 201

#runs through each conditional to see if it matches with the user inputted value. No need for elif.
if value < 200:
    print("Value is less than 200")
    if value < 150:
        print("Value is less than 150")
        if value < 100:
            print("Value is less than 100")
            if value == 50:
                print("Value is 50")

#if the user inputted value is not matching with any of the above conditions, 
#it is automatically assumed that the value in this case is not less than 200.
else:
    print("Value is not less than 200")