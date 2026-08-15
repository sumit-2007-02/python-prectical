file = open("sample.txt", "w")

file.write("Hello, this is a Python file handling program.\n")
file.write("We are performing write and read operations.")

file.close()

print("Data written successfully.")

# Read operation
file = open("sample.txt", "r")

data = file.read()

print("\nData read from file:")
print(data)

file.close()