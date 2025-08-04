
responses = {}

polling_active = True

while polling_active:
    name = input('\n what is you name? ')
    response = input('which program would you like to learn? ')
    responses[name] = response

    repeat = input('would to like to let another person respond? (yes/no): ')
    if repeat == 'no':
        polling_active = False
    
print('\n---poll results---')

for name, response in responses.items():
    print(f"{name} would like to learn {response}")