# Given a two list of numbers, write a program to create
# a new list such that the new list should contain odd
# numbers from the first list and even numbers from the second list.
def odd_even(first, second):
    result_list = []
    for item in first:
        if item % 2 == 1:
            result_list.append(item)
    for item in second:
        if item % 2 == 0:
            result_list.append(item)
            
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(odd_even(list1, list2))