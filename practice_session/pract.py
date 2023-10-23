# str1 = "Holberton"
# str2 = "School"
# str1 += " " + str2
# print(f"Welcome to {str1}!")
#!/usr/bin/python3
# word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
# print(f"First 3 letters: {word[:3]}")
# print(f"Last 2 letters: {word[7:]}")
# print(f"Middle word: {word[1:8]}")
#!/usr/bin/python3
# str = "Python is an interpreted, interactive, object-oriented programming\
#  language that combines remarkable power with very clear syntax"
# str = str[39:66] + str[106:112] + str[:6]
# print(str)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print(f"{num} is an even number", num)
        continue
    print("Found an odd number", num)

# pip install pycodestyle
# $ pip install --upgrade pycodestyle
# $ pip uninstall pycodestyle
# import random
# number = random.randint(-10, 10)
# if number > 0:
#     print(f"{number} is positive")
# elif number < 0:
#     print(f"{number} is negative")
# else:
#     print(f"{number} is zero")
######Another one
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# lastDigit = 0

if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = (-number % 10) * -1

message = f"Last digit of {number} is {lastDigit}"

if lastDigit == 0:
    print(f"{message} and is 0")
elif lastDigit > 5 and lastDigit % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
        

# Last digit of 4205 is 5 and is less than 6 and not 0
#!/usr/bin/python3
for char in range(26):
    if char!= 4 and char != 16:
      print("{:s}".format(chr(char + ord("a"))), end="")
####To print Hex
for num in range(99):
    print("{:d} = {:s}".format(num, hex(num)))

####
#!/usr/bin/python3
# for i in range(100):
#     if i == 99:
#         print(i)
#     else:
#         print("{}".format('0' + str(i) if i < 10 else i), end=", ")
# #####

# now = date.today()
# now
# datetime.date(2003, 12, 2)
# now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# # dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# age.days


#!/usr/bin/python3
def add(a, b):
    a = 1
    b = 2
add()
    # print("{} + {} = {}".format(a,b, add(a,b)))

