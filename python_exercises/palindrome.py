# Write a program to check if the given number is a palindrome number.
def palindrome(number):
    print(f'Original number: {number}')
    new_number = ''
    first = number[0]
    middle = number[1]
    last = number[-1]
    new_number += last + middle + first
    if number == new_number:
        print('Yes.given number is palindrome number')
    else:
        print('No. given number is not palindrome number')


print(palindrome(str(input('Enter a number you think is a palindrome: '))))

