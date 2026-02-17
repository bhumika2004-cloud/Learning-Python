# create compute_area() function that
# computes area and returns it
def compute_area(radius,pi):
    Area=3.14*radius*radius
    return Area
# take float input and store it in radius variable
radius=float(input('enter radius'))

# assign value 3.14 to pi variable
pi=3.14

# call compute_area() with arguments radius and pi
result=compute_area(radius,pi)

# print returned value
print(result)
