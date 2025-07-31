# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
    
#     if requested_topping == 'green peppers':
#         print('sorry, we are out  of green peppers right now.')
#     else:
#         print(f"Adding {requested_topping}")
# print('\nFinished making your pizza!')

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")   
#     print('\nFinished making your pizza!')
# else:
#     print('are you sure you watn a plain pizza')

# available_toppings = ['mushrooms', 'olives', 'green peppers',
#  'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         # print(available_toppings)
#         print(f"adding {requested_topping}")
#     else: 
#         print(f"Sorry, we don;t have {requested_topping}")
    
# print('\nfinished making your pizza')

user_names = ['bharath',  'virat', 'shubman gill', 'shreyas iyer', 'rohit sharma', 'admin']
if user_names:
    for user in user_names:
        if user == 'admin':
            print(f"Hello {user} would you like to see a status report")
        else:
            print(f'Hello {user}, thank you for logging in again')
else: 
    print('we need to find some users!')

curretn_users = ['walter white', 'jesse pinkman', 'hank schrader', 'saul goodman', 'mike', 'gus fring', 'bharath', 'virat']
new_users = ['todd', 'lydia', 'jane', 'hector', 'gale', 'bharath', 'virat']

for newUser in new_users:
    if(newUser in curretn_users):
        print('please enter a new username')
    else:
        print('username is available')

numbers = [1,2,3,4,5,6,7,8,9]
ordinal_Numbers =[]
for number in numbers:
    if number < 2:
        print(ordinal_Numbers.append(f'{number}st'))
    elif number >=2 and number <=2:
        ordinal_Numbers.append(f'{number}nd')
    elif number >=3 and number <=3:
        ordinal_Numbers.append(f'{number}rd')
    else:
        ordinal_Numbers.append(f'{number}th')
print(ordinal_Numbers)
