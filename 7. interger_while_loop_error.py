def ask():
    # Waiting for the correct response
    waiting = True
    while waiting:
        try:
            n = int(input('Enter a number: '))
        except:
            print('Please try again: ')
            continue
        else:
           waiting = False 
    print('Your number squared is: ')
    print(n**2)

ask()
