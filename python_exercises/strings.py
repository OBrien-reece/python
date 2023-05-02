# Write a program to accept a string from the user
# and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

word = input('Enter a word: ')


for item in range(0, len(word)-1, 2):
    print(word[item])


