places = ["Bali", "Tokyo", "Lombok", "Jakarta", "Bandung"]

print("Original list:")
print(places)

print("\nAlphabetical order:")
print(sorted(places))

print("\nOriginal list again:")
print(places)

print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

print("\nOriginal list again:")
print(places)

places.reverse()
print("\nReversed list:")
print(places)

places.reverse()
print("\nOriginal list again:")
print(places)

places.sort()
print("\nSorted list:")
print(places)

places.sort(reverse=True)
print("\nReverse sorted list:")
print(places)