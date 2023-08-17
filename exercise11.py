import random
import tkinter as tk

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

    if start_index is not None:
        end_index = len(memory_usage) - 1
        if (end_index - start_index + 1) * interval >= during_time:
            periods.append((start_index, end_index))

    return periods

def generate_memory_usage():
    length = 20
    min_value = 30
    max_value = 100
    memory_usage = generate_random_memory_usage(length, min_value, max_value)
    return memory_usage

def detect_periods(memory_usage, threshold, interval, during_time):
    periods = detect_memory_usage_periods(memory_usage, threshold, interval, during_time)
    return periods

def show_results():
    memory_usage = generate_memory_usage()
    threshold = 40
    interval = 5
    during_time = 15

    periods = detect_periods(memory_usage, threshold, interval, during_time)

    result_text = ""

    if periods:
        result_text += "Detected Memory Usage Periods:\n"
        for start_index, end_index in periods:
            duration = (end_index - start_index + 1) * interval
            result_text += f"From index {start_index} to {end_index}, duration: {duration} minutes\n"
    else:
        result_text = "No memory usage periods detected."

    result_label.config(text=result_text)

# Create the GUI window
window = tk.Tk()
window.title("Memory Usage Detector")

# Create the result label
result_label = tk.Label(window, wraplength=300)
result_label.pack(pady=10)

# Create the button to trigger the detection
detect_button = tk.Button(window, text="Detect Memory Usage", command=show_results)
detect_button.pack(pady=10)

# Start the GUI main loop
window.mainloop()