print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want: S, M, L?\n")
add_pepperoni = input("Do you want pepperoni: Y or N?\n")
extra_cheese = input("Do you want extra cheese: Yor N?\n")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    size == "L"
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 3
    else:
        bill +=5
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")
