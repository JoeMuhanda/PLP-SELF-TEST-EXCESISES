import random

# Generate a list of random numbers
numbers = [random.randint(0, 9) for i in range(10)]
print("List of numbers:", numbers)

# Ask the user for a number to search for
search_num = int(input("Enter a number to search for: "))

# Implement linear search algorithm
def linear_search(numbers, search_num):
    for index, num in enumerate(numbers):
        if num == search_num:
            return index
    return "Number not found"

# Call the linear_search function and print the result
result = linear_search(numbers, search_num)
print("Result:", result)
