while True:
    
    user_input = input("Enter a number:")
    
    try:
        x = float(user_input)
        
        if(x>5):
            print (x,"is greater than 5")
        elif(x<5):
            print (x,"is less than 5")
        elif(x==5):
            print (x,"is equal to 5")
            
    except:
        print ("x is not a number")

# Helpful Page:
# https://www.w3schools.com/python/python_conditions.asp
