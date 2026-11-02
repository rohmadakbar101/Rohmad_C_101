developers = {
    'jen': {
        'language': 'python',
        'experience_years': 4,
        'role': 'data scientist'
    },
    'sarah': {
        'language': 'c',
        'experience_years': 10,
        'role': 'embedded systems engineer'
    },
    'edward': {
        'language': 'rust',
        'experience_years': 2,
        'role': 'backend developer'
    },
    'phil': {
        'language': 'python',
        'experience_years': 8,
        'role': 'machine learning engineer'
    }
}

print("---  DEVELOPER PROFILES  ---\n")

for name, info in developers.items():
    print(f"Name: {name.title()}")
    
    role = info['role'].title()
    language = info['language'].title()
    experience = info['experience_years']
    
    print(f"  ├─ Role       : {role}")
    print(f"  ├─ Language   : {language}")
    print(f"  └─ Experience : {experience} years\n")