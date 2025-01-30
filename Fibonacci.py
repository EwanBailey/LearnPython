fibonacci = [0, 1]

for i in range(10):
    x = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(x)
print(fibonacci)
