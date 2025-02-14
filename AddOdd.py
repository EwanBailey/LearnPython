a = int(input("Value for A:"))
b = int(input("Value for B:"))

def add_or_odd(a, b):
    num = a + b
    return num if num % 2 == 0 else num + 1

print(add_or_odd(a,b))
