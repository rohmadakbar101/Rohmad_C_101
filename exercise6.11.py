cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_929_286,
        'fact': 'It is the most populous metropolitan area in the world.'
    },
    'paris': {
        'country': 'france',
        'population': 2_161_000,
        'fact': 'It is often referred to as the City of Light.'
    },
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'fact': 'The Andes mountains can be seen from almost anywhere in the city.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    
    country = info['country'].title()
    population = info['population']
    fact = info['fact']
    
    print(f"  Country: {country}")
    print(f"  Population: {population:,}")
    print(f"  Fact: {fact}")