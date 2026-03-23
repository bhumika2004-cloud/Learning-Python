# create a try block
try:
    # take input for numerator
    numerator = int(input())
    # take input for denominator
    denominator = int(input())

    # Divide numerator by denominator and print the result
    result=numerator/denominator
    print(result)

# create the except block
except:
    if denominator==0:
        print('Denominator cannot be 0. Try again.')
