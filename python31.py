def reverse_value(value):
    return value[::-1]

# Get value from user
value = input("Enter a value: ")

# Function call
result = reverse_value(value)

print("Reversed value =", result)