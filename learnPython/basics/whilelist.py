uncofirm_Users = ['bharath', 'rohit', 'virat']
confirm_users = []

while uncofirm_Users:
    current_user = uncofirm_Users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirm_users.append(current_user)
for confirm_user in confirm_users:
    print(confirm_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while "cat" in pets:
    pets.remove('cat')

print(pets)
