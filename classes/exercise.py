# define a new type Person
# should have a name attribute and a talk() method

class Person():

    def __init__(self, name):
        self.name = name
    def talk(self):
        return input('Say Something: ')


person = Person(input('Whats your name: '))
print(f'Hello {person.name}. Did you say, {person.talk()} ?')
