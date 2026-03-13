# create the class
class Square:

    # define the __init__() method
    def __init__(self,length):
        self.length=length
  
    # define the compute_area() method
    def compute_area(self):
        return length*length
    
    # define the compute_perimeter() method
    def compute_perimeter(self):
        return 4*length


# get integer input
length = int(input())

# create an object of Square    
sq=Square(length)

# call compute_area() and print the area
area=sq.compute_area()
print(area)

# call compute_perimeter() and print the perimeter
perimeter=sq.compute_perimeter()
print(perimeter)
