import random

for item in range(10):
    current_number = random.randint(0, 10)
    previous_number = random.randint(0, 10)
    print(f'Current Number: {current_number} Previous Number: {previous_number} Sum: {current_number+previous_number}')


