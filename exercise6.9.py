favorite_places = {
    'akbar': ['solo', 'klaten', 'pacitan'],
    'naufal': ['sokaraja'],
    'al': ['blok m', 'jakarta']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    
    for place in places:
        print(f"  - {place.title()}")