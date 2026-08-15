# Global variable
x = 100

def display():
    # Local variable
    y = 50

    print("Global variable x =", x)
    print("Local variable y =", y)

# Function call
display()

# Global variable can be accessed outside the function
print("Outside function, Global variable x =", x)