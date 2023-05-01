# define a new type Person
# should have a name attribute and a talk() method

class Person():

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hello {self.name}. Pleased to meet you')


person = Person(input('What is your name: '))
person.talk()


