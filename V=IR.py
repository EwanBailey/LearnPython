x = float(input("Value for Volts:"))
y = float(input("Value for Milliamps:"))
r = x / (y*1000)
print("The required resistor is", r, chr(0x2126))
