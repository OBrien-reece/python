phone = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}
num = input('Phone: ')

output = ''
for number in num:
    output += phone.get(number, '!') + ' '
print(output)