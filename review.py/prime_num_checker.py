def prime_checker(number):
    is_prime_no = True
    for i in range(2, number):
        
        if number %  i == 0:
            is_prime_no = False
    if is_prime_no:
        print("It's a prime number")
    else:
        print("It's not a prime number")
n = int(input("Check this number: "))
prime_checker(n)