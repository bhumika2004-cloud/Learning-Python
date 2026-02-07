countdown = int(input("Enter starting countdown number: "))
elapsed = 0
while countdown>=0:
    
    # Show how much time is left
    print(f"Time left: {countdown} seconds")
    
    # Show how much time has passed
    print(f"Elapsed: {elapsed} seconds")
    
    # Print a separator line
    print("---")
    
    # Decrease the countdown by 1
    countdown-=1
    
    # Increase the elapsed time by 1
    elapsed+=1
  print('Liftoff!')
