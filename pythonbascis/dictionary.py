
# get integer input
n = int(input())

# create the dictionary using comprehension
numbers = { i : i*10 for i in range(1,n+1) if i>=3}

print(numbers)
