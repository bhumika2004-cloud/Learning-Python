def print_items(*items):
    # use a for loop to print individual items of the argument
    total=0
    for item in items:
        print(item)

# take two string inputs
text1 = input()
text2 = input()

# call print_items with text1 as argument
print_items(text1)

# call print_items with text1 and text2 as arguments
print_items(text1,text2)
