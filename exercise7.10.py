responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")