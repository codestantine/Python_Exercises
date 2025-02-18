# de facto solution:
def factor(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


print(factor(6))
print(factor(5))
print(factor(1))
print(factor(0))
print(factor(-1))


# another possible solution
def factorial(x):
    if x == 0 or x == 1:
        return 1
    if x < 0:
        return "Factorial not defined for negative numbers"
    r = range(x, 1, -1)
    factorial_list = list(r)
    res = 1
    for i in factorial_list:
        res *= i
    return res


print(factorial(6))
print(factorial(5))
print(factorial(1))
print(factorial(0))
print(factorial(-1))
