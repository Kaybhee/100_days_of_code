Year = int(input("Which year do you want to check?\n"))
if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else: 
        print("leap year")               
else:
    print("Not a leap year")