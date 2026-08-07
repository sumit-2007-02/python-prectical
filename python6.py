print("I. input() & print() function\n")

name = input("Enter your name:")
age = input("Enter your age:")

print("\nHello", name, "you are", age, "years old.")
print("*" * 45 + "\n")

print("II. ‘sep’ attribute\n")

print("Date", "Month", "Year", sep="-")
print("Red", "Green", "Blue", sep=" | ")
print("*" * 45 + "\n")

print("III. ‘end’ attribute\n")

print("Loading", end="... ")
print("Done!")
print("*" * 45 + "\n")

print("IV. replacement Operator ({ })\n")

print("Hello {0}, you are {1} years old.".format(name, age))
print("*" * 45 + "\n")