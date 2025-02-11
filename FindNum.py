x_s = abs(int(input("Enter a Number:")))
print(type(x_s))
i=0
x = x_s
while x>1:
    x = x/2
    i = i+1
print("It has taken ", i, "loops to halve it")
print("The binary form of", x_s, "is", bin(int(x_s)))
