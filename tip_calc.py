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

        print("Tip amount: $ %.2f " %(result)) 

        print("Total amount: $ %.2f " %(result + bill))
        break
            
        
    
     
