# Get input from the user
n = int(input("Enter a positive integer: ")) #7

# Initialize variables
sum = 0
i = 1

# Calculate sum using while loop
while i <= n:
    sum = sum + i # 0 + 1 = 1
    i += 1 # 1 + 1 = 2 

# Print the result
print(f"The sum of numbers from 1 to {n} is: {sum}")