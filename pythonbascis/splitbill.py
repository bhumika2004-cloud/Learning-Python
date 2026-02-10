# get input value for total number of friends 
total_friends=int(input('Enter total number of friends'))

# get input value for bill 
bill=int(input('Enter the amount for resturant bill'))

# calculate the tax amount
tax_amount=(20/100)*bill

# divide the total bill among friends
total_bill= bill + tax_amount
split_amount= (total_bill)/(total_friends)

# print the split amount
print(split_amount)
