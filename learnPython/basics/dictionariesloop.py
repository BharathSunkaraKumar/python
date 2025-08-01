user = {
    'fname': 'bharath',
    'lname': 'kumar',
    'city': 'tirupati',
}
# print(user)
# for key, value in user.items():
    # print(f'key:{key}\nvalue:{value}')

favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'javascript',
    "bharath": 'react',
    "iyer" : 'python'
}

friends = ['bharath', 'sarah']
# for name,language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")
for name in favorite_languages.keys():
    print(f"Hello, {name.title()}'s")
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, i see you love {language}')

for name in sorted(favorite_languages.keys()):
    print(f'sorted list {name}')

for language in favorite_languages.values():
    print(language.title())

for name in set(favorite_languages.values()):
    print(f'set list {name}')

user1 = {
    'fname': 'bharath',
    'lname': 'kumar',
    'city': 'tirupati',
}
 
user2 = {
    'fname': 'subhman',
    'lname': 'gill',
    'city': 'Punjab',
}
 
user3 = {
    'fname': 'kl',
    'lname': 'rahul',
    'city': 'bangalore',
}

users = [user1, user2, user3]
for user in users:
    print(user)
 
