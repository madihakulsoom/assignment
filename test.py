# 1.Create a tuple of numbers. Write a function that returns the sum of the numbers in the
# tuple.


def sums(num):
    return sum(num)
numbers = (3, 7, 2, 9)
result = sums(numbers)
print(result)


# 2.Write a function that takes a list of strings and returns the list with its elements
# reversed.
fruits = ['apple', 'banana', 'cherry']
abc=fruits[::-1]
print(abc)

# 3.Create two dictionaries with some overlapping keys. Write a function that merges them,
# giving priority to values in the second dictionary for overlapping keys.

d1={'a':1,'b':2,'c':3}
d2={'c':4,'b':5,'a':6}
def merge_dic(d1,d2):
    dict=d1.copy()
    dict.update(d2)
    return dict
result=merge_dic(d1,d2)
print(result)

# Count Vowels in a String
# 4.Write a function that takes a string and returns a dictionary with the count of each
# vowel in the string.

# Find Common Elements
# 5.Write a function that takes two lists and returns a list of elements that are common to
# both lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
def common_elements(list1, list2):
    return list(set(list1) & set(list2))
print(common_elements(list1, list2))

# Sort a List of Tuples
# 6.Create a list of tuples representing (name, age). Write a function to sort this list
# by age.
#
# Create a Nested Dictionary
# 7.Create a nested dictionary representing a classroom, where each student has a name and a list of grades.
# Write a function to calculate the average grade for each student.
classroom = {
    'student1': {'name': 'Alice', 'grades': [85, 90, 78]},
    'student2': {'name': 'Bob', 'grades': [82, 88, 91]},
    'student3': {'name': 'Charlie', 'grades': [95, 85, 87]}
}
def calculate_average_grades(classroom):
    average_grades = {}
    for student_id, student_info in classroom.items():
        name = student_info['name']
        grades = student_info['grades']
        average = sum(grades) / len(grades)
        average_grades[name] = average
    return average_grades
average_grades = calculate_average_grades(classroom)
print(average_grades)

# Filter Even Numbers
# 8.Write a function that takes a list of integers and returns a new list containing only the even numbers.
def even(x):
    if x % 2==0:
        return True
    return False
list11=[1,2,3,4,5,6,7,8,9]
result=filter(even, list11)
print("even numbers are:" ,list(result))
# Flatten a List of Lists
# 9.Given a list of lists, write a function that flattens it into a single list.
def flatten(nested_list):
    return [num for sublist in list12 for num in sublist]
list12=[[1],[2,3],[4,5,6]]
f1=flatten(list12)
print(f1)
# Unique Elements
# 10.Write a function that takes a list and returns a list of unique elements, preserving the original order.
list22= [3, 4, 5, 6, 7,7,3,3]
def commonelements(list22):
    return list(set(list22))
print(commonelements(list22))
# Character Frequency
# 11.Write a function that takes a string and returns a dictionary with each character as a key and its frequency as the value.
def count(string):
    my_dict = {}
    for i in string:
        my_dict[i] = my_dict.get(i,0) + 1
    return my_dict
input_string = "hello world"
character_frequency = count(input_string)
print(character_frequency)
# Temperature Conversion
# 12.Create a function that takes a list of temperatures in Celsius and returns a list of the corresponding temperatures in Fahrenheit.
def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = [(temp * 9 / 5) + 32 for temp in celsius_list]
    return fahrenheit_list
celsius_temperatures = [0, 20, 37, 100]
fahrenheit_temperatures = celsius_to_fahrenheit(celsius_temperatures)
print(fahrenheit_temperatures)
# List Comprehension with Conditions
# 13.Using list comprehension, create a list of squares of even numbers from a given list of integers.
def square_of_even_numbers(nums):
    return [num ** 2 for num in nums if num % 2 == 0]
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_even = square_of_even_numbers(input_list)
print(squares_of_even)
# Remove Duplicates from a List
# 14,Write a function that removes duplicate values from a list while maintaining the original order of elements.
#
# Matrix Transposition
# 15.Write a function that takes a 2D list (matrix) and returns its transpose.
#
