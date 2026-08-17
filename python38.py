my_dict = {
    'A': 50,
    'B': 20,
    'C': 40,
    'D': 10,
    'E': 30
}

# Ascending order
ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# Descending order
descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Ascending Order:", ascending)
print("Descending Order:", descending)