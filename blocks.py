#aslong as the number is between 1 and upto but not including 13 the programme will run.
for i in range(1, 13):
    #example: number 2 (the first i) will print 2 as it hasn't been changed. Then squared (the second i) will multiply itself = 4. 
    #the final i - cubed multiplies the original number by itself twice = 8.
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    #each time the for loop runs it will print 80 stars, as a seperator between each output.
    print("*" * 80)