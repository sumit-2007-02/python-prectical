# 1) list()
a = list((10, 20, 30))
print("1. list():", a)

# 2) len()
print("2. len():", len(a))

# 3) count()
a = [10, 20, 10, 30, 10]
print("3. count(10):", a.count(10))

# 4) index()
print("4. index(20):", a.index(20))

# 5) append()
a.append(40)
print("5. append(40):", a)

# 6) insert()
a.insert(1, 15)
print("6. insert(1, 15):", a)

# 7) extend()
a.extend([50, 60])
print("7. extend([50, 60]):", a)

# 8) remove()
a.remove(15)
print("8. remove(15):", a)

# 9) pop()
a.pop()
print("9. pop():", a)

# 10) reverse()
a.reverse()
print("10. reverse():", a)

# 11) sort()
a.sort()
print("11. sort():", a)

# 12) copy()
b = a.copy()
print("12. copy():", b)

# 13) clear()
a.clear()
print("13. clear():", a)