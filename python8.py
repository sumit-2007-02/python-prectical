print("1. Counting using while loop:")
count = 1
while count <= 5:
    print("Count: {0}".format(count))
    count += 1  

print("-" * 45 + "\n")

print("1. Odd numbers using for loop:")
for i in range(1, 10, 2):
    print(" ",i,end=" ")
print("\n")

n = 5
print("2. Multiplication Table of {0}: using for loop".format(n))
for i in range(1, 11):
    print(" {0} x {1:2d} = {2}".format(n, i, n * i))