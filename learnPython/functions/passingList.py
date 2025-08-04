# def greet_User(names):
#     for name in names:
#         print(name)
# greet_User(['bharath', 'mr.white', 'jessi'])

def make_pizza(inch,*toppings):
    print(f"\nmaking a {inch}-inch pizza with following toppings")
    for topping in toppings:
        print(f'-{topping}')
make_pizza(16,'mushrooms', 'green peppers')