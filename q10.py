import math

def calculate_trailing_zeros(n):
    count = 0
    i = 5

    while i <= n:
        count += n // i
        i *= 5

    return count

n = 1000
trailing_zeros = calculate_trailing_zeros(n)
print(f"The number of trailing zeros in {n}! is {trailing_zeros}.")
factorial = math.factorial(n)
print(f"The value of {n}! is {factorial}.")