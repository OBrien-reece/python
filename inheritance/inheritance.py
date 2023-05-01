class Mammal:
    def xtics(self):
        print('Has mammary glands')


class Dog(Mammal):
    def bark(self):
        print('Barks')


class Cat(Mammal):
    pass


animal = Dog()
print(animal.xtics(), animal.bark())