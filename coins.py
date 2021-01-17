print("You have 0 coins.")
count = 0
while True and count != 6:
    answer = input("Do you want another?  ")
    if count == 5:
        print("Sorry, I am out of coins to give.  Goodbye.")
        break
    elif answer == "yes":
        count += 1
        print(f"You have {count} coins.")
    
    else:
        if answer != "yes":
            print("Bye")
            break
        