# Iterate the given list of numbers and print only
# those numbers which are divisible by 5
def divisible(numbers):
    print(f'Given the list {numbers}')
    for number in numbers:
        if number % 5 == 0:
            print(number)


numbers = [10, 20, 33, 46, 55]
print(divisible(numbers))


