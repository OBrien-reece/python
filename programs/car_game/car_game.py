# Car start game
# type help to bring out the help commands
# start to start
# stop to stop
# quit to stop the program
# any other command will make the program state that it doesn't understand

command = ''

while command[0:] != 'quit':
    command = input('> ')
    if command[0:] == 'help':
        print('''
            start - start the car
            stop - stop the car
            quit - quit the program
        ''')
    elif command[0:] == 'start':
          print('> start the car')
    elif command[0:] == 'stop':
        print('> stop the car')
    elif command[0:] == 'quit':
        break
    else:
        print('I do not understand...')

