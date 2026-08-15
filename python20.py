t = (10, 20, 30, 20, 40, 50)

# 1) len()
print("1. len():", len(t))

# 2) count()
print("2. count(20):", t.count(20))

# 3) index()
print("3. index(30):", t.index(30))

# 4) sorted()
print("4. sorted():", sorted(t))

# 5) min()
print("5. min():", min(t))

# 6) max()
print("6. max():", max(t))

# 7) cmp()
def cmp(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

print("7. cmp(10, 20):", cmp(10, 20))
print("   cmp(20, 20):", cmp(20, 20))
print("   cmp(30, 20):", cmp(30, 20))

# 8) reversed()
print("8. reversed():", tuple(reversed(t)))