# Get input from the user
n = int(input("Enter a positive integer: "))

# Initialize variables
sum = 0
i = 1

# Calculate sum using while loop
while i <= n:
    sum += i
    # i += 1

# Print the result
print(f"The sum of numbers from 1 to {n} is: {sum}")