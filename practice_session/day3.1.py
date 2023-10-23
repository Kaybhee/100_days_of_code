print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height > 120 :
    print("You can ride the roller coaster!")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill = 4
        print("Children ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Teenagers bill is $7.")
    else:
        bill = 8
        print("please pay premium of $12.")
#For a roller coaster pics is needed
    want_photo = input("Do you want a photo: Y or N?\n")
    if want_photo == "Y":
        #Add $3 to their bill
    #increment bill by $3
        bill += 3
        print(f"Your final bill is ${bill}")

else:
    print("You need to grow taller before you can ride!")

    

    
    
    