while True:
    
    user_input = input("Guess the number:")
    
    try:
        x = float(user_input)
        
        if(x!=5):
            print (x,"is not the number...")
        elif(x==5):
            print (x,"is the number!!!")
            
    except:
        print ("that is not a valid guess")
