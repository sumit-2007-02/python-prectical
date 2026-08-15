file = open("sample.txt", "r")

# Read the complete file
data = file.read()

# Count characters
characters = len(data)

# Count words
words = len(data.split())

# Count lines
lines = len(data.splitlines())

# Close the file
file.close()

# Display the results
print("Number of Characters =", characters)
print("Number of Words      =", words)
print("Number of Lines      =", lines)