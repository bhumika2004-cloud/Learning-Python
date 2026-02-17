# take string input for check
check=input("Enter a string for checking: ")


# use list index to check if the first and the last character of a string are equal or not
if check[0]==check[-1]:
    print("Equal")
else:
    print("Not Equal")
