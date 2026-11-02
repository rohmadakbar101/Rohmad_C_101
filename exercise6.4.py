glossary = {
    'variable': 'A named placeholder for storing data.',
    'string': 'A series of characters.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'boolean': 'A value that is either True or False.',
    'tuple': 'An immutable list.',
    'set': 'A collection in which each item must be unique.',
    'float': 'A numerical value with a decimal component.',
    'integer': 'A whole number.',
    'loop': 'Work through a collection of items, one at a time.'
    }

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")