import random

def generate_random_memory_usage(length, min_value, max_value):
    memory_usage = [random.randint(min_value, max_value) for _ in range(length)]
    return memory_usage

def detect_memory_usage_periods(memory_usage, threshold, interval, during_time):
    periods = []
    start_index = None

    for i, usage in enumerate(memory_usage):
        if usage >= threshold:
            if start_index is None:
                start_index = i
        else:
            if start_index is not None:
                end_index = i - 1
                if (end_index - start_index + 1) * interval >= during_time:
                    periods.append((start_index, end_index))
                start_index = None

    if (start_index is not None):
        end_index = len(memory_usage) - 1
        if ((end_index - start_index + 1 ) * interval >= during_time):
            periods.append((start_index, end_index))

    return periods

# Example usage
# memory_usage = [12, 15, 17, 17, 17, 19, 14, 16, 18, 22, 24, 32, 45, 45, 50, 56, 62, 60, 60, 42, 22, 38, 40, 42, 43, 43, 45, 42, 37, 35, 20, 18, 17, 17, 17, 20, 17]
# memory_usage = [12, 15, 32, 50, 40, 40, 32, 12, 35, 50, 40]

# Generate a random memory usage list
length = 20
min_value = 30
max_value = 100
memory_usage = generate_random_memory_usage(length, min_value, max_value)
print(memory_usage)

threshold = 40
interval = 5
during_time = 15

# Call the function to detect memory usage periods
periods = detect_memory_usage_periods(memory_usage, threshold, interval, during_time)

# # Print the detected periods
# for start_index, end_index in periods:
#     print(f"Memory usage rising for the last {(end_index - start_index + 1) * interval} minutes from index {start_index} onwards.")


# Print the detected periods
if periods:
    print("Detected Memory Usage Periods:")
    for start_index, end_index in periods:
        duration = (end_index - start_index + 1) * interval
        print(f"From index {start_index} to {end_index}, duration: {duration} minutes")
else:
    print("No memory usage periods detected.")
    
    