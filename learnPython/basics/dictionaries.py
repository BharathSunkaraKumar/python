# alien_0 = {'color': 'green', "points": 5}
# print(f"before {alien_0}")
# new_points = alien_0['points'] = 6
# alien_0['x_postion'] = 0
# alien_0['y_postion'] = 25
# print(new_points)
# print(f"after{alien_0}")

# alien_1 = {}
# alien_1['color'] = 'red'
# alien_1['points'] = 10
# print(f"This alien color is {alien_1['color']}")
# alien_1['color'] = 'blue'
# print(f"This alien color is now {alien_1['color']}")

alien_2 = {'x-position': 0, 'y-postion': 25, 'speed': "fast"}
print(f'original postion {alien_2['x-position']}')

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_2['x-position'] = alien_2['x-position'] + x_increment

print(f'new position: {alien_2['x-position']}')
print(alien_2)
alien_2['points'] = 25
print(alien_2)
del alien_2['points']
print(alien_2)


favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'javascript',
    # "bharath": 'mern'
}

language = favorite_languages['edward']
print(language)
print(f"edward's favorite language is {language}" )
point_value = favorite_languages.get('bharath', 'bharath not assigned')
print(point_value)

