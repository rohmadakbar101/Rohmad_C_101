prompt = "Please enter your age to check the ticket price:"
prompt += " (Enter 'quit' when you are finished) "

while True:
    age_input = input(prompt)
    
    if age_input.lower() == 'quit':
        print("Thank you! Have a great time at the movies.")
        break
    
    age = int(age_input)
    
    if age < 3:
        print("  Your ticket is free!")
    elif 3 <= age <= 12:
        print("  Your ticket cost is $10.")
    else:
        print("  Your ticket cost is $15.")