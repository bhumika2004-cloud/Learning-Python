# define a function named find_sum()
def find_sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
number = int(input())

# call the function and print the return value
result=find_sum(number)
print(result)
