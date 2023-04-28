# if name is less than three characters long
#     name must be at least 3 characters
# otherwise if it is more than 10 characters long
#     name can be a maximum of 10 characters
# otherwise
#     name looks good

name = input('What is your name? ')

if len(name) < 3:
    print('The name you have entered is to short')
elif len(name) > 10:
    print('The name entered is too long. Please review it')
else:
    print(f'Hello {name}. Welcome to Python Programming')