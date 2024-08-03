weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if(unit.upper() == "L"):
    kilograms = int(weight) * 0.454
    print(f"You're {kilograms} kg")
elif(unit.upper() == "K"):
    pounds = int(weight) // 0.454
    print(f"You're {pounds} pounds")
else:
    print("You entered a wrong key!!")