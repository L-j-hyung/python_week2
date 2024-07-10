def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number = 5
fact = factorial(number)
print(fact)