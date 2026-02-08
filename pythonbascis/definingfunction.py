def compute_factorial(n):
    total=1
    for n in range(1,number+1):
        total=total*n
    return total
# Get the user input
number = int(input("Enter a positive integer: "))
    
    

total=compute_factorial(number)
print(total)
