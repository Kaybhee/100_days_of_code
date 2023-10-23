import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','L','M','N','o','p','q','r','s','t','u','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5', '6','7','8','9','10']
symbols = ['!','+', '#', '$','%','&','*','(',')']
print("Welcome to the pypassword generator")
work1 = int(input("How many letters would you like in your password?\n"))
work2 = int(input("How many numbers would you like?\n"))
work3 = int(input("How many symbols would you like?\n "))
password = [ ]
#for i in range(1 , work1 + 1):
   # random_letters = random.choice(letters)
    #password += random_letters
#for i in range(1, work2 + 1):
    #random_numbers = random.choice(numbers)
    #password += random_numbers
#for i in range(1, work3 + 1):
   # random_symbols = random.choice(symbols)
   # password += random_symbols
    #print(password)
for i in range(1, work1 +1):
    random_letters = random.choice(letters )
    password += random_letters
        #The extend function only work for a list(+=)
for i in range(1, work2 + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers
for i in range(1, work3 + 1):
   random_symbols = random.choice(symbols)
   password += random_symbols
   random.shuffle(password)
password_str = " "
for i in password:
    password_str += i
print(f"The password is : {password_str}")