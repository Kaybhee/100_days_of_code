def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2
def power(n1, n2):
    return n1 ** n2
"""To create a dictionary to contain the operators"""
operators = {"+": add,
             "-": subtract,
             "*": multiply,
             "**": power,
             "/": division}
want_continue = False
for symbol in operators:
    print(symbol)
while not want_continue:
    n1 = int(input("Enter the first number: "))
    symbol = input("Choose from the symbols above: ")
    Total_cal = operators[symbol]
    n2 = int(input("Enter the second number: "))
    answer = Total_cal(n1, n2)
   
    # print(f"{n1} {symbol} {n2} = {Total_cal(n1, n2)}")
    # symbol = input("Choose another symbol: ")
    # another_cal = operators[symbol]
    # n3 = int(input("Enter another number: "))
    print(f"{n1} {symbol} {n2} = {answer}")

    if input("Type 'y' to continue calculating with {answer}, or type 'n' to exit: " ) == "y":
        n1 = answer
    else:
        want_continue = True




     

