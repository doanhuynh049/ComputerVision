def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero")
    except (ValueError, TypeError):
        print("Error: Invalid input")
    else:
        print("Result:", result)
    finally:
        print("Cleanup")

# Main program
x = 10
y = 0

divide_numbers(x, y)
