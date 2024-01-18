#list of the available parts in a computer store
available_parts = {         
    "1": "Hard Drive",
    "2": "Monitor",
    "3": "Keyboard",
    "4": "Mouse",
    "5": "Printer",
    "6": "HDMI Cable",
    "7": "DVD Drive",
    "8": "Fax Machine",
}

#current_choice set to none, as there is nothing in our "basket" (dictionary).
current_choice = None

#creates an empty list
computer_parts = {}                 

while current_choice != "0":
    if current_choice in available_parts:

        #"in" checks the key in a dictionary eg 1,2,3
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)

        #"in" in a list checks the items eg "mouse"
        else:
            print(f"Adding {chosen_part}")      
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")

    else:
        print("Please add options from the list:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: Exit")
    current_choice = input("> ")