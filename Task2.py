#ask to user for number as input
num = int(input("Enter a number: "))
#Uses the math module to calculate the:
#o   Square root of the number
#o   Natural logarithm (log base e) of the number
#o   Sine of the number (in radians)
import math
sqrt_result = math.sqrt(num)
log_result = math.log(num)
sin_result = math.sin(num)
print("Square root of", num, "is", sqrt_result)
print("Natural logarithm of", num, "is", log_result)
print("Sine of", num, "is", sin_result) 