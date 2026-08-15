# 1. Creating an empty dictionary
dict1 = {}
print("1. Empty Dictionary:", dict1)

# 2. Creating a dictionary with key-value pairs
dict2 = {"name": "Sumit", "age": 18, "course": "BCA"}
print("2. Dictionary with key-value pairs:", dict2)

# 3. Creating a dictionary using dict() constructor
dict3 = dict(name="Rahul", age=20, city="Rajkot")
print("3. Using dict() constructor:", dict3)

# 4. Creating a dictionary using a list of tuples
dict4 = dict([("a", 10), ("b", 20), ("c", 30)])
print("4. From list of tuples:", dict4)

# 5. Creating a dictionary using zip()
keys = ["name", "age", "city"]
values = ["Amit", 21, "Jamnagar"]

dict5 = dict(zip(keys, values))
print("5. Using zip():", dict5)

# 6. Creating a dictionary using fromkeys()
keys = ["a", "b", "c"]
dict6 = dict.fromkeys(keys, 0)
print("6. Using fromkeys():", dict6)

# 7. Creating a nested dictionary
dict7 = {
    "student1": {"name": "Raj", "age": 20},
    "student2": {"name": "Jay", "age": 21}
}
print("7. Nested Dictionary:", dict7)