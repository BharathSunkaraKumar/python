# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1

prompt = '\nenter somting i will repeat it back to you:'
prompt += "\nenter 'quit' to end the program. "

message = ""
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)