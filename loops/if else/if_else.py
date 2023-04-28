# # is_rainy = input('Answer True/False, Is it raining? ')
# # is_rainy = bool(is_rainy)
# is_rainy = False
# is_hot = True
#
# if is_rainy:
#     print('Please wear a raincoat for your trip')
# elif is_hot:
#     print('Today will be hot, I`d advice going to the beach')
# else:
#     print('Wear lightly today')

# Exercise
# Price of a house is $1M
# If a buyer has good credit
# they need to put down 10%
# otherwise
# they need to put down 20%
# Print the down payment

morgage = 1000000
buyer = input("What is the Buyer's name? ")
has_good_credit = input(f'Does {buyer} have good credit? True/False ')
# has_good_credit = bool(has_good_credit)
has_good_credit = has_good_credit.lower() == 'true'

if has_good_credit:
    print('''
    It has been affirmed that {} has good credit
    He therefore stands a 10% down-payment of all goods    
    His down-payment therefore amounts to ${}
    '''.format(buyer, morgage*0.1))
else:
    print(''''
    It has been affirmed that {} has bad credit
    He therefore stands a 20% down-payment of all goods
    His down-payment therefore amounts to ${}
    '''.format(buyer, morgage * 0.2))

# input() function returns a string,
# and in Python, a non-empty string is considered True.
# This means that when you convert the input to a boolean
# using the bool() function, it will always evaluate to
# True if the string is not empty, regardless of its content.
