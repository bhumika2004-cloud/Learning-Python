# get two integers from user
num1 = int(input())
num2 = int(input())

# create a function my_function that accepts are two arguments arg1 and arg2
def my_function(num11,num2):

    # compare arg1 and arg2 to see if they are equal
    if num1==num2:
        return True
    else:
        return False

# call the function and pass the parameters
result=my_function(num1,num2)
print(result)
