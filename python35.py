def is_vowel(ch):
    if ch in "aeiouAEIOU":
        return True
    else:
        return False

# Input from user
ch = input("Enter a character: ")

# Check the character
if is_vowel(ch):
    print("True - It is a vowel.")
else:
    print("False - It is not a vowel.")