course = 'Python course for absolute beginners'

print(len(course))

# find where the character c begins from, from the text and use that to print PYTHON
length = course.find('c')
lang_name = course[:length]

# Replace a character
new_course = course.replace(lang_name, 'Php ')

# print(course.upper())

print(f'{lang_name.upper()} is an amazing language that is why i recommend you watching Mosh`s {course}')
print(f'{new_course} is an amazing language but obsolete that is why i recommend you watching Mosh`s {course}')


print('Python' in course)

