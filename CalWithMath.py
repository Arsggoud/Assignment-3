import math

number = float(input("Enter a number: "))


square_root = math.sqrt(number)

if number > 0:
    natural_log = math.log(number)
else:
    natural_log = "log only works for positive numbers"

sine_value = math.sin(number)

print(f"Square root: {square_root}")
print(f"Natural logarithm: {natural_log}")
print(f"Sine (in radians): {sine_value}")
