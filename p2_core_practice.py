
# PYTHON MCQ

# Q.1 Consider the following Python code snippet:

data = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6]} 
result = [] 
for key in data: 
        for value in data[key]: 
            if value % 2 == 0: 
             result.append((key, value)) 
result.sort(key=lambda x: x[1], reverse=True) 
print(result)#[('c', 6), ('b', 4), ('a', 2)]

# After executing the above code, what is the content of the result list?
# A) [('c', 6), ('b', 4), ('a', 2)]
# B) [('a', 2), ('b', 4), ('c', 6)]
# C) [('b', 5), ('a', 3), ('c', 6)]
# D) [('c', 6), ('b', 5), ('a', 2)]


# Q.2 What will be the output of the following code snippet?
for i in range(5): 
    print(i) 
else: 
    print("Done") 
# 0
# 1
# 2
# 3
# 4
# Done

# A) 0 1 2 3 4 followed by "Done"
# B) 0 1 2 3 4 without "Done"
# C) "Done" only
# D) SyntaxError

# Q.3 What is the output of the following code?
# def make_multiplier_of(n): 
# return lambda x: x * n 
# times3 = make_multiplier_of(3) 
# times5 = make_multiplier_of(5) 
# print(times3(times5(2))) 

# A) 30
# B) 10
# C) 6
# D) 15

# Q.4 What does the following code snippet return?
# def foo(a, b=[]): 
# b.append(a) 
# return b 
# print(foo(1)) 
# print(foo(2,[])) 
# print(foo(3)) 

# A) [1], [2], [3]
# B) [1], [2], [3, 3]
# C) [1, 3], [2], [1, 3]
# D) [1], [2], [1, 3]

# Q.5 What is the result of executing the following code?
# d = lambda p: p * 2 
# t = lambda p: p * 3 x = 2 
# x = d(x) 
# x = t(x) 
# x = d(x) 
# print(x) 
# A) 24
# B) 36
# C) 12
# D) 18
# PYTHON PROGRAM QUESTION

# Q.6 Write a Python program that prints all prime numbers up to a specified integer n.
n = int(input("Enter number: "))

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1): # 0.5 is square root 1/2
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')





# Q.7 Write a Python function named print_armstrong_numbers that prints all Armstrong numbers between 1 and 2000. An Armstrong number 
# (also known as a narcissistic number) is an integer such that the sum of its own digits raised to the power of the number of digits 
# is equal to the number itself.
# For example, 153 is an Armstrong number because 13+53+33=15313+53+33=153.


# Q.8 Example Output for n = 4:


# 1 
# 2*2 
# 3***3 
# 1234 
# 3***3 
# 2*2 
# 1 

# Example Output for n = 5:
# 1 
# 2*2 
# 3***3 
# 4*****4 
# 12345 
# 4*****4 
# 3***3 
# 2*2 
# 1

# Q.9 Python Challenge: Longest Palindromic Subsequence
# Problem Statement:
# Given a string s, write a Python function longest_palindromic_subsequence(s) that returns the length of the longest palindromic subsequence in s. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a word, phrase, number, or other sequences of characters that reads the same backward as forward.
# Objective:
# Your task is to implement a solution using dynamic programming to efficiently find the length of the longest palindromic subsequence.
# Example Usage:
# s = "bbbab" 
# print(longest_palindromic_subsequence(s)) 
# Expected Output:
# 4

# Q.10 Python Challenge: Nested Dictionary Transformation
# Problem Statement:
# Given a nested dictionary that represents data from various departments of a company, where each department has several teams, and each team has a list of employees with their respective salaries, write a Python function transform_structure(dept_data) that performs the following operations:
# Salary Adjustment: Increase the salary of every employee by a fixed percentage passed as an argument to the function. The percentage should be applied differently based on conditions that you define (e.g., different departments might have different adjustment rates).
# Flattening Structure: Transform the nested dictionary into a flat dictionary where each key is a unique identifier (you may construct this identifier by concatenating department and team names, or any other method you deem suitable) and the value is the average salary of the team after adjustment.
# Filtering: After flattening, filter out any entries where the average salary (post-adjustment) is below a certain threshold, also passed as an argument to the function.
# Sorting and Ranking: Finally, return a list of tuples sorted by the average salary in descending order. Each tuple should contain the unique identifier and the average salary.



# Example Input:


# dept_data = {
#     'Engineering': {
#         'DevOps': [{'name': 'Alice', 'salary': 1000}, {'name': 'Bob', 'salary': 1100}],
#         'Backend': [{'name': 'Charlie', 'salary': 1050}, {'name': 'David', 'salary': 1200}],
#     },
#     'HR': {
#         'Recruitment': [{'name': 'Eve', 'salary': 950}, {'name': 'Frank', 'salary': 990}],
#     },
# }
# percentage = 10  # Percentage increase
# threshold = 1100  # Minimum average salary threshold
