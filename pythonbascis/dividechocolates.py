# take two integer inputs for chocolates and children
chocolates=int(input("Enter no of chocolates"))
children=int(input("Enter no of childrens"))

# find chocolates each children will get and and print it
cpc=(chocolates)/(children)
rc=(chocolates)%(children)

# find remaining chocolates and print it
print(int(cpc))
print(rc)
