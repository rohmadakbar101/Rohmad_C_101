prompt = "Please enter a pizza topping you would like:"
prompt += " (Enter 'quit' when you are finished) "

while True:
    topping = input(prompt)
    
    if topping.lower() == 'quit':
        break
    
    print(f"  I'll add {topping} to your pizza!")