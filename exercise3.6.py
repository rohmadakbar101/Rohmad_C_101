guests = ["Adib","naufal","rohmad","fayaz","abi"]
print("Great news! I found a bigger dinner table.\n")

guests.insert(0, "Eshan")
guests.insert(2, "Rizky")
guests.append("Dimas")

for i in guests:
    print(f"Dear {i}, I would like to invite you to dinner. It would be an honor to have you join me!")