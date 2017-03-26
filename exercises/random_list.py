""" Python training exercise

Random list

Below is a list of random numbers between 0 and 100.  Using built-in funcions
and the list sub-functions, can you?:

(a) Sort the list?
    HINT: Use the sorted() built-in function.

(b) What are the smallest and largest numbers?
    HINT: There are two ways to do this; get directly from the ordered list, or
          use the built-in min/max functions.

(c) How many numbers are greater than or equal to 50?
    HINT: Use the index sub-function to locate 50 in the ordered data.
"""

data = [
    41, 26, 45, 8, 67, 98, 1, 43, 19, 62, 11, 47, 46, 1, 29, 36, 69, 59, 65, 96,
    91, 76, 53, 100, 17, 89, 38, 50, 82, 99, 63, 16, 64, 65, 75, 68, 99, 27, 8,
    92, 17, 91, 3, 41, 40, 32, 29, 49, 54, 90, 55, 7, 38, 11, 33, 56, 87, 27,
    31, 82, 96, 26, 66, 61, 65, 66, 4, 43, 10, 80, 13, 22, 12, 62, 24, 61, 67,
    88, 73, 24, 14, 35, 38, 71, 87, 96, 42, 95, 91, 83, 46, 38, 26, 22, 86, 79,
    86, 98, 58, 28, 44, 30, 60, 17, 48, 56, 77, 32, 44, 26, 50, 62, 49, 55, 6,
    18, 60, 22, 45, 97, 51, 53, 59, 93, 35, 29, 52, 91, 33, 56, 95, 23, 69, 54,
    4, 83, 17, 73, 46, 79, 99, 75, 53, 20, 96, 91, 72, 93, 32, 9, 54, 45, 80,
    88, 10, 93, 24, 15, 84, 67, 68, 13, 60, 9, 31, 87, 80, 87, 29, 24, 27, 81,
    28, 22, 11, 0, 79, 47, 60, 17, 98, 84, 43, 62, 46, 64, 41, 27, 41, 0, 73,
    89, 1, 92, 12, 1, 49, 46, 54, 99
]


# (a) Sort the list.
#     HINT: Use the sorted() built-in function.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
ordered_data = sorted(data)
print(ordered_data)
# =======

# (b) What are the smallest and largest numbers?
#     HINT: There are two ways to do this; get directly from the ordered list,
#     or use the built-in min/max functions.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
# There are two ways to do this.  Either get directly from the ordered list, or
# use the built-in min/max functions.
smallest = ordered_data[0]
smallest = min(data)
print('Smallest number is {}.'.format(smallest))

largest = ordered_data[-1]
largest = max(data)
print('Largest number is {}.'.format(largest))
# =======

# (c) How many numbers are greater than or equal to 50?
#     HINT: Use the index sub-function to locate 50 in the ordered data.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
i = ordered_data.index(50)
n = len(ordered_data) - i
print('There are {} numbers >= 50.'.format(n))
# =======
