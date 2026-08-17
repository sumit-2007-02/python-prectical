my_dict = {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40
}

total = 0

for value in my_dict.values():
    total = total + value

print("Dictionary:", my_dict)
print("Sum of all values =", total)