#Task 1: Calculate Factorial Using a Function 
 # Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage
num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of", num, "is", result)