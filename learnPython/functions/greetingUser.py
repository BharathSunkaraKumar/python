def greet_user(user):
    # print(f"hello! {user.title()}")
    return user
print(greet_user("water white"))

def describe_pet(animal_type, pet_name):
    print(f'\n i hvae a {animal_type}')
    print(f"\n my {animal_type}'s name is {pet_name}")
describe_pet('hamster', 'harry')
describe_pet('dog', 'budda')

def formated_name(first, last):
    full_name = f"{first} {last}"
    return full_name
developer = formated_name('bharath', 'kumar')
print(developer)

def build_person(first, last, age=None):
    person = {"firstName": first, "lastName":last}
    if age:
        person['age'] = age
    return person
details = build_person('virat', "kohli", age=37)
print(details)
