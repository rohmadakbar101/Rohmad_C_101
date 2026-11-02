favorite_pizzas = ['pepperoni', 'margherita', 'hawaiian']

for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza.")

print("\nI really love pizza!")

#selanjutnya
animals = ["turtle", "cat", "dog", "hamster", "parrot"]

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("\nAny of these animals would make a great pet!")

#terakhir
cubes = [number ** 3 for number in range(1, 11)]

for cube in cubes:
    print(cube)