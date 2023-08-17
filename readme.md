
Computer Vision 
Question: 
1.	Have you ever heard/seen an application of computer vision/machine learning? What is it? What does it do? What kind of problem does it solve?

yes, computer vision and machine learning are used in multiple applications, such as autonomous vehicles, object recognition (face, body), robotics, diagnosis of diseases based on imaging (skin, CT scan of lungs) …
In autonomous vehicles, computer vision will process data captured by camera on vehicle. it analyzes and interprets the information of camera to understand the surrounding environment, detect objects such as pedestrians, vehicle, traffic light, make the appropriate decisions. Machine learning is often utilized to train models that can accurately recognize and classify objects in real-time. 
The primary problem that CV and ML in autonomous vehicles solve is perception and object recognition. By immediately detecting and understanding the objects in the environment, autonomous vehicles can make informed decisions about navigation, obstacle avoidance, and following traffic rules. This technology has the potential to significantly improve road safety, reduce accidents caused by human error, and provide enhanced transportation solutions.

2.	If you were the one who developed that application, what would be your priorities/concerns?
If I were the developer of application utilizing CV and ML. it has some priorities and concerns that I would consider:
Accurate data: collecting a diverse and representative dataset would be crucial for training learning model. Collected data cover all of scenarios and variations that maybe encounter in the target environment. Ensuring the quality and accuracy of labeled data to avoid biases and improve the model’s quality.
Accuracy of training model: the agent could achieve high accuracy in the application’s output. It relates to selecting and training appropriate model (self-driving vehicle use reinforcement learning, machine learning used for image classification). we need to optimize parameter and ensuring they can perform in the real-world.
In addition to, it has some factors that we need to concern are security (potential vulnerabilities in the application like system error, attack human), ethical consideration, scalability and adaptability.
3.	How will you form an approach for a problem?
Understand the problem: clear understanding of the problem you are trying to solve. determine and analyze the problem statement, identify the key objectives, then establish the success criteria. Gather relevant data to solve the problem, requirement and constraint related to the problem. If data’s problem happens, I will evaluate the quality and available of data, perform necessary data preprocessing step such as cleaning, normalization and feature engineering. Split data into training, validation and testing sets. Choose the appropriate model that suitable for the problem such as type of problem (classification, regression). 
4.	How will you track your assignments/tasks?
To track the assignments/ tasks, I use some following approaches:
List To-Do: I create tablework to list all assignments and task the everyday. I often use the google To-Do list tool to make sure the prioritize tasks, set due dates and update the status of my progress.
Use Calendar: list all tasks for a week along with allocated time for particular task with start time and end time. It helps me analyze and manage my time effectively
Excel: use excel combined V-model to track the assignments, identify what stage is the project in and what will we do in the next stage. 
5.	How will you react when you have an assignment that you have never got before?
When facing with an assignment or task that I have never encountered before, I would approach it like that:
-	Gather relevant information: I would start researching and look for document from internet, AI, and seeking guidance from colleagues. 
-	Break it down: I would break down the assignment into smaller, manageable components or sub-task. This help divided the large tasks into each step. it’s like the step of the stair. It helps in understanding the problem and allows for a systematic approach to solving it.
-	Make plan: it is outline of steps needed to complete the task. Learning new concepts and techniques along the way to work on the assignment. I will adapt to suitable for the project.
6.	What do you know about virtual environment, what is the benefit of using a virtual environment?
Virtual environment is a software emulation of a physical computer system. It also creates and run multiple OS and its associated software on a single physical machine. It is also an isolated environment that allow developers to manage project dependencies, isolate project-specific packages and libraries from the system-level installations. 
The benefits of using virtual environments include:
•	Dependency management: Virtual environments enable you to install project-specific dependencies without interfering with other projects or the system environment.
•	Isolation: Each virtual environment is isolated from others, which means that changes made to one environment do not affect others.
•	Portability: Virtual environments can be easily shared with others or deployed to production environments. You can package the virtual environment along with your code, ensuring that the project's dependencies are self-contained and reproducible.
•	Easy setup and cleanup: Creating a virtual environment is a straightforward process, usually done with a few simple commands. Similarly, when you're done with a virtual environment, you can easily delete it without leaving any traces on your system.

7.	How to catch and handle exceptions in Python? What do you think is the best way to handle exceptions? 
In Python, exceptions are used to handle errors and exceptional situations that may occur during program execution. To catch and handle exceptions, you can use a combination of the try, except, else, and finally blocks.
Here's how exception handling works in Python: 
•	The try block: You enclose the code that might raise an exception within a try block. If an exception occurs within the try block, the remaining code within the block is skipped. 
•	The except block: Immediately following the try block, you can add one or more except blocks to catch specific types of exceptions. Each except block specifies the exception type it can handle and the code to execute if that exception occurs. 
•	The else block (optional): After the except block(s), you can include an else block that is executed only if no exceptions occurred in the try block. It is useful for code that should run only when no exceptions are raised. 
•	The finally block (optional): After the except or else block(s), you can include a finally block that is always executed regardless of whether an exception occurred. It is commonly used for cleanup tasks, such as closing files or releasing resources.
Example: 
 
if a ZeroDivisionError occurs, the first except block is executed. If a ValueError or TypeError occurs, the second except block is executed. If no exceptions occur, the else block is executed. Finally, the finally block is always executed, regardless of whether an exception occurred.
The best way to handle exceptions depends on the specific situation and the requirements of your program. It is generally recommended to: 
•	Catch specific exceptions: Handle specific exception types to provide targeted error messages or take appropriate actions based on the type of error. 
•	Provide informative error messages: Include meaningful error messages in your exception handling code to aid in debugging and troubleshooting. 
•	Avoid catching broad exceptions: While it's possible to catch the base Exception class to handle all exceptions, it's generally better to catch specific exceptions to avoid masking unexpected errors. 
•	Use the finally block for cleanup: If I have cleanup tasks, such as closing files or releasing resources, place them in the finally block to ensure they are always executed, regardless of exceptions. 
•	Log or report exceptions: Consider logging or reporting exceptions to capture information about errors for debugging and monitoring purposes.

8.	Solve this problem:
    + You have this array of integer: [5, 89, 72, 14, 32, 54, 32, 93, 49, 20, 93, 65, 44, ...] with n items.
    + Write a Python script to extract only number >= 50
    + You are not allowed to create a temporary variable (list)
    + Explain your choice of algorithm
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
 

Explain my choice of algorithm
1.	We define a function filter_numbers that takes the numbers list as input.
2.	Inside the function, we use a list comprehension to create a new list called filtered_numbers. The list comprehension iterates over each element in the numbers list and checks if the number is greater than or equal to 50. If it is, the number is included in the filtered_numbers list.
3.	The filtered_numbers list is then returned from the function.
4.	In the main program, we call the filter_numbers function with the numbers list. The returned filtered_numbers list contains only the numbers greater than or equal to 50.
5.	Finally, we print the filtered_numbers.


9.	 Solve this problem:
    + You have this input array: [12, 15, 17, 17, 17, 19, 14, 16, 18, 22, 24, 32, 45, 45, 50, 56, 62, 60, 60, 42, 22, 38, 40, 42, 43, 43, 45, 42, 37, 35, 20, 18, 17, 17, 17, 20, 17]
    + This array represents the value of memory usage over time, of interval 5 minutes.
    + Write a Python script to detect raising and prolonging periods of memory usage.
        + The use case for this is: to detect if memory is rising for the last 15 minutes
        + The memory usage is higher than a certain threshold
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

# Print the detected periods
for start_index, end_index in periods:
    print(f"Memory usage rising for the last {(end_index - start_index + 1) * interval} minutes from index {start_index} onwards.")
 
10.	Problem:
    + You have the number 10000! (ten thousand factorial)
    + Let say number 120 has 1 zero on the right, 7200 has 2 zeros on the right, 302902000 has 3 zeros on the right.
    + 10000! have n zeros on the right.
    + Suggest a way to find n.
    + Bonus: suppose you don't need to worry about computing time, no time limit. Suggest an approach to calculate the value of 10000!
To find the number of trailing zeros in the factorial of a given number I use the concept of prime factorization. The number of trailing zeros in the factorial is determined by the number of times the prime factor 5 appears in the product. 
Here's an approach to calculate the number of trailing zeros in 10000!: 
•	Initialize a variable count to 0. 
•	Start a loop from i = 5 and continue while i is less than or equal to 10000.
•	For each iteration, divide 10000 by i and add the result to count. 
•	Increment i by 5 in each iteration (since we are interested in the prime factor 5). After the loop ends, the value of count will be the number of trailing zeros in 10000!.
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
 

