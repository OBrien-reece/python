# Check if the first and last number of a list is the same
def comparison(numbers):
    print(f'Given list: {numbers}')

    first = numbers[0]
    last = numbers[len(numbers_y)-1]
    if first == last:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(comparison(numbers_x))
print(comparison(numbers_y))