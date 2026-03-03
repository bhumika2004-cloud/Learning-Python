# create the class
class Person:
    # create the __init__(self, name) method
    def __init__(self, name, age):
        # create the current_name attribute and assign name to it
        self.current_name=name
        # create the current_age attribute and assign age to it
        self.current_age=age

# create the object with 'Phil' and 19 as argument
person1 = Person('Phil',19)

# print the current_name attribute of person1
print(person1.current_name)

# print the current_age attribute of person1
print(person1.current_age)
