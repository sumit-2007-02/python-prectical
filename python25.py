def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication


# Function call
result1, result2, result3 = calculate(20, 10)

print("Addition =", result1)
print("Subtraction =", result2)
print("Multiplication =", result3)