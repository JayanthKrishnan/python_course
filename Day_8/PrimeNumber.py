def prime_checker(number):
    is_prime = True
    for _ in range(2,number):
        if number % _ == 0:
            is_prime = False
    if is_prime:
        print("it's a prime number")
    else:
        print("it's not a prime number")


print("Prime Number Checker")
n = int(input("Enter the number : "))
prime_checker(number=n)
