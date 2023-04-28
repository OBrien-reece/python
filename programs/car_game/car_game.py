# Car start game
# type help to bring out the help commands
# start to start
# stop to stop
# quit to stop the program
# any other command will make the program state that it doesn't understand

command = ''
status = 'idle'

while True:
    command = input('> ').lower()
    if status == 'started' and command[0:] == 'start':
        print('The car is already started')
    elif status == 'stopped' and command[0:] == 'stop':
        print('The car is already stopped')

    elif command[0:] == 'help':
        print('''
                start - start the car
                stop - stop the car
                quit - quit the program
        ''')
    elif command[0:] == 'start' and status == 'idle':
          status = 'started'
          print('> You have started the car')
    elif command[0:] == 'stop' and status == 'idle':
        status = 'stopped'
        print('> You have stopped the car')
    elif command[0:] == 'quit':
        print('> You have opted to quit the session')
        break
    else:
        print('I do not understand...')

