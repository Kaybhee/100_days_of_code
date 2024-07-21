def add_binary(num1, num2) :
    num  = num1 + num2
    bin_num = bin(num)[2:]
    return bin_num
num1 = int(input("first number: "))
num2 = int(input("second number: "))

total = add_binary(num1, num2)
print(total)
