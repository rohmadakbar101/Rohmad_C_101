guests = ["Al Kina","naufal","rohmad","fayaz","abi"]
guests_cancelled = guests.pop(0)
print(f"Dear {guests_cancelled}, I am sorry to inform you that I can no longer invite you to dinner due to unforeseen circumstances.\n")

guests.insert(0, "Adib")

for i in guests:
    print(f"Dear {i}, I would like to invite you to dinner. It would be an honor to have you join me!")