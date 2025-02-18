# Calculate the factorial of a number


def factorial(n):
    # Your code here
    pass  # Implement the function


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
