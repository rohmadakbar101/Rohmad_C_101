pet_1 = {
    'kind_of_animal': 'dog',
    'owner_name': 'alice'
}

pet_2 = {
    'kind_of_animal': 'cat',
    'owner_name': 'bob'
}

pet_3 = {
    'kind_of_animal': 'parrot',
    'owner_name': 'charlie'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\nHere is what I know about {pet['owner_name'].title()}'s pet:")
    
    for key, value in pet.items():
        formatted_key = key.replace('_', ' ').title()
        print(f"  {formatted_key}: {value.title()}")