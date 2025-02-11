def percent(x):
    x = round(x/100, 2)
    return x

x = abs(float(input("Enter a value to convert to percentage:")))
percent(x)
print("As a percentage, the value is equal to:", x, "%")
