file = open("sample.txt", "r")

# Read contents of file
data = file.read()

# Close the file
file.close()

# Create an empty dictionary
frequency = {}

# Count each character
for char in data:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Display character frequency
print("Character Frequency:")

for char, count in frequency.items():
    print(char, "=", count)