# 1) dict()
d = dict(name="Sumit", age=18, course="BCA")
print("1. dict():", d)

# 2) len()
print("2. len():", len(d))

# 3) clear()
temp = d.copy()
temp.clear()
print("3. clear():", temp)

# 4) get()
print("4. get('name'):", d.get("name"))

# 5) pop()
temp = d.copy()
print("5. pop('age'):", temp.pop("age"))
print("   Dictionary after pop():", temp)

# 6) popitem()
temp = d.copy()
print("6. popitem():", temp.popitem())
print("   Dictionary after popitem():", temp)

# 7) keys()
print("7. keys():", d.keys())

# 8) values()
print("8. values():", d.values())

# 9) items()
print("9. items():", d.items())

# 10) copy()
d2 = d.copy()
print("10. copy():", d2)

# 11) update()
d.update({"city": "Jamnagar", "age": 19})
print("11. update():", d)