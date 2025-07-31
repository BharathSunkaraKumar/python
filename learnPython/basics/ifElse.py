# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# print('--------')
# age = 18
# if (age>21) or (age<20):
#     print(age)

# bmw = 'bmw' in cars
# print(bmw)

# audi = 'audi'
# if audi not in cars:
#     print('audi not in cars')
# else:
#     print('audi in cars')

# banned_users = ['andrew', 'carolina', 'david']
# user = 'danger dilli'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")

# car = 'bmw'
# if car == 'bmw':
#     print("I predict True")
# else:
#     print("I predict False")

age = 5

if age < 4:
    print('your admission cost is $0')
elif age < 18:
    print('your admission cost is $25')
else:
    print('your admission cost is $40')

age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"your admission cost is ${price}")

