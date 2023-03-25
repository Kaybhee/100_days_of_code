def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def power(n1, n2):
    return n1 ** n2
def divide(n1, n2):
    return n1 / n2
operators = { "+" : add,
             "*" :  multiply,
             "/" : divide,
             "**" : power
            }

def calculator():
    n1 = float(input("Enter the first number: "))
    want_continue = False
    for symbols in operators:
        print(symbols)
 
    while not want_continue:
        symbols = input("Choose an operation: ")
        cal_symbol = operators[symbols]
        n2 = float(input("Enter the next number: "))
        cal_value = cal_symbol(n1, n2)
        print(f"{n1} {symbols} {n2} = {cal_value}")

        should_continue = input("Would you like to continue, type 'y' for yes and 'n' for no: ")
        if should_continue == "y":
            n1 = cal_value
        else:
            #To make it recursive when it is passed no and it restarts the operation.
            calculator()

calculator()
