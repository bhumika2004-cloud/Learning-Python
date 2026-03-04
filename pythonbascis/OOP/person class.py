class Person:
    def __init__(self):
        self.name = input('Enter name: ')
        self.age = int(input('Enter age: '))
    
    def display_info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')

person1 = Person()
person1.display_info()

person2 = Person()
person2.display_info()
