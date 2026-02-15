# run a while loop that is always True
while(True):
    # take integer input for number 
    number=int(input("Enter a number"))

    # check if user input is less than 0. If yes, skip the number
    if number<0:
        continue

    # check if user input is 0. If yes, terminate the loop
    elif number==0:
        break
  
    # print the number
    else:
        print(number)
