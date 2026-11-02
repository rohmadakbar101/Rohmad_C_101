person_1 = {
    'first_name': 'al',
    'last_name': 'kina',
    'age': 13,
    'city': 'bekasi'
}

person_2 = {
    'first_name': 'rohmad',
    'last_name': 'akbar',
    'age': 18,
    'city': 'sukoharjo'
}

person_3 = {
    'first_name': 'jeva',
    'last_name': 'gasut',
    'age': 99,
    'city': 'gotham'
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"\nInformation about {full_name}:")
    
    for key, value in person.items():
        if isinstance(value, str):
            print(f"  {key.title()}: {value.title()}")
        else:
            print(f"  {key.title()}: {value}")