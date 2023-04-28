# Write a program to remove the duplicates in a list
numbers = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,0,0,0]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
