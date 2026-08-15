# 1. Number Pattern
print("Number Pattern:")

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()


# 2. Alphabet Pattern
print("\nAlphabet Pattern:")

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


# 3. Star Pattern
print("\nStar Pattern:")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()