favorite_languages = {
    'al': 'python',
    'akbar': 'c',
    'naufal': 'rust',
    'iyan': 'python',
}

people_to_poll = ['al', 'josh', 'akbar', 'lucy', 'naufal', 'iyan']

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you for responding to our poll, {person.title()}!")
    else:
        print(f"{person.title()}, we invite you to take our favorite languages poll!")