def factorial(x):
    if x == 0 or x == 1:
        return 1
    r = range(x, 1, -1)
    res = 1
    for i in r:
        res *= i
    return res


# Calculate the factorial of a number
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
