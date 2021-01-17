while (True):
    try:
        C = float(input("Enter you temperature of Celsius degrees you want to convert to Fahrenheit.  "))
        Fahrenheit = ((C * 9/5) + 32)
        answer = (f"The temperature of {C} Celsius is {Fahrenheit} Fahrenheit.")
        print(answer)
    except (NameError, ValueError):
        print("That did'd work, please give me a number.")
    break

   

