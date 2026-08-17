file = open("s.txt", "r")

print("Lines in reverse order:")

# Read each line and reverse it
for line in file:
    print(line.rstrip()[::-1])

# Close the file
file.close()