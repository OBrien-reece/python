print("Hello World")
print('o----')
print(' ||||')

# expression
print('*' * 10)

# Variables

# integer
price = 10
price = 20
# the new value 20 gets printed since the interpreter is
# interpreting the code line by line
print(price)

# boolean
is_published = True
print(is_published)

# float
average = 4.9
print(average)

# Exercise
# We check in a patient named John Smith.
# He is 20 years old and is a new patient
name = 'John Smith'
age = 20
is_new_patient = True
print('Patient name: ' + name + ' Age: ', age, 'New Patient: ', is_new_patient)

# Concatenate with +
# Though Python doesn't implicitly convert objects from one type to another1 in order to make operations "make sense".
# In python + means two tings (Addition and concatenation) depending on where and how it is used
print('Patient name: ' + name + f' Age: {age}')
print('Patient name: ' + name + ' Age: ', age)
