""" Python training exercise

Bob database entry - as a dictionary

Below is a list containing information about "Bob".
"""

record = {
    'name': 'Bob',
    'surname': 'Builder, the',
    'height': 1.85,
    'age': 34,
    'address': '2 Main Street'
}


# (a) Get and print Bob's age, height and address.

# YOUR CODE HERE.
age = record['age']
# <<<<<<< SOLUTION
height = record['height']
address = record['address']
print("Bob's age is", age)
print("Bob's height is", height)
print("Bob's address is", address)
# =======

# (b) Append Bob's post code (AB25 1SP) to the end of the list.
#     HINT: Use the append sub-function of the list.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
record['postcode'] = 'AB25 1SP'
print("Bob's record after added post code:")
print(record)
# =======

# (c)  Today is Bob's birthday.  Increase his age by one.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
age = record['age'] + 1
record['age'] = age
print("Bob's record after increase his age:")
print(record)

# Alternative solution:
record['age'] += 1
print("Bob's record after increase his age a second time:")
print(record)
# =======

# (d) Bob has moved house.  His new street is 16 Bank Lane, AB16 3DD.  Update
#     the list with this new information.

# YOUR CODE HERE.
# <<<<<<< SOLUTION
record['address'] = '16 Bank Lane'
record['postcode'] = 'AB16 3DD'
# Alternatively,
new_data = {'address': '16 Bank Lane', 'postcode': 'AB16 3DD'}
record.update(new_data)
print("Bob's record after changing address:")
print(record)
# =======
