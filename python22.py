# Create a set
s = {10, 20, 30, 40}
print("Original Set:", s)

# 1) add()
s.add(50)
print("1. add(50):", s)

# 2) update()
s.update([60, 70])
print("2. update([60, 70]):", s)

# 3) copy()
s2 = s.copy()
print("3. copy():", s2)

# 4) pop()
s.pop()
print("4. pop():", s)

# 5) remove()
s.remove(20)
print("5. remove(20):", s)

# 6) discard()
s.discard(30)
print("6. discard(30):", s)

# Create two sets for set operations
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# 7) clear()
temp = s.copy()
temp.clear()
print("7. clear():", temp)

# 8) union()
print("8. union():", a.union(b))

# 9) intersection()
print("9. intersection():", a.intersection(b))

# 10) difference()
print("10. difference():", a.difference(b))