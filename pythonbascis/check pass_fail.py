# define a function named check with argument marks
def check(marks):
    # inside the function, check Pass or Fail using if...else statement
    if marks>40:
        return 'Pass'
    else:
        return 'Fail'

marks = int(input())

#call the function
result= check(marks)
print(result)
