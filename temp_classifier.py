# Get temprature from the user
temp = float(input("Enter temprature: "))

if temp < 0:
    print("It's freezing!")
elif temp < 10:
    print("It's cold!")
elif temp < 20:
    print("It's a bit chilly!")
elif temp < 28:
    print("It's warm!")
else:
    print("It's a bit hot!")