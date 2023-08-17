import random


def filter_numbers(numbers):
    filtered_numbers = [num for num in numbers if num >= 50]
    return filtered_numbers

# numbers = [5, 89, 72, 14, 32, 54, 32, 93, 49, 20, 93, 65, 44, 50]

n = 10  # Number of items in the array

numbers = [random.randint(1, 100) for _ in range(n)]

print(numbers)
filtered_numbers = filter_numbers(numbers)

# Print the filtered numbers
print(filtered_numbers)