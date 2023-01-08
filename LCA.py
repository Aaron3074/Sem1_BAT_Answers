# 1.Create a list of first 5 even numbers using list comprehension.

even_numbers = [i for i in range(2, 12, 2) if i <= 10]
print(even_numbers)


# 2.Write a Python program to Multiply every element of a list by five and assign it to a new list using list comprehension.

# create a list of numbers
numbers = [1, 2, 3, 4, 5]

# create a new list with the elements multiplied by 5
multiplied_numbers = [i*5 for i in numbers]

print(multiplied_numbers)


# 3.Write a program using list comprehension to extract and print all the numbers from a given string.

# define the string
string = "There are 3 apples and 5 oranges in the basket."

# extract the numbers from the string using a list comprehension
numbers = [int(c) for c in string if c.isdigit()]

print(numbers)


# 4.Write a Python program to Matrix addition and Multiplication using list comprehension.

# define the matrices
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# perform matrix addition using list comprehension
result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print(result)

# perform matrix multiplication using list comprehension
result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

print(result)


# 5.Write a Python program to create a new list of Numbers that are divisible by 7 from all the numbers in the range of 1-1000.

# create a new list of numbers divisible by 7 using a list comprehension
numbers = [x for x in range(1, 1000) if x % 7 == 0]

print(numbers)


# Code Written by Aaron D'Costa(22BRS1129).

