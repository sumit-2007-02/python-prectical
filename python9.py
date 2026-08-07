print("=== i) BREAK STATEMENT ===")
print("Searching for number 5 in range 1 to 10...")

for i in range(1, 11):
    if i == 5:
        print(f"-> Found {i}! Breaking out of the loop.")
        break  # Loop ends immediately
    print(f"Processing number: {i}")

print("Loop finished (terminated early by break).\n")
print("-" * 50 + "\n")