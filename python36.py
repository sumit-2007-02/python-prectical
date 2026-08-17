def find_length(data):
    count = 0

    for item in data:
        count = count + 1

    return count


# Example with string
string = "Python"
print("Length of string =", find_length(string))

# Example with list
my_list = [10, 20, 30, 40, 50]
print("Length of list =", find_length(my_list))