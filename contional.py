name = input("Enter name: ")

if len(name) < 3:
    print("Name must be atleast 3 charecters")
elif len(name) >= 15:
    print("Name can be maximum 15 charecters")
else:
    print("Name looks good!")


houseRate = 10000000
heHasGoodCredit = False

if heHasGoodCredit:
    print(houseRate*0.10)
else:
    print(houseRate*0.20)