# take float input for salary
salary=float(input('Enter salary'))

# take integer input for years
years=int(input('Years of work'))

# check if years worked is greater than 5 or not
if(years>5): 
    # calculate bonus using 5 * salary / 100
    bonus= 5*(salary/100)
    # print bonus
    print(bonus)
