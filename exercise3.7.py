guests = ["Eshan", "Adib", "Rizky", "naufal", "rohmad", "fayaz", "abi", "Dimas"]
print("Unfortunately, the new table won't arrive in time, so I can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

for i in guests:
    print(f"Dear {i}, you are still invited to dinner.")
    
del guests[-1]