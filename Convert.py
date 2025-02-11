def convert(x):
    x = x_s
    x = x*27.84
    print(x_s, "United States Dollars Equals", x, "of New Taipei Dollars")

while(True):
    x_s = int(input("Enter amount in USD:"))
    try:
       convert(x_s)
       
    except ValueError:
        print("Please enter a valid amount")
