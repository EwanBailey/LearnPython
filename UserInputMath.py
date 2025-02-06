while True:
    try:
        user_number = int(input("Please enter an integer greater than 20: "))
        if user_number > 20:
            break
        else:
            print("The number must be greater than 20.")
    except ValueError:
        print("That's not a valid number.")

count = 0

while user_number > 1:
    user_number //= 2
    print(user_number)
    count += 1
    print("The loop has cycled", count, "times")

print("The while loop cycled a total of", count, "times")
