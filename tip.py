# Tip calculator
# (15%, 18% and 20%)

while True:
    try:
        user_input = input("What is the total of your check? > $")
        total_check = float(user_input)
        break 
    except ValueError:
        print("I'm sorry, looks like you typed something incorrectly. Try typing in a number! :)")

# In this next loop, there is no try hermmmm 
# that was my Yoda impression
# Here it will loop unless you type in exactly what is in the () 
while True:
    tip_choice = input("Type 'a' for 15%, 'b' for 18%, or 'c' for 20% > ")
    if tip_choice not in ('a', 'b', 'c'):
        print("I'm sorry, looks like you typed something incorrectly. Please read the instructions and try again!")
    else:
        if tip_choice == "a":
            result = .15 * total_check  
        elif tip_choice == "b":
            result = .18 * total_check
        elif tip_choice == "c":
            result = .20 * total_check
        
        print("You should leave $%.2f " % (result))
        break