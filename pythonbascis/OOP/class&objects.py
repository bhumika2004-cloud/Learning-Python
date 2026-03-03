
# create the person class
class Person:
    # create the greet() method
    def greet(self,message):
        print(message)

# get user input
greeting = input()

# create object
person1 = Person()

# call the greet() method using person1
# use greeting as an argument
person1.greet(greeting)
