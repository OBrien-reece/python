try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('Cannot square a string')
