while True:
    try:
        bill = float(input("How much was your bill?  "))
        break
    except ValueError:
        print('Please give me a number.')    

while True:
    level_of_service = input("How would you rate your level of service:  'good', 'fair', or 'bad'?  ")
    if level_of_service not in ('good', 'fair', 'bad'):
        print("Please rate the service:  ")
    else:    
        if level_of_service == "good":
            result = .20 * bill 

        elif level_of_service == "fair":
            result = .15 * bill    

        elif level_of_service == "bad":
            result = .10 * bill
    while True:
        split = input("Will you be splitting the check?  ")
        if split == "yes":
            split_amount = float(input("How many ways will the check be split?  "))
            print("Tip amount: $ %.2f " %(result)) 
            total_amount = (result + bill)
            print("Total amount: $ %.2f " %(total_amount))
            print("Amount per person: $ %.2f " %(total_amount / split_amount))
        else:
            if split != "yes":
                print("Tip amount: $ %.2f " %(result))  
                print("Total amount: $ %.2f " %(result + bill))  
        break
    break        

