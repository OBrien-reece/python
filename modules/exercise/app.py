# Create a function find_max() that accepts a list
# then prints out the maximum number from that list
# use modules
import utils
from utils import find_max

numbers = [input('Enter a number: '), input('Enter a number: '), input('Enter a number: '), input('Enter a number: '), input('Enter a number: ')]
maximum = find_max(numbers)
print(maximum)

