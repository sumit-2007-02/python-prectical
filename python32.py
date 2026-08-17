def check_armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if total == original:
        return True
    else:
        return False


# Get input from user
num = int(input("Enter a number: "))

# Check Armstrong
if check_armstrong(num):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")