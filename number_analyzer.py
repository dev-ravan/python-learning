number = int(input("Enter the number:"))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if number % 5 == 0:
    print("The number is multiple of 5.")
else:
    print("The number is not a multiple of 5.")