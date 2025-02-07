while(True):

    try:
        x = int(input("Pick a number 0 through 9:"))
    
        if 0 < x < 9:
            break
    
        else:
            print("The number must be between 0 and 9.")
    
    except ValueError:
        print("That is not a valid number.")
        
count = 0
while(count != x):
    print(count)
    count = count + 1
    
if(count == x):
    print("The count variable and the Input are identical")
