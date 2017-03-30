""" Python training exercise

Bob database entry - as a list

Below is a list containing information about "Bob".
"""

record = ['Bob', 'Builder, the', 1.85, 34, '2 Main Street']


# (a) Get and print Bob's age (index 3), height and address.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
age = record[3]
height = record[2]
address = record[4]
print("Bob's age is", age)
print("Bob's height is", height)
print("Bob's address is", address)
# =======

# (b) Append Bob's post code (AB25 1SP) to the end of the list.
#     HINT: Use the append sub-function of the list.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
record.append('AB25 1SP')
print("Bob's record after added post code:")
print(record)
# =======

# (c)  Today is Bob's birthday.  Increase his age by one.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
age = record[3] + 1
record[3] = age

# Alternative solution:
record[3] += 1
print("Bob's record after increase his age:")
print(record)
# =======

# (d) Bob has moved house.  His new street is 16 Bank Lane, AB16 3DD.  Update
#     the list with this new information.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
record[4] = '16 Bank Lane'
record[5] = 'AB16 3DD'
# Alternatively,
record[4:6] = ['16 Bank Lane', 'AB16 3DD']
print("Bob's record after changing address:")
print(record)
# =======
