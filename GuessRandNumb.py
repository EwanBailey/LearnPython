import random
# Random library is needed for this code
while True:
    print("Welcome to the game!")
    user_input = input("Guess the number:")
    
    try:
        x = float(user_input)
        y = (random.randint(0, 5))
        # Generates the two numbers
        if(x!=y):
            print (x,"is not the number...")
        elif(x==y):
            print (x,"is the number!!!")
        # Compares the numbers and displays if it is correct
    except:
        print ("that is not a valid guess")
