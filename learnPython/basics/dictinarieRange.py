aliens = []

for alien in range(30):
    newAlien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(newAlien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print('....')
print(f"Total number of aliens: {len(aliens)}")
print('....')

pizza = {
    'cust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f'you ordered a {pizza['cust']}-crust pizza with the following toppings')
for topping in pizza['toppings']:
    print('\t' + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")