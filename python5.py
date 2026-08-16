# i) Arithmetic Operators
print("I. Arithmetic Operators\n")
a=10
b=5

print("value of a=",a)
print("value of b=",b)
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulus:",a%b)
print("Exponentiation:",a**b)
print("Floor Division:",a//b)

print("*" * 45 + "\n")

# ii) Relational (Comparison) Operators
print("II. Relational (Comparison) Operators\n")

print("value of a:-",a)
print("value of b:-",b)
print("Equal (a==b):",a==b)
print("Not Equal (a!=b):",a!=b)
print("Greater Than (a>b):",a>b)
print("Less Than (a<b):",a<b)
print("Greater Than or Equal (a>=b):",a>=b)
print("Less Than or Equal (a<=b):",a<=b)

print("*" * 45 + "\n")

print("III. Assignment Operators\n")
num = 10
print("Initial value of num:", num)

num += 5
print("After num += 5:", num)

num -= 3
print("After num -= 3:", num)

num *= 2
print("After num *= 2:", num)

num /= 4
print("After num /= 4:", num)

num **= 2
print("After num **= 2:", num)

num //= 3
print("After num //= 3:", num)

print("*" * 45 + "\n")

print("IV. Logical Operators\n")
x, y = True,False

print("x=", x)
print("y=", y)
print("Logical AND (x and y):", x and y)
print("Logical OR (x or y):", x or y)
print("Logical NOT (not x):", not x)
print("Logical NOT (not y):", not y)

print("*" * 45 + "\n")

print("V. Bitwise Operators\n")
p , q = 10, 4

print("p=", p)
print("q=", q)
print("Bitwise AND (p & q):", p & q)
print("Bitwise OR (p | q):", p | q)
print("Bitwise XOR (p ^ q):", p ^ q)
print("Bitwise NOT (~p):", ~p)
print("Bitwise Left Shift (p << 1):", p << 1)
print("Bitwise Right Shift (p >> 1):", p >> 1)

print("*" * 45 + "\n")

print("VI. Ternary Operator\n")
age = 20

status = "Adult" if age >= 18 else "Minor"
print("age:", age)
print("Status:", status)

n1, n2 = 45, 82
max_val = n1 if n1 > n2 else n2
print("n1:", n1)
print("n2:", n2)
print("Maximum of n1 and n2: {}".format(max_val))
print("*" * 45 + "\n")