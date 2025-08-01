person = {
    "firstName": 'bharath',
    "lastName": "Kumar",
    "age": 26,
    "city": 'tirupati',
}
# print(person['firstName'])
# print(person['lastName'])
# print(person['age'])

favoriteNumber = {
    'bharath': 3,
    'virat': 18,
    'dhoni': 7,
    'kl rahul': 1,
    'shubman gill': 77
}
# print(f"shubman gill's favroite number is {favoriteNumber['shubman gill']}.")

glossary = {
    'forloop' : 'loop item',
    "list": 'list is a collection of data',
    "tuple": "tuple is looks like list but using paranteses instead of using square brackets",
    "dictionaries": 'like objects in javascript',
    "ifelse": 'condion statements'
}

print(f'forloop\n{glossary["forloop"].title()}')
print(f'list\n{glossary["list"]}')
print(f'tuple\n{glossary["tuple"]}')
print(f'dictionaries\n{glossary["dictionaries"]}')
print(f'ifelse\n{glossary["ifelse"]}')
