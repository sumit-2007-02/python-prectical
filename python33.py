def check_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False


# Input from user
num = int(input("Enter a number: "))

# Check Palindrome
if check_palindrome(num):
    print("The number is Palindrome.")
else:
    print("The number is not Palindrome.")