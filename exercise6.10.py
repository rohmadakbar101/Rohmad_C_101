favorite_numbers = {
    "akbar": [13, 27],
    "al": [100, 50, 25],
    "ronaldo": [7],
    "Messi": [10, 30],
    "naufal": [99, 1]
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()} adalah:")
    
    for number in numbers:
        print(f"  - {number}")