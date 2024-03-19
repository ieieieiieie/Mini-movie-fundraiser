#functions


#main routine
instructions = input("would you like to read the instructions? ").lower()

if instructions == "yes" or instructions == "y":
    print("print instructions")

elif instructions == "no" or instructions == "n":
    pass

else:
    print("invalid response, please answer yes or no")