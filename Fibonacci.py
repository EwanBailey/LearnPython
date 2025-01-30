fibonacci = [0, 1]
y = input("How many digits should be calculated?")
variable = int(y)

for i in range(variable):
    x = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(x)
print(fibonacci)
