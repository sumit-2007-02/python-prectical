source = open("sample.txt", "r")

# Read contents of source file
data = source.read()

# Close source file
source.close()

# Open destination file in write mode
destination = open("destination.txt", "w")

# Write contents into destination file
destination.write(data)

# Close destination file
destination.close()

print("File contents copied successfully.")