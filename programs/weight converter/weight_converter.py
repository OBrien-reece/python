# User enters weight
# Ask whether it is in pounds or KGs
# Then convert it to either pounds or Kgs depending on the input

weight = input('What is your weight? ')
unit = input('Is it (L)bs or (K)g? ')
unit = unit.lower()

if unit == 'l':
    print('Your weight in kilograms is {} kgs'.format(round(int(weight) / 2.20462)))
elif unit == 'k':
    print('Your weight in pounds is {} pounds'.format(round(int(weight) * 2.20462)))
else:
    print('Please enter a weight class')