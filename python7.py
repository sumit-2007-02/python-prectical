print("I. IF STATEMENT\n")
temperature = 35

if temperature > 30:
    print("Temperature is {0}°C.".format(temperature))
    print("It's a hot day outside!")

print("-" * 45 + "\n")

print("II. IF-ELSE STATEMENT\n")
age = int(input("Enter your age: "))

if age >= 18:
    print("Age: {0} -> You are eligible to vote.".format(age))
else:
    print("Age: {0} -> You are NOT eligible to vote yet.".format(age))

print("-" * 45 + "\n")

print("III. IF-ELIF-ELSE STATEMENT\n")
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 35:
    grade = "Pass"
else:
    grade = "Fail"

print("Marks: {0} -> Final Grade: {1}".format(marks, grade))

print("-" * 45 + "\n")